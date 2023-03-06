from django.contrib import admin
from django.urls import path , include
from Soil_Predictor.views import *

urlpatterns = [
    path("",index),
    path("about",about),
    path("prediction",prediction)
]
