from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, "home.html")

def output(request): 
    return render(request, "output.html")

def search(request): 
    return render(request, "search.html")