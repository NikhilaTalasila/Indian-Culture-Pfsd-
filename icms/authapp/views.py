# authapp/views.py
from django.contrib.auth import login,logout, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def welcome(request):
    return render(request, 'authapp/welcome.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('nav_buttons')
    else:
        form = AuthenticationForm()
    return render(request, 'authapp/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('nav_buttons')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authapp/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('welcome')

def nav_buttons(request):
    return render(request, 'authapp/nav_buttons.html')

#def index(request):
  #  return render(request, 'authapp/index.html')
