from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): 
    return render(request, "home.html")

def major(request): 
    return render(request, "major.html")

def history_major_view(request):
    search_query = request.GET.get('q', '')
    return HttpResponse(search_query)