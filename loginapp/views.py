from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as dj_login,logout


def index(request):
    return render(request,"index.html")


def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if username and email and fname and lname and password and cpassword:
            if password == cpassword:
                user=User.objects.create_user(username,email,password)
                user.first_name=fname
                user.last_name=lname
                user.save()
                if user:
                    messages.success(request,"user account created")
                    return redirect("/login/")
                else:
                    messages.success(request,"user account not created")

            else:
                    messages.success(request,"password not mached")
                    return redirect("/signup/")

    return  render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username and password:
            user=authenticate(username=username,password=password)
            if user is not None:
                dj_login(request,user)
                fname=user.first_name
                return render(request,"index.html",{'fname':fname})
        
    return render(request,'login.html')
# Create your views here.

def logoutfu(request):
    logout(request)
    return redirect("signup")

