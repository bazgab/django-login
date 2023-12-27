from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
# Create your views here.

class login_view(TemplateView):
    template_name = 'login/login.html'

class authorized(LoginRequiredMixin, TemplateView):
    template_name = 'login/authorized.html'
    login_url = '/admin'

class login_interface_view(LoginView):
    template_name = 'login/login.html'
    
    
