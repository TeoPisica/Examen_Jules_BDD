from behave import *
from time import sleep


@when('Add property page: I set property name "{name}"')
def step_impl(context, name):
    context.add_property_page.set_property_nickname(name)
    sleep(1)

@when('Add property page: I click the continue button')
def step_impl(context):
    context.add_property_page.click_continue_button()

@when('Add property page: I fill property parcel number "{number}"')
def step_impl(context, number):
    context.add_property_page.fill_property_parcel(number)
    sleep(1)

@when('Add property page: I fill property address "{address}"')
def step_impl(context, address):
    context.add_property_page.fill_property_address(address)
    sleep(1)

@when('Add property page: I click save button')
def step_impl(context):
    context.add_property_page.click_save_button()


@when('Add property page: I verify success message')
def step_impl(context):
    context.add_property_page.verify_success_message()
    sleep(1)

@then('Add property page: I click finish button')
def step_impl(context):
    context.add_property_page.click_finish_button()
    sleep(1)


