from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home page - Welcome to StudyBud!")

def room(request):
    return HttpResponse("Room page - This is a study room!")