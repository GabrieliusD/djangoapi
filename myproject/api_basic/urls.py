from django.urls import path
from . import views

urlpattern = [
    path('playground/hello', views.say_hello)
]