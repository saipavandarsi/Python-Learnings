from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from django.core.mail import send_mail

from .models import UserProfile

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
    #send_email()
    return render(request,'success.html')

@csrf_exempt    
def homepage(request):
    """ """
    email = request.POST.get('email')
    password = request.POST.get('password')
    print email
    print password
    user_record = UserProfile.objects.filter(email=email, password=password)
    if user_record:
        return render(request,'homepage.html', {'username': email})
    return render(request,'error.html')

def send_email(request):
    """ """
    send_mail('Welcome to Hubree', 'Welcome to Hubree, Real estate app, Plick below link to activate',
              'hubreeh@gmail.com',
             ['mail.ramachandra.raju@gmail.com'], fail_silently=False)
    return render(request,'success.html')
