from django.urls import path
from . import views

urlpatterns = [
    path('authorized/', views.authorized.as_view()),
    path('index/', views.index_page.as_view()),
    path('login_user', views.login_user, name='login_user')
]
