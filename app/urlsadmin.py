from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'car/create',CarViewSet, basename='posts')
urlpatterns = router.urls