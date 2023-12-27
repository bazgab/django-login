from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

@login_required(login_url='login_user')
def index_page(request):
    return render(request, 'login/index.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index/')
        else:
            messages.success(request, ("Invalid Username and/or password. Please try again."))
            return redirect('login_user')
            
    
    else:
        return render(request, 'login/login.html', {})   

def logout_user(request):
    logout(request)
    messages.success(request, ("You have logged out."))
    return redirect('login_user')

def register_user(request):
    return render(request, 'login/register.html', {})