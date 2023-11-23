from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage
from pages.forgot_password_page import ForgotPassPage
from pages.menu_page import MenuPage
from pages.add_page import AddPage
from pages.add_person_page import AddPersonPage
from pages.add_property_page import AddPropertyPage
from pages.people_page import PeoplePage
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.sign_in_page = SignInPage()
    context.sign_up_page = SignUpPage()
    context.forgot_password_page = ForgotPassPage()
    context.menu_page = MenuPage()
    context.add_page = AddPage()
    context.add_person_page = AddPersonPage()
    context.add_property_page = AddPropertyPage()
    context.people_page = PeoplePage()

def after_all(context):
    context.browser.close()