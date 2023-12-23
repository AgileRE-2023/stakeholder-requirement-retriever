from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('the user is on the search page')
def step_given(context):
    context.browser.get('http://localhost:8000/search') 

@when('the user submits the form with "{major}" as an input value')
def step_when(context, major):
    major_input = context.browser.find_element("id","input-box")  
    major_input.send_keys(major)
    major_input.send_keys(Keys.ENTER)

@then('the user should see stakeholder requirements of "{major}" in the output page')
def step_then(context, major):
    output_text = context.browser.find_element("id","major_name_output").text
    assert major in output_text, f"Stakeholder requirements for '{major}' not found in the output"

@then('the user should see an error popup with the message "{error_message}"')
def step_then_error_popup(context, error_message):
    popup_text = context.browser.find_element("id", "swal2-html-container").text
    assert error_message in popup_text, f"Expected error message not found in the popup"