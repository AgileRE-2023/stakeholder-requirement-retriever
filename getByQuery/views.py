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
        preprocessed_one_sentence,preprocessed_separate_docs,preprocessed_separate_docs_tokenized = preprocess_data(jobDescription)
        top_terms_list = mainProcess(preprocessed_one_sentence,preprocessed_separate_docs,preprocessed_separate_docs_tokenized)
        context  = {'top_terms_list': top_terms_list,'query':input_value}
        return render(request,'output.html', context)
        # return HttpResponse(f'your input value: {result}')
    else:
        return HttpResponse("nowhere to go!!!")