from django.http import HttpResponse
from django.shortcuts import render
from .preprocess import preprocess_data
from .scrapingKalibrr import scrapingKalibrr
from .mainprocess import mainProcess
from .validateInput import validateInput
from .validateTerms import validateTerms
from getByQuery.models import Scraping
from getByHistory.models import History
from datetime import datetime, timedelta
from getByQuery.models import Prodi
import json
# Create your views here.
def home(request): 
    return render(request, "home.html")


def search(request):
    major = Prodi.objects.all()
    majorAH = Prodi.objects.filter(subject=0)
    majorET = Prodi.objects.filter(subject=1)
    majorLSM = Prodi.objects.filter(subject=2)
    majorNS = Prodi.objects.filter(subject=3)
    majorSSM = Prodi.objects.filter(subject=4)
    major_values = [prodi.nama_prodi for prodi in major]
    context = {
        'major':major_values,
        'majorAH':majorAH,
        'majorET':majorET,
        'majorLSM':majorLSM,
        'majorNS':majorNS,
        'majorSSM':majorSSM,
    }
    return render(request, "search.html",context)


def getByQuery(request):
    if request.method == 'POST':
        # Get the request body to get user input
        input_value = request.POST.get('getByQuery')
        try:
            clean_input, prodi_instance = validateInput(input_value)
        except:
            return HttpResponse("Input is not on the major list!", status=404)
        
        # Get data from kalibrr
        jobDescription = scrapingKalibrr(clean_input)

        # Preprocess data
        preprocessed_one_sentence,preprocessed_separate_docs,preprocessed_separate_docs_tokenized = preprocess_data(jobDescription)

        dateNow = datetime.now()
        # Add 60 days
        expired_date = dateNow + timedelta(days=60)
        # saving preprocessed scraping result to db
        try:
            # json.dumps() to convert to JSON-formatted string 
            # json.loads() to make it back to the original array later
            converted_preprocessed_data = json.dumps(preprocessed_separate_docs)
            # Save the serialized array into the Scraping model
            scraping_instance = Scraping(teks=converted_preprocessed_data,tgl_scrap=dateNow,id_prodi=prodi_instance)
            scraping_instance.save()
        except:
            return HttpResponse("Something went wrong while saving scraping result!", status=500)

        top_terms_list = mainProcess(preprocessed_one_sentence,preprocessed_separate_docs,preprocessed_separate_docs_tokenized)

        validatedTermsAndDescription = validateTerms(top_terms_list)

        # saving terms extraction to db
        try:
            converted_terms_data = json.dumps(validatedTermsAndDescription)
            # Save the serialized array into the Scraping model
            history_instance = History(date_generated=dateNow, exp_date=expired_date, requirements=converted_terms_data, id_prodi=prodi_instance)
            history_instance.save()
        except:
            return HttpResponse("Something went wrong while saving scraping result!", status=500)
        
        context  = {'terms_with_description': validatedTermsAndDescription,'query':input_value}
        return render(request,'output.html', context)
    else:
        return HttpResponse("nowhere to go!!!")


def majorView(request):
    major = Prodi.objects.all()
    context = {
        'major':major
    }
    return render(request, 'major.html', context)
