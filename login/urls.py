from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view.as_view()),
    path('authorized/', views.authorized.as_view()),
    path('index/', views.index_page.as_view()),
]
