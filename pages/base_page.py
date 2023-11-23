# import unittest
from selenium.webdriver.common.keys import Keys
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class BasePage(Browser):
# class BasePage(Browser, unittest.TestCase):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))

    def verify_page_url(self, expected):
        actual = self.driver.current_url
        assert actual == expected, 'url is not correct'

    def wait_and_click_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        self.driver.find_element(by, selector).click()

    def press_enter(self, elem):
        elem.send_keys(Keys.ENTER)

