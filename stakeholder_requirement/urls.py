"""
URL configuration for stakeholder_requirement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from stakeholder_requirement import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about,name='about'),
    path('faq', views.faq,name='faq'),
    path('output/', views.output, name='output'),
    path('', include("getByQuery.urls")),
    path('query/',include("getByQuery.urls")),
    path('history/',include("getByHistory.urls"),name='history_major')
]