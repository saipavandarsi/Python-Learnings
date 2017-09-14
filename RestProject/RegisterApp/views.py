# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt

from .models import UserProfile
from .serializers import UserProfileSerializer

@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.AllowAny,])
def create_user(request):
    """
    Create a New User
    :param request: 
    :return: 
    """
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
@permission_classes([permissions.AllowAny,])
def get_users(request):
    """"
    """
    allusers = UserProfile.objects.all()
    serializer = UserProfileSerializer(allusers,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
