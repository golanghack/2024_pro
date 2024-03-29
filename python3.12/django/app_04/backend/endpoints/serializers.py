from rest_framework import serializers
from endpoints.models import Endpoint
from endpoints.models import MLAlgo
from endpoints.models import MLAlgoStatus
from endpoints.models import MLRequest
from endpoints.models import ABTest


class EndpointSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        read_only_fields = (
            "id",
            "name",
            "owner",
            "created_at",
        )
        fields = read_only_fields


class MLAlgoSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlalgo):
        return (
            MLAlgoStatus.objects.filter(parent_mlalgo=mlalgo)
            .latest("created_at")
            .status
        )

    class Meta:
        model = MLAlgo
        read_only_fields = (
            "id",
            "name",
            "description",
            "code",
            "version",
            "owner",
            "created_at",
            "parent_endpoint",
            "current_status",
        )
        fields = read_only_fields


class MLAlgoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgoStatus
        read_only_fields = (
            "id",
            "active",
        )
        fields = (
            "id",
            "active",
            "status",
            "created_by",
            "created_at",
            "parent_mlalgo",
        )


class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgo",
        )
        fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "feedback",
            "created_at",
            "parent_mlalgo",
        )


class ABTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABTest
        read_only_fields = (
            "id",
            "ended_at",
            "created_at",
            "summary",
        )
        fields = (
            "id",
            "title",
            "created_by",
            "created_at",
            "ended_at",
            "summary",
            "parent_mlalgo_1",
            "parent_mlalgo_2",
        )
