from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from endpoints.views import EndpointViewSet
from endpoints.views import MLAlgoViewSet
from endpoints.views import MLAlgoStatusViewSet
from endpoints.views import MLRequestViewSet
from endpoints.views import PredictView
from endpoints.views import ABTestViewSet
from endpoints.views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgos", MLAlgoViewSet, basename="mlalgos")
router.register(r"mlalgostatus", MLAlgoStatusViewSet, basename="mlalgostatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequest")
router.register(r"abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    re_path(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
    re_path(
        r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)",
        StopABTestView.as_view(),
        name="stop_ab",
    ),
]
