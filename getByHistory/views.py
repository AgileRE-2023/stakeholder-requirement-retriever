from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): 
    return render(request, "home.html")

def major(request): 
    return render(request, "major.html")

def history_major_view(request):
    search_query = request.GET.get('q', '').replace(" ","+").lower()
    return HttpResponse(search_query)

from getByQuery.models import Prodi

def majorView(request):
    major = Prodi.objects.all()
    majorAH = Prodi.objects.filter(subject=0)
    majorET = Prodi.objects.filter(subject=1)
    majorLSM = Prodi.objects.filter(subject=2)
    majorNS = Prodi.objects.filter(subject=3)
    majorSSM = Prodi.objects.filter(subject=4)
    context = {
        'major':major,
        'majorAH':majorAH,
        'majorET':majorET,
        'majorLSM':majorLSM,
        'majorNS':majorNS,
        'majorSSM':majorSSM,

    }
    return render(request, 'major.html', context)