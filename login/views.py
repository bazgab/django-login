from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


class authorized(LoginRequiredMixin, TemplateView):
    template_name = 'login/authorized.html'
    login_url = '/admin'

class index_page(TemplateView):
    template_name = 'login/index.html'

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index/')
        else:
            return redirect('login_user')
    
    else:
        return render(request, 'login/login.html', {})   
