from collections import namedtuple

from selenium.webdriver.common.by import By

Locator = namedtuple('Locator', 'type value')


class SearchBox(object):
    search_input = Locator(By.ID, 'search_form_input_homepage')
    search_button = Locator(By.ID, 'search_button_homepage')

    def __init__(self, browser):
        self.browser = browser

    def search(self, term):
        search_box = self.browser.find_element_by_id(
            self.search_input.value
        )
        search_box.send_keys(term)
        search_button = self.browser.find_element_by_id(
            self.search_button.value
        )
        search_button.click()

