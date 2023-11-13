import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/jobs/search?keywords=information%2Bsystems&location=Indonesia&geoId=102478259&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# Find all div elements with class 'job'
job_divs = soup.find_all('a', class_='base-card__full-link')
job_urls = []
# Extract the 'data-job-id' attribute from each div
for job_div in job_divs:
    job_urls.append(job_div.get('href'))
print(job_urls)
print(len(job_urls))

responses_html  = []
limit = 5
counter = 0
for url in job_urls:
    if counter < limit:
        response = requests.get(url)
        responses_html.append(BeautifulSoup(response.text, 'html.parser'))
        # print(responses_html)
        counter += 1
    else:
        break

# Find all div elements with class 'description__text'
description_divs_of_responses = []
for response_html in responses_html:
    description_divs_of_responses.append(response_html.find_all('div', class_='description__text'))

# Extract the inner text of each div
inner_text = []
for description_divs_of_response in description_divs_of_responses:
    for div in description_divs_of_response:
        inner_text.append(div.get_text(strip=True))
print(inner_text)