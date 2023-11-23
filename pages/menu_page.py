from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage(BasePage):
    SEARCH_FIELD_INPUT = (By.XPATH, '//input[@placeholder="Type and Search..."]')
    FILTER_BUTTON = (By.XPATH, '//span[contains(text(),"FILTER")]')
    ADD_BUTTON = (By.XPATH, '//span[text()="Add"]')
    PEOPLE_BUTTON = (By.XPATH, '//span[text()="People"]')
    def fill_search_field(self, search):
        self.wait_for_elem(*self.SEARCH_FIELD_INPUT)
        search_field = self.driver.find_element(*self.SEARCH_FIELD_INPUT)
        search_field.send_keys(search)
        search_field.send_keys(Keys.RETURN)

    def select_item_by_name(self, item_name):
        xpath = f"//span[contains(text(),'{item_name}')]"
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()

    def click_filter_button(self):
        self.driver.find_element(*self.FILTER_BUTTON).click()

    def click_record_button(self):
        self.driver.find_element(*self.RECORD_BUTTON).click()

    def click_add_button(self):
        self.driver.find_element(*self.ADD_BUTTON).click()

    def click_people_button(self):
        self.driver.find_element(*self.PEOPLE_BUTTON).click()

    # def press_enter(self):
    #     self.wait_for_elem(*self.INPUT)
    #     sleep(1)

    def verify_correct_page(self):
        actual = self.driver.current_url
        expected = 'https://jules.app/search/all'
        self.assertEqual(actual, expected, 'URL is incorrect.The login process is not successful.')