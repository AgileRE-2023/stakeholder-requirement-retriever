from django.http import HttpResponse
from django.shortcuts import render

def about(request): 
    return render(request, "about.html")

def faq(request): 
    return render(request, "faq.html")

def major(request): 
    return render(request, "major.html")

def output(request): 
    return render(request, "output.html")
