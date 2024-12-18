from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(req):
    form = UserCreationForm()
    return render(req, 'accounts/signup.html',{'userform': form})