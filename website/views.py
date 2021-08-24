from django.shortcuts import render,redirect
# from django.contrib.auth.models import User,auth
from.models import *
from django.http import HttpResponse

# Create your views here.
def about(request):
       return render(request,'about.html')
def scholarship(request):
       return render(request,'scholarship.html')


