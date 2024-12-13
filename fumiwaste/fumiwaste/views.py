from django.http import HttpResponse
from django.shortcuts import render


def home(req):
   return render(req, 'Home.html')
   # return HttpResponse("home")


def about(req):
   return render(req, 'About.html')
   # return HttpResponse("about")

