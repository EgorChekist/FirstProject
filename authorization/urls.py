from django.urls import path
from .views import login, login_handle

urlpatterns = [
    path("login/", login),
    path("login/handle/", login_handle)
]