from django.urls import path
from . import views

urlpatterns = [
    path("", views.wordle_home, name="wordle_home"),
]