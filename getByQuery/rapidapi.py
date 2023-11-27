import requests

def getJobDescriptionJobWizRapidAPI(query):
    url = "https://job-search-api1.p.rapidapi.com/v1/job-description-search"


    headers = {
        "X-RapidAPI-Key": "997fb11043mshc85667bcbcecda7p12ecc8jsn9fadca695bff",
        "X-RapidAPI-Host": "job-search-api1.p.rapidapi.com"
    }
    job_descriptions = []
    for i in range(1,6):
        querystring = {"q":query,"page":str(i)}
        response = requests.get(url, headers=headers, params=querystring)
        if (response.status_code == 200):
            res = response.json()['jobs']
            for desc in res:
                job_descriptions.append(desc['plain_text_description'])

    return job_descriptions