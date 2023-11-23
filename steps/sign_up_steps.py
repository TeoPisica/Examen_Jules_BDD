from behave import *
from time import sleep

@when('Sign up: I select personal option')
def step_impl(context):
    context.sign_up_page.click_personal_option()
    context.sign_up_page.click_continue_button()
    sleep(1)

@when('Sign up: I complete first and last name inputs')
def step_impl(context):
    context.sign_up_page.complete_input('Teo')
    context.sign_up_page.click_continue_button()
    context.sign_up_page.complete_input('Pisica')
    context.sign_up_page.click_continue_button()
    sleep(1)

@when('Sign up: I complete email input "{email}"')
def step_impl(context, email):
    context.sign_up_page.complete_input(email)
    context.sign_up_page.press_enter()

@then('Sign up: I validate error message is as expected "{message}"')
def step_impl(context, message):
    sleep(3)
    context.sign_up_page.validate_email_error(message)
