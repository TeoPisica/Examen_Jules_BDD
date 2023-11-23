from behave import *
from time import sleep

@when('Add person page: I set first name "{name}"')
def step_impl(context, name):
    context.add_person_page.set_first_name(name)
    sleep(1)

@when('Add person page: I set last name "{name}"')
def step_impl(context,name):
    context.add_person_page.set_last_name(name)
    sleep(1)

@when('Add person page: I click save')
def step_impl(context):
    context.add_person_page.click_save_button()

@when('Add person page: I verify success message')
def step_impl(context):
    context.add_person_page.verify_success_message()
    sleep(1)

@then('Add person page: I click finish button')
def step_impl(context):
    context.add_person_page.click_finish_button()




