from behave import *
from selenium.webdriver.common.by import By

@given(u'I am on the Major List Page')
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/history/major")
    assert(context.browser.find_element(By.CSS_SELECTOR, '.contents .contain .part2 h1 span').text) == "Major"

@when(u'I click a "{major}" from the provided list')
def step_impl(context, major):
    major_to_click = context.browser.find_element(By.XPATH, f'//li[contains(text(), "{major}")]')
    major_to_click.click()

@then(u'I see a display of skills that are relevant to the "{major}" major')
def step_impl(context, major):
    assert context.browser.title == "output"

    major_name_output = context.browser.find_element(By.CSS_SELECTOR, '#major_name_output').text
    assert major in major_name_output, f"Expected '{major}' but got '{major_name_output}'"

    requirement_tabs = context.browser.find_elements(By.CSS_SELECTOR, '.output .tab_o')
    assert len(requirement_tabs) > 0, "Expected at least one requirement tab but found none"

@then(u'I should see an error popup with the message "{error_message}"')
def step_impl(context, error_message):
    error_modal = context.browser.find_element(By.CLASS_NAME, 'swal2-popup')

    assert error_modal.is_displayed(), "Error modal is not displayed"

    error_message_element = error_modal.find_element(By.CLASS_NAME, 'swal2-html-container')
    assert error_message in error_message_element.text, f"Expected '{error_message}' but got '{error_message_element.text}'"
    

   
