from django.shortcuts import render
from django.http import HttpResponse
from getByQuery.validateInput import validateInput
from django.shortcuts import get_object_or_404
from getByHistory.models import History
import json

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

def getByHistory(request):
    if request.method == 'POST':
        input_value = request.POST.get('getByHistory')
        try:
            clean_input, prodi_instance = validateInput(input_value)
        except:
            # return HttpResponse("Input is not on the major list!", status=404)
            error_message = "Your input is not on the list of majors. Please input a valid major."
            return render(request, 'search.html', {'error_message': error_message})

        # Get the latest History record for the specified id_prodi
        latest_history = History.objects.filter(id_prodi=prodi_instance.id_prodi).order_by('-date_generated').first()

        if latest_history is not None:
            try:
                requirements_data = json.loads(latest_history.requirements)
                date_generated = latest_history.date_generated
                context = {
                    'terms_with_description': requirements_data,
                    'query': prodi_instance.nama_prodi,
                    'id_prodi': prodi_instance.id_prodi,
                    'date_generated':date_generated,
                }
                return render(request, 'output.html', context)
            except json.JSONDecodeError as e:
                # Handle JSONDecodeError, print details for debugging
                print(f"JSONDecodeError: {e}")
                return HttpResponse("Error decoding JSON data", status=500)
        else:
            # Handle the case where no History instance is found for the specified id_prodi
            # return HttpResponse("No history found for the specified id_prodi", status=404)
            error_message = "No history found for the specified major. Please input the major in the search field."
            return render(request, 'search.html', {'error_message': error_message})