from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Car
from django.contrib.auth import get_user_model

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'