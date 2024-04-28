from django.urls import path
from shop.views import get_product_list
from shop.views import get_product_detail

app_name = "shop"

urlpatterns = [
    path("", get_product_list, name="product_list"),
    path("<slug:category_slug>/", get_product_list, name="product_list_by_category"),
    path("<int:id>/<slug:slug>/", get_product_detail, name="product_detail"),
]
