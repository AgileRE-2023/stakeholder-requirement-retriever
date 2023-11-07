from django.contrib import admin
from django.urls import path,include
from stakeholder_requirement import views

from . import views

urlpatterns = [
    path('',views.home),
    path('search', views.search),
    path('output', views.output),
]  