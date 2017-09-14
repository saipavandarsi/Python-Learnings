from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from model import UserProfile

def signup(request):
    """ """
    return render(request,'register.html')

@csrf_exempt
def create_user(request):
    """ """
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user_obj = UserProfile(
        name = name,
        email = email,
        password = password)
    user_obj.save()
    return render(request,'success.html')