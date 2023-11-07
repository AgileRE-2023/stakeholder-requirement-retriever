from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, "home.html")

def major(request): 
    return render(request, "major.html")