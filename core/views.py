from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, generics, status, filters

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, renderer_classes, permission_classes

# Create your views here.


class user_list_view(viewsets.ModelViewSet):
    # permission_classes([IsAuthenticated])
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()#.exclude(userType="Super Admin")
    serializer_class = UserDetailsSerializer
    http_method_names = ['get','put','head']
    # code below is to override methods and implement custom method
    # def create(self, request, *args, **kwargs):
    #     try:
    #         data = request.data
           
    #         new_user=User.objects.create(
    #             first_name=request.data['first_name'],
    #             last_name=request.data['last_name'],
    #             email=request.data['email'],
    #             phone=request.data['phone'],
    #             role=request.data['role'],
    #             position=request.data['position'],
    #         )
           
           
    #         new_user.save()
    #         return Response(status=200)
    #     except Exception as e:
    #         print(e)
    #         return Response({status:500,'message':"Internal server error"})

# def 