from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    return render(request, "login.html")

def login_handle(request):
    data = {}
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    user = User.objects.filter(username=username)
    if user.exists():
        print("Пользователь найден")
    else:
        data["error"] = "Пользователь не найден"
        return render(request, "login.html", data)

    return redirect("/auth/login/")

def registration(request):
    return render(request, "registration.html")