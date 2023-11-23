from behave import *
from time import sleep


@when('Menu: I fill the search field and click Enter')
def step_impl(context):
    context.menu_page.fill_search_field_click_enter()

@then('Menu: I am a user on search page')
def step_impl(context):
    context.menu_page.verify_correct_page()

@when('Menu: I am a user on search page')
def step_impl(context):
    context.menu_page.verify_correct_page()

@when('Menu: I type in search field "{search}"')
def step_impl(context, search):
    context.menu_page.fill_search_field(search)
    sleep(5)
@then('Menu: I select item "{item_name}"')
def step_impl(context, item_name):
    context.menu_page.select_item_by_name(item_name)
    sleep(5)

@when('Menu: I click on add page')
def step_impl(context):
    context.menu_page.click_add_button()
    sleep(2)

@when('Menu: I click on people page')
def step_impl(context):
    context.menu_page.click_people_button()
    sleep(2)


