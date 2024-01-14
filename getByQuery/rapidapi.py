import os
import requests

def jobWizRapidAPI(query):
    url = "https://job-search-api1.p.rapidapi.com/v1/job-description-search"


    headers = {
        "X-RapidAPI-Key": os.environ.get('JOBWIZ_RAPIDAPI_JOBSCRAPER'),
        "X-RapidAPI-Host": "job-search-api1.p.rapidapi.com"
    }
    job_descriptions = []
    for i in range(1,4):
        querystring = {"q":query,"page":str(i)}
        response = requests.get(url, headers=headers, params=querystring)
        if (response.status_code == 200):
            res = response.json()['jobs']
            for desc in res:
                job_descriptions.append(desc['plain_text_description'])

    return job_descriptions