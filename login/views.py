from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
# Create your views here.


@csrf_protect
def login_view(request):
	username = request.POST.get("username")
	password = request.POST.get("password")
	user = authenticate(request , username=username , password=password)
	if user is not None:
		login(request , user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request , "login/login.html" , {"message":"invalid credentials"})

def logout_view(request):
	logout(request)
	return render(request , "login/login.html" , {"message" : "Logout Successfully"})

def register(request):
	return render(request , "login/register.html")

def registered(request):
	username = request.POST.get("usernam")
	email = request.POST.get("emai")
	password = request.POST.get("passwor")
	user = User.objects.create_user(f"{username}" , f"{email}" , f"{password}")
	user.save()
	return render(request , "login/login.html")



