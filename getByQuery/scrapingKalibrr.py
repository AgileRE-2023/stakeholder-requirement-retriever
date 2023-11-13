from bs4 import BeautifulSoup
import requests

def scrapingKalibrr(inputValue):
    url = "https://www.kalibrr.com/kjs/job_board/search?limit=50&offset=50&text="+inputValue
    job_descriptions = []  # Initialize a list to store job descriptions

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for job in data["jobs"]:
            qualifications = job.get("qualifications", "")
            description = job.get("description", "")

            # Remove HTML tags 
            qualifications_text = BeautifulSoup(qualifications, "html.parser").get_text()
            description_text = BeautifulSoup(description, "html.parser").get_text()

            # Combine text for each job listing and add to the list
            job_description = qualifications_text + description_text
            job_descriptions.append(job_description)

    else:
        print("Failed to retrieve data. Status code:", response.status_code)

    return job_descriptions