from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def signup_view(req):
 
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(req, 'accounts/signup.html',{'userform': form})

def login_view(req):
    if req.method == 'POST':
        form = AuthenticationForm(data = req.POST)
        if form.is_valid():
         return redirect('articles:list')
    else:
       form = AuthenticationForm()
    return render(req,'accounts/login.html',{'form': form})