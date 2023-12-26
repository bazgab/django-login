from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class login_view(TemplateView):
    template_name = 'login/login.html'

class authorized(LoginRequiredMixin, TemplateView):
    template_name = 'login/authroized.html'
    login_url = '/admin'


