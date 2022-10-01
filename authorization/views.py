from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "login.html")

def login_handle(request):
    data = {}
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    else:
        data["error"] = "Пользователь не найден"
        return render(request, "login.html", data)

    return redirect("/auth/login/")

def registration(request):
    return render(request, "registration.html")