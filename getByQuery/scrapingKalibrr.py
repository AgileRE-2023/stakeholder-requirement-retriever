from bs4 import BeautifulSoup
import requests

def scrapingKalibrr(inputValue):
    url = "https://www.kalibrr.com/_next/data/RHBx-W8Ym0gWx0tw46C5b/en/home/te/"+inputValue.replace(" ","-")+".json?param=te&param="+inputValue.replace(" ","-")
    job_descriptions = []  # Initialize a list to store job descriptions

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for job in data["pageProps"]["jobs"]:
            qualifications = job["qualifications"]
            description = job["description"]

            # Remove HTML tags 
            qualifications_text = BeautifulSoup(qualifications, "html.parser").get_text()
            description_text = BeautifulSoup(description, "html.parser").get_text()

            # Combine text for each job listing and add to the list
            job_description = qualifications_text + description_text
            job_descriptions.append(job_description)

    else:
        print("Failed to retrieve data. Status code:", response.status_code)

    return job_descriptions