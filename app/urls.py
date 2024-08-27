from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cars/', CarView.as_view()),
    path('cars/detail/<str:name>/', CarDetailView.as_view()),
]