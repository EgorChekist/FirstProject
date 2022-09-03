from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request, "login.html")

def login_handle(request):
    print(request.POST)
    return redirect("/auth/login/")

def registration(request):
    return render(request, "registration.html")