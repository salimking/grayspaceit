from django.http import Http404
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from .models import Mainuser
from posts.urls import *
import re

# from django.contrib.auth import authenticate,login,logout
# LOGIN VIEW ENDPOINT

def login(request):
    if request.method=="POST":
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        email=request.POST["email"]
        password=request.POST["password"]
        if (re.search(regex,email)):
            user=Mainuser.objects.filter(email=email,password=password).count()
            if user>0:
                
                
                return HttpResponse(" <h1> You are logged in </h1>")

            else:
                return HttpResponse("Your email and password not match")    
        else:
            return HttpResponse("Your email is not correct")        
    return render(request, 'login.html')


def register(request):
    if request.method=="POST":
        
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        password=request.POST["password"]
        c_password=request.POST["c_password"]
        email=request.POST["email"]
        error=None
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if not first_name:
            error="Enter first name"
        
        if not last_name:
            error="Enter last name"    
        if  not email  :
            error="Enter valid Email "
         
        context={
            'f':first_name,
            'l':last_name,
            'email':email,
            'password':password,
            'error':error,
            "massage":"Email already exist"
            
        }
        if not error:     
            if password==c_password:
                if Mainuser.objects.filter(email=email).exists():
                    return render(request,"register.html",context)
                else:
                    user=Mainuser(first_name=first_name,last_name=last_name,email=email,password=password)
                    user.save()
                    
                
                    return render(request, 'blog-listing.html',context) 

            else:

                return HttpResponse("Your Password not matched ")

        return render(request, 'register.html',context)    

    else:
        return render(request, 'register.html')