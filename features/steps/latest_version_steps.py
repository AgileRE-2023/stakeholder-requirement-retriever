from behave import when, then
from selenium.webdriver.common.by import By
import time

@given('the user is on the major list page')
def step_given(context):
    context.browser.get('http://127.0.0.1:8000/history/major') 

@when('the user clicks "{major}"')
def step_when_click_major(context, major):
    print(major)
    major_button = context.browser.find_element(By.XPATH, f'//li[contains(text(), "{major}")]')
    major_button.click()

@when('the user clicks on the "see new version" button')
def step_when_click_latest_version(context):
    latest_version_button = context.browser.find_element(By.ID, "new_version_button")
    latest_version_button.click()
    time.sleep(2)

@then('the user should see the latest stakeholder requirements in the output page')
def step_then_latest_requirements(context):
    last_updated_element = context.browser.find_element(By.CLASS_NAME, "last_up")
    last_updated_text = last_updated_element.text.split("Last Updated ")[1]

    latest_requirements_info = context.browser.find_element(By.ID, "output_req").text
    assert last_updated_text in latest_requirements_info, "Latest requirements not found on the page"