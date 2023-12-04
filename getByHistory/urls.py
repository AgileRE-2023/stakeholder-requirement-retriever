from django.contrib import admin
from django.urls import path,include
from stakeholder_requirement import views

from . import views

urlpatterns = [
    path('major', views.majorView, name="major"),
    path('major/find/', views.history_major_view, name='history_major'),
    path('getByHistory/', views.getByHistory, name='getByHistory'),
]  