from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from django.db.models import F
from django.db import transaction

import datetime
import json
from numpy.random import rand

from endpoints.models import Endpoint
from endpoints.serializers import EndpointSerialiser

from endpoints.models import MLAlgo
from endpoints.serializers import MLAlgoSerializer

from endpoints.models import MLAlgoStatus
from endpoints.serializers import MLAlgoStatusSerializer

from endpoints.models import MLRequest
from endpoints.serializers import MLRequestSerializer

from endpoints.models import ABTest
from endpoints.serializers import ABTestSerializer

from ml.registry import MLRegistry
from server.wsgi import registry


class EndpointViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = EndpointSerialiser
    queryset = Endpoint.objects.all()


class MLAlgoViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgoSerializer
    queryset = MLAlgo.objects.all()


def deactivate_other_statuses(instance):
    old_statuses = MLAlgoStatus.objects.filter(
        parent_mlalgo=instance.parent_mlalgo,
        created_at__lt=instance.created_at,
        active=True,
    )
    for i in len(old_statuses):
        old_statuses[i].active = False
    MlAlgoStatus.objects.bulk_update(old_statuses, ["active"])


class MLAlgoStatusViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = MLAlgoStatusSerializer
    queryset = MLAlgoStatus.objects.all()

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                deactivate_other_statuses(instance)
        except Exception as err:
            raise APIException(str(err))


class MLRequestViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()


# pre-
class PredictView(views.APIView):
    def post(self, request, endpoint_name, format=None):
        algo_status = self.request.query_params.get("status", "production")
        algo_version = self.request.query_params.get("version")
        algs = MLAlgo.objects.filter(
            parent_endpoint__name=endpoint_name,
            status__status=algo_status,
            status__active=True,
        )
        if algo_version is not None:
            algs = algs.filter(version=algo_version)
        if len(algs) == 0:
            return Response(
                {"status": "Error", "message": "ML algo is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if len(algs) != 1 and algo_status != "ab_testing":
            return Response(
                {
                    "status": "Error",
                    "message": "Ml algo selection is ambiguos.Please specify algo version",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        alg_index = 0
        if algo_status == "ab_testing":
            alg_index = 0 if rand() < 0.5 else 1
        algo_object = registry.endpoints[algs[alg_index].id]
        prediction = algo_object.compute_prediction(request.data)
        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=json.dumps(request.data),
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgo=algs[alg_index],
        )
        ml_request.save()
        prediction["request_id"] = ml_request.id
        return Response(prediction)


class ABTestViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = ABTestSerializer
    queryset = ABTest.objects.all()

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save()
                # update algo
                status_1 = MLAlgoStatus(
                    status="ab_testing",
                    created_by=instance.created_by,
                    parent_mlalgo=instance.parent_mlalgo_1,
                    active=True,
                )
                status_1.save()
                deactivate_other_statuses(status_1)

                status_2 = MLAlgoStatus(
                    status="ab_testing",
                    created_by=instance.created_by,
                    parent_mlalgo=instance.parent_mlalgo_2,
                    active=True,
                )
                status_2.save()
                deactivate_other_statuses(status_2)
        except Exception as err:
            raise APIException(str(err))


class StopABTestView(views.APIView):
    def post(self, request, ab_test_id, format=None):
        try:
            ab_test = ABTest.objects.get(pk=ab_test_id)
            if ab_test.ended_at is not None:
                return Response({"message": "AB test alrwady finished."})
            date_now = datetime.datetime.now()
            # algo 1
            all_responses_1 = MLRequest.objects.filter(
                parent_mlalgo=ab_test.parent_mlalgo_1,
                created_at__gt=ab_test.created_at,
                created_at_lt=date_now,
            ).count()
            correct_response_1 = MLRequest.objects.filter(
                parent_mlalgo=ab_test.parent_mlalgo_1,
                created_at__gt=ab_test.created_at,
                created_at__lt=date_now,
                response=F("feedback"),
            ).count()
            accuracy_1 = correct_response_1 / float(all_responses_1)
            print(all_responses_1, correct_response_1, accuracy_1)

            all_responses_2 = MLRequest.objects.filter(
                parent_mlalgo=ab_test.parent_mlalgo_2,
                created_at__gt=ab_test.created_at,
                created_at__lt=date_now,
            ).count()
            correct_response_2 = MLRequest.objects.filter(
                parent_mlalgo=ab_test.parent_mlalgo_2,
                created_at__gt=ab_test.created_at,
                created_at__lt=date_now,
                response=F("feedback"),
            ).count()
            accuracy_2 = correct_response_2 / float(all_responses_2)
            print(all_responses_2, correct_response_2, accuracy_2)

            # selecting higher accuracy
            algo_id_1 = ab_test.parent_mlalgo_1
            algo_id_2 = ab_test.parent_mlalgo_2
            # swapping
            if accuracy_1 < accuracy_2:
                algo_id_1, algo_id_2 = algo_id_2, algo_id_1

            status_1 = MLAlgoStatus(
                status="production",
                created_by=ab_test.created_by,
                parent_mlalgo=algo_id_1,
                active=True,
            )
            status_1.save()
            deactivate_other_statuses(status_1)
            # update status
            status_2 = MLAlgoStatus(
                status="testing",
                created_by=ab_test.created_by,
                parent_mlalgo=algo_id_2,
                active=True,
            )
            status_2.save()
            deactivate_other_statuses(status_2)

            summary = (
                f"Algo #1 -> accuracy: {accuracy_1}, algo #2 -> accuracy: {accuracy_2}"
            )
            ab_test.ended_at = date_now
            ab_test.summary = summary
            ab_test.save()
        except Exception as err:
            return Response(
                {
                    "status": "Error",
                    "message": str(err),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "message": "AB Test finished",
                "summary": summary,
            }
        )
