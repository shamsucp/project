from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid login ")
    return render(request, 'app1/login.html')

@login_required
def dashboard_view(request):
    return HttpResponse("Welcome to your dashboard!")

def logout_view(request):
    logout(request)
    return redirect('login')