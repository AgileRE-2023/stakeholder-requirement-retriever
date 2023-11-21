from django.http import HttpResponse
from django.shortcuts import render
from .preprocess import preprocess_data
from .scrapingKalibrr import scrapingKalibrr
from .mainprocess import mainProcess
from .validateInput import validateInput
from getByQuery.models import Prodi
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
        input_value = request.POST.get('getByQuery')
        clean_input = validateInput(input_value)
        jobDescription = scrapingKalibrr(clean_input)
        preprocessed_one_sentence,preprocessed_separate_docs,preprocessed_separate_docs_tokenized = preprocess_data(jobDescription)
        top_terms_list = mainProcess(preprocessed_one_sentence,preprocessed_separate_docs,preprocessed_separate_docs_tokenized)
        context  = {'top_terms_list': top_terms_list,'query':input_value}
        return render(request,'output.html', context)
        # return HttpResponse(f'your input value: {result}')
    else:
        return HttpResponse("nowhere to go!!!")

def majorView(request):
    major = Prodi.objects.all()
    context = {
        'major':major
    }
    return render(request, 'major.html', context)
