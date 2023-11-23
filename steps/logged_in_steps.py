from behave import *
from time import sleep


@when('Sign in: I write my email')
def step_impl(context):
    context.sign_in_page.set_email('p.iuuliana@gmail.com')
    sleep(1)

@when('Sign in: I write my password')
def step_impl(context):
    context.sign_in_page.set_pswd('Password1.')
    context.sign_in_page.click_login_button()
    sleep(5)

@then('Search all: I am a user on search page')
def step_impl(context):
    context.menu_page.verify_correct_page()
    sleep(1)