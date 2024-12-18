from django.shortcuts import render

# Create your views here.

def signup_view(req):
    return render(req, 'accounts/signup.html')