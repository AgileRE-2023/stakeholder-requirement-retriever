from django.http import HttpResponse
from django.shortcuts import render
from .preprocess import preprocess_data
from .scrapingKalibrr import scrapingKalibrr
from .mainprocess import mainProcess
# Create your views here.
def home(request): 
    return render(request, "home.html")


def search(request): 
    return render(request, "search.html")


def getByQuery(request):
    if request.method == 'POST':
        input_value = request.POST.get('getByQuery')
        jobDescription = scrapingKalibrr(input_value)
        preprocessed_data,lemmatized_words = preprocess_data(jobDescription)
        result = mainProcess(preprocessed_data,lemmatized_words)
        return HttpResponse(f'your input value: {result}')
    else:
        return render(request, 'your_template.html')