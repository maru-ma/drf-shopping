from rest_framework import routers

from django.contrib import admin
from django.urls import path, include
from shopping_list.api.viewsets import ShoppingItemViewset


router = routers.DefaultRouter()
router.register("shopping-items", ShoppingItemViewset, basename="shopping-items")

urlpatterns = [
    path("api/", include(router.urls)),
]

