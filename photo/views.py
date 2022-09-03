from django.shortcuts import render, redirect
from .models import Photo, Contact
import random

# Create your views here.
def photos(request):
    data = {}
    # data["secret"] = random.randint(1, 100)
    # data["locations"] = ["поле", "лес", "речка", "дамбу", "деревня", "огород"]
    data["photos"] = Photo.objects.all()
    return render(request, "photos.html", data)


def contact_form(request):
    print("Кто-то посетил эту страницу")
    name = request.GET.get("name")
    email = request.GET.get("email")
    message = request.GET.get("message")

    # Contact.objects.create(name=name, email=email, message=message)
    Contact(name=name, email=email, message=message).save()

    return redirect("/")