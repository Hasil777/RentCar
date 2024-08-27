from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *


class CarView(APIView):
    def get(self,request):
        model = Car.objects.all()
        serializer = CarSerializer(model,many=True)
        return Response(serializer.data)

class CarDetailView(generics.RetrieveAPIView):
    lookup_field = 'name'
    queryset = Car.objects.all()
    serializer_class=CarSerializer

class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class CarViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAdminUser,)
    serializer_class = CarSerializer
    queryset = Car.objects.all()
