from django.urls import path

from . import views

urlpatterns = [
    path("products/api/", views.product_list_api, name="product_list_api"),
    path("categories/api/", views.category_list_api, name="category_list_api"),
]