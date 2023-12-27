from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view.as_view()),
    path('authorized/', views.authorized.as_view()),
    path('login_successful', views.login_interface_view.as_view()),
]
