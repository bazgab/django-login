from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class logout_view(TemplateView):
    template_name = 'logout/logout.html'