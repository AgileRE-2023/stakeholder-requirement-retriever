from urllib.parse import urlparse
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given(u'the user is on the search page with path of "{search_page_path}"')
def step_given(context,search_page_path):
    context.browser.get(f"http://localhost:8000{search_page_path}") 

@when(u'the user type "{major}" as a value for input tag with id of "{id}"')
def step_when(context,major, id):
    major_input = context.browser.find_element("id",id)  
    major_input.send_keys(major)

@when(u'the user press enter to submit the form that have the input tag with id of "{id}"')
def step_when(context, id):
    major_input = context.browser.find_element("id", id)
    major_input.send_keys(Keys.ENTER)

@then(u'the user should be on the output page with the path of "{output_page_path}"')
def step_when(context, output_page_path):
    current_url = context.browser.current_url
    current_path = urlparse(current_url).path
    assert output_page_path == current_path, f"Failed to redirect to output page with path of '{output_page_path}'"

@then(u'the user should see stakeholder requirements of "{major}" in the div with id of "{div_id}"')
def step_then(context, major,div_id):
    output_text = context.browser.find_element("id",div_id).text
    assert major in output_text, f"Stakeholder requirements for '{major}' not found in the output"

@then(u'the user should see an error popup with the message "{error_message}" in the div with id of "{div_id_error_popup}"')
def step_then_error_popup(context, error_message,div_id_error_popup):
    popup_error_text = context.browser.find_element("id", div_id_error_popup).text
    assert error_message in popup_error_text, f"Expected error message not found in the popup, expected : '{error_message}', got : '{popup_error_text}'"