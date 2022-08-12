from django.shortcuts import render
from .models import Photo
import random

# Create your views here.
def photos(request):
    data = {}
    # data["secret"] = random.randint(1, 100)
    # data["locations"] = ["поле", "лес", "речка", "дамбу", "деревня", "огород"]
    data["photos"] = Photo.objects.all()
    return render(request, "photos.html", data)