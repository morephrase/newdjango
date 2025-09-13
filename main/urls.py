from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import signup_view

urlpatterns = [
    # Home and general pages
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('contact/', views.contactpage, name='contactpage'),
    path('projects/', views.allprojects, name='allprojects'),
    path('add/', views.addpage, name='addpage'),  # only for superusers

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='userlogin'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='userlogout'),
    path('signup/', views.usersignup, name='usersignup'),
]
