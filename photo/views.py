from django.shortcuts import render
import random

# Create your views here.
def photos(request):
    data = {}
    data["secret"] = random.randint(1, 100)
    data["locations"] = ["поле", "лес", "речка", "дамбу", "деревня", "огород"]
    return render(request, "photos.html", data)