from behave import *
from time import sleep

@when('Forgot pass: I write my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.set_email(email)
    sleep(1)

@then('Forgot pass: I validate that send email button is NOT enabled')
def step_impl(context):
    context.forgot_password_page.validate_send_email_button_is_disabled()
    sleep(3)

@then('Forgot pass: I validate that send email button is enabled')
def step_impl(context):
    context.forgot_password_page.validate_send_email_button_is_enabled()
    sleep(3)