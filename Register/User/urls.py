from django.urls import path

from .views import index, create_user

urlpatterns = [
    path('', index),
    path('create', create_user),
]