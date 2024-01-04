from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dateutil import parser

@given('the user is on the major list page')
def step_given(context):
    context.browser.get('http://127.0.0.1:8000/history/major') 

@when('the user clicks "{major}"')
def step_when_click_major(context, major):
    print(major)
    major_button = context.browser.find_element(By.XPATH, f'//li[contains(text(), "{major}")]')
    major_button.click()

@when('the user sees the last updated date')
def step_when_sees_date(context):
    last_updated_text = context.browser.find_element(By.CLASS_NAME, "last_up").text
    # Parse the string to a datetime object using dateutil.parser.parse
    last_updated_datetime = parser.parse(last_updated_text, fuzzy=True)
    # Convert the datetime object to a timestamp
    timestamp = time.mktime(last_updated_datetime.timetuple())
    # Store the timestamp in the context for later use
    context.last_updated_timestamp = timestamp

@when('the user clicks on the "see new version" button')
def step_when_click_latest_version(context):
    # Get the initial timestamp before submitting the form
    initial_timestamp = get_current_timestamp(context)

    # Find the form element and submit it
    search_form = context.browser.find_element(By.ID, "search-form")
    search_form.submit()

    # Wait for the timestamp to change
    WebDriverWait(context.browser, timeout=240).until(
        lambda browser: get_current_timestamp(context) > initial_timestamp
    )

def get_current_timestamp(context):
    # Extract and parse the timestamp from the page
    last_updated_text = context.browser.find_element(By.CLASS_NAME, "last_up").text
    last_updated_datetime = parser.parse(last_updated_text, fuzzy=True)
    return time.mktime(last_updated_datetime.timetuple())

@then('the user should see the latest stakeholder requirements in the output page by knowing that current date of requirement terms is newer than the previous one')
def step_then_latest_requirements(context):
    last_updated_text = context.browser.find_element(By.CLASS_NAME, "last_up").text

    # Parse to a timestamp using dateutil.parser.parse
    last_updated_datetime = parser.parse(last_updated_text, fuzzy=True)
    new_timestamp = time.mktime(last_updated_datetime.timetuple())

    # Compare the new timestamp with the stored timestamp
    assert new_timestamp > context.last_updated_timestamp, "New timestamp is not newer than the stored timestamp, the requirements are not updated!"
