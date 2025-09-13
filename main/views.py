# main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignUpForm

# ---------------------------
# General Pages
# ---------------------------
def homepage(request):
    return render(request, 'main/home.html')

def aboutpage(request):
    return render(request, 'main/about.html')

def contactpage(request):
    return render(request, 'main/contact.html')

def projects_page(request):
    return render(request, 'main/projects.html')

def allprojects(request):
    return render(request, 'main/projects.html')


# ---------------------------
# User Authentication
# ---------------------------
def user_login(request):
    """Custom login view (if not using built-in LoginView)"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid credentials'})
    return render(request, 'main/login.html')


def userlogout(request):
    """Logout view"""
    logout(request)
    return redirect('homepage')


def usersignup(request):
    """User registration/signup view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('userlogin')  # redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})


# ---------------------------
# Optional: Superuser-only Page
# ---------------------------
@user_passes_test(lambda u: u.is_superuser)
def addpage(request):
    """Page accessible only to superusers"""
    return render(request, 'main/add.html')


# ---------------------------
# Using Django's built-in LoginView
# ---------------------------
def userlogin(request):
    """Optional: use built-in LoginView"""
    return auth_views.LoginView.as_view(template_name='main/login.html')(request)
def contactpage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # handle saving or sending the message
        messages.success(request, "Your message has been sent!")
    return render(request, "main/contact.html")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately after signup
            return redirect('home')  # change 'home' to your homepage URL name
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})
