from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class PeoplePage(BasePage):
    SEARCH_FIELD_INPUT = (By.XPATH, '//input[@placeholder="Type to search..."]')
    EDIT_BUTTON = (By.XPATH, '//span[contains(text(), "EDIT")]')
    MIDDLE_NAME_INPUT = (By.XPATH, '//label[contains(text(), "Middle")]/parent::div//div//input')
    LAST_NAME_INPUT = (By.XPATH, '//label[contains(text(), "Last")]/parent::div//div//input')
    SAVE_BUTTON = (By.XPATH, '//span[contains(text(), "SAVE")]')
    SUCCES_MESSAGE = (By.XPATH, '//span[contains(text(), "successfully")]')
    SELECT_ALL_BUTTON = (By.XPATH, '//span[contains(text(), "Select All")]')
    DELETE_BUTTON = (By.XPATH, '//*[local-name()="svg"]/following-sibling::text()[contains(., "Delete")]/parent::div')
    WARNING_MESSAGE = (By.XPATH, '//span[contains(text(), "Delete Person")]')
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//span[contains(text(), "DELETE")]')
    ELLIPSIS_BUTTON = (By.XPATH, '(//span[contains(text(), "EDIT")]/following::button//*[local-name()="svg" and contains(@class, "MuiSvgIcon-root")])[1]')
    DELETE_PERSON_BUTTON = (By.XPATH, '//li[contains(., "Delete Person")]')




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

    def set_middle_name(self, name):
        self.wait_for_elem(*self.MIDDLE_NAME_INPUT)
        sleep(2)
        middle_name_input = self.driver.find_element(*self.MIDDLE_NAME_INPUT)
        # Clear existing text using backspace
        current_text = middle_name_input.get_attribute("value")
        for _ in range(len(current_text)):
            middle_name_input.send_keys(Keys.BACKSPACE)
        # Enter the new input
        middle_name_input.send_keys(name)

    def set_last_name(self, name):
        self.wait_for_elem(*self.LAST_NAME_INPUT)
        sleep(2)
        last_name_input = self.driver.find_element(*self.LAST_NAME_INPUT)
        current_text = last_name_input.get_attribute("value")
        for _ in range(len(current_text)):
            last_name_input.send_keys(Keys.BACKSPACE)
        last_name_input.send_keys(name)


    def click_edit_button(self):
        self.driver.find_element(*self.EDIT_BUTTON).click()
        sleep(2)

    def click_save_button(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()
        sleep(2)

    def verify_success_message(self):
        assert self.driver.find_element(*self.SUCCES_MESSAGE).is_displayed(), 'The message is not displayed!'

    def click_select_all(self):
        self.driver.find_element(*self.SELECT_ALL_BUTTON).click()
        sleep(2)

    def click_delete(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()
        sleep(2)

    def verify_warning_message(self):
        assert self.driver.find_element(*self.WARNING_MESSAGE).is_displayed(), 'The message is not displayed!'

    def confirm_delete(self):
        self.driver.find_element(*self.CONFIRM_DELETE_BUTTON).click()
        sleep(2)

    def click_ellipsis_button(self):
        self.driver.find_element(*self.ELLIPSIS_BUTTON).click()
        sleep(2)
    def delete_person_button(self):
        self.driver.find_element(*self.DELETE_PERSON_BUTTON).click()
        sleep(2)