from behave import *
from time import sleep

@given('Sign in: I navigate to sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()
    sleep(1)

@when('Sign in: I click on forgot password button')
def step_impl(context):
    context.sign_in_page.click_forgot_pass_link()

@when('Sign in: I click on sign up link')
def step_impl(context):
    context.sign_in_page.click_sign_up_link()


