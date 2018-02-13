from django.urls import path

from . import views

urlpatterns = [
    path('aframe/<int:sceneid>', views.aframe, name="aframe")
]
