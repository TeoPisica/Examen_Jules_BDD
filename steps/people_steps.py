from behave import *
from time import sleep

@when('People page: I search for name "{search}"')
def step_impl(context, search):
    context.people_page.fill_search_field(search)
    sleep(3)

@when('People page: I click on last name "{item_name}"')
def step_impl(context, item_name):
    context.people_page.select_item_by_name(item_name)
    sleep(1)

@when('People page: I click edit button')
def step_impl(context):
    context.people_page.click_edit_button()
    sleep(1)

@when('People page: I set middle name "{name}"')
def step_impl(context, name):
    context.people_page.set_middle_name(name)
    sleep(1)

@when('People page: I set last name "{name}"')
def step_impl(context, name):
    context.people_page.set_last_name(name)
    sleep(1)

@when('People page: I click save button')
def step_impl(context):
    context.people_page.click_save_button()
    sleep(1)

@then('People page: I verify success message')
def step_impl(context):
    context.people_page.verify_success_message()
    sleep(1)

@when('People page: I click select all')
def step_impl(context):
    context.people_page.click_select_all()
    sleep(1)

@when('People page: I click delete')
def step_impl(context):
    context.people_page.click_delete()
    sleep(1)

@when('People page: I verify warning message')
def step_impl(context):
    context.people_page.verify_warning_message()
    sleep(1)

@when('People page: I confirm delete')
def step_impl(context):
    context.people_page.confirm_delete()
    sleep(1)

@when('People page: I click on ellipsis button')
def step_impl(context):
    context.people_page.click_ellipsis_button()
    sleep(1)

@when('People page: I click delete person')
def step_impl(context):
    context.people_page.delete_person_button()
    sleep(1)

