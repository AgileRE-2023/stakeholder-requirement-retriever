from django.http import HttpResponse
from django.shortcuts import render

def about(request): 
    return render(request, "about.html")

def faq(request): 
    return render(request, "faq.html")

def home(request): 
    return render(request, "home.html")

def output(request): 
    return render(request, "output.html")

def search(request): 
    return render(request, "search.html")