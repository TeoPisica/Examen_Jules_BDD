import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.delete_all_cookies()

    def close(self):
        self.driver.close()

    def click_element(self, by, selector):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, selector)))
        element.click()

    def press_enter(self, by, selector):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))
        element.send_keys(Keys.ENTER)

    # Example usage in a test case
    if __name__ == '__main__':
        browser = Browser()
        try:
            browser.driver.get('https://example.com')
            browser.click_element(By.XPATH, '//button[text()="Click me"]')
        finally:
            browser.close()