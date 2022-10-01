from django.urls import path
from .views import login_view, login_handle
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", login_view),
    path("login/handle/", login_handle),
    path("logout/", LogoutView.as_view()),
]