from urllib.parse import urlparse
from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from dateutil import parser

@given(u'I am on "{search_page_path}"')
def step_given(context,search_page_path):
    context.browser.get(f"http://localhost:8000{search_page_path}") 

@when(u'I fill in "{major}" for "{id}"')
def step_when(context,major, id):
    major_input = context.browser.find_element("id",id)  
    major_input.send_keys(major)

@when(u'I press enter')
def step_when(context):
    major_input = context.browser.find_element("id", "input-box")
    major_input.send_keys(Keys.ENTER)
    
@then(u'I should be on "{page}" with the url should match "{output_page_path}"')
def step_when(context,page, output_page_path):
    current_url = context.browser.current_url
    current_path = urlparse(current_url).path
    assert output_page_path == current_path, f"Failed to redirect to output page with path of '{output_page_path}'"

@then(u'I should see "{major}" in the "{div_id}" element')
def step_then(context, major,div_id):
    output_text = context.browser.find_element("id",div_id).text
    assert major in output_text, f"Stakeholder requirements for '{major}' not found in the output"

@then(u'I should see "{error_message}" as an error in the "{div_id_error_popup}" element')
def step_then_error_popup(context, error_message,div_id_error_popup):
    popup_error_text = context.browser.find_element("id", div_id_error_popup).text
    assert error_message in popup_error_text, f"Expected error message not found in the popup, expected : '{error_message}', got : '{popup_error_text}'"


@when(u'I select "{major}"')
def step_impl(context, major):
    major_to_click = context.browser.find_element(By.XPATH, f'//li[contains(text(), "{major}")]')
    major_to_click.click()


#
@when(u'I see "last updated date"')
def step_when_sees_date(context):
    last_updated_text = context.browser.find_element(By.CLASS_NAME, "last_up").text
    last_updated_datetime = parser.parse(last_updated_text, fuzzy=True)
    context.last_updated_timestamp = time.mktime(last_updated_datetime.timetuple())

@when(u'I press "see new version"')
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
    last_updated_text = context.browser.find_element(By.CLASS_NAME, "last_up").text
    last_updated_datetime = parser.parse(last_updated_text, fuzzy=True)
    return time.mktime(last_updated_datetime.timetuple())


@then(u'I should see "the latest stakeholder requirements" in the output page')
def step_then_latest_requirements(context):
    last_updated_text = context.browser.find_element(By.CLASS_NAME, "last_up").text

    # Parse to a timestamp using dateutil.parser.parse
    last_updated_datetime = parser.parse(last_updated_text, fuzzy=True)
    new_timestamp = time.mktime(last_updated_datetime.timetuple())

    # Compare the new timestamp with the stored timestamp
    assert new_timestamp > context.last_updated_timestamp, "New timestamp is not newer than the stored timestamp, the requirements are not updated!"

@then(u'the current date of requirement terms is newer than the previous one')
def step_then_newer_date(context):
    new_timestamp = get_current_timestamp(context)
    assert new_timestamp > context.last_updated_timestamp, "New timestamp is not newer than the stored timestamp, requirements are not updated!"