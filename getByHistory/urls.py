from django.contrib import admin
from django.urls import path,include
from stakeholder_requirement import views

urlpatterns = [
    path('major', views.major),
]  