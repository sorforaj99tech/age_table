from django.shortcuts import render, HttpResponse, redirect
from . models import Signup

# Create your views here.

def home(request):
    if request.method == "POST":
        
    username = request.POST.get()
    subject = request.POST.get()
    age = request.POST.get()
    data = from(username=name, subject=sunject, age=age)
    data.save()
    
    return redirect()