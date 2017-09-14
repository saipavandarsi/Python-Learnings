# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#this is for cross
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from models import UserProfile

# Create your views here.

def signup(request):
    """
    
    :param request: 
    :return: 
    """
    return render(request,'register.html')

@csrf_exempt
def create_user(request):
    """
    
    :param request: 
    :return: 
    """
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user_obj = UserProfile(
        name=name,
        email=email,
        password = password
    )
    user_obj.save()
    return render(request,'success.html')