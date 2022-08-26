from django.urls import path
from django.views.generic.base import TemplateView
from photo.views import photos, contact_form

urlpatterns = [
    path("", photos),
    path("contact_form/", contact_form),
]