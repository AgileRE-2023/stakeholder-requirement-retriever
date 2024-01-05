from urllib.parse import urlparse
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@given(u'I am on "{search_page_path}"')
def step_given(context,search_page_path):
    context.browser.get(f"http://localhost:8000{search_page_path}") 

@when(u'I fill in "{major}" for "{id}"')
def step_when(context,major, id):
    major_input = context.browser.find_element("id",id)  
    major_input.send_keys(major)

@when(u'I press "{keys}"')
def step_when(context,keys):
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