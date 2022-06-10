from django import views
from django.urls import path
from .views.first_view import users_generator

urlpatterns = [
    path('', view=users_generator),
]