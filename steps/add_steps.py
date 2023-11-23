from behave import *
from time import sleep


@when('Add page: I click on the person button')
def step_impl(context):
    sleep(1)
    context.add_page.click_person()

@when('Add page: I click on the property button')
def step_impl(context):
    context.add_page.click_property()
    sleep(3)

