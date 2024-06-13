from django.urls import path
from order.views import CreateOrder
from order.views import CreateShipment

urlpatterns = [
    path('orders', CreateOrder.as_view()),
    path('shipments', CreateShipment.as_view()),
]