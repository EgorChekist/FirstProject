from django.urls import path
from django.views.generic.base import TemplateView
from photo.views import photos

urlpatterns = [
    path("", photos)
]