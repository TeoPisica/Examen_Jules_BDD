from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SignInPage(Browser):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"] ')
    PASS_INPUT = (By.XPATH, '//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//span[text()="Log in"]/parent::button')
    FORGOT_PSWD_LINK = (By.XPATH, '//a[text()="Forgot password?"]')
    SIGN_UP_LINK = (By.XPATH, '//a[text()="Sign up."]')
    INPUT = (By.XPATH, '//input')



    def navigate_to_sign_in_page(self):
        self.driver.get('http://jules.app/sign-in')

    def set_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pswd(self,pswd):
        self.driver.find_element(*self.PASS_INPUT).send_keys(pswd)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def user_login(self,email,password):
        self.set_email(email)
        self.set_pswd(password)
        self.click_login_button()


    def complete_input(self, value):
        self.wait_for_elem(*self.INPUT)
        sleep(2)
        self.driver.find_element(*self.INPUT).send_keys(value)
        sleep(2)

    def click_forgot_pass_link(self):
        self.driver.find_element(*self.FORGOT_PSWD_LINK).click()

    def click_sign_up_link(self):
        self.driver.find_element(*self.SIGN_UP_LINK).click()