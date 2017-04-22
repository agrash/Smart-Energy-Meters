from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def home(request):
    return render (request, "home.html")

def Bharti(request):
    return render (request, "Bharti.html")

def SIT(request):
    return render (request, "SIT.html")

def Block4(request):
    return render (request, "Block4.html")

def Block6(request):
    return render (request, "Block6.html")

def Girnar(request):
    return render (request, "Girnar.html")

def Udaigiri(request):
    return render (request, "Udaigiri.html")

def Overview(request):
	return render (request, "Overview.html")