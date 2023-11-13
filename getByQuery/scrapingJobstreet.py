import requests
from bs4 import BeautifulSoup


# Scraping Jobstreet

url = 'https://www.jobstreet.co.id/id/information-systems-jobs'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# Find all div elements with class 'job'
job_divs = soup.find_all('a', class_='jdlu992')
job_urls = []
# Extract the 'data-job-id' attribute from each div
for job_div in job_divs:
    job_urls.append('https://www.jobstreet.co.id'+job_div.get('href'))
print(job_urls)
print(len(job_urls))

responses_html  = []
limit = 120
counter = 0
for url in job_urls:
    if counter < limit:
        response = requests.get(url)
        responses_html.append(BeautifulSoup(response.text, 'html.parser'))
        counter += 1
    else:
        break
# print(responses_html)
# Find all div elements with class 'description__text'
description_divs_of_responses = []

for response_html in responses_html:
    
    description_divs_of_responses.append(response_html.find_all('div', class_='z1s6m00 _1hbhsw66y _1hbhsw673 _1hbhsw674'))
# print(description_divs_of_responses)
# Extract the inner text of each div
inner_text = []
for description_divs_of_response in description_divs_of_responses:
    for div in description_divs_of_response:
        inner_text.append(div.get_text(strip=True))
print(inner_text)