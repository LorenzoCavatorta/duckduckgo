from collections import namedtuple

from selenium.webdriver.common.by import By

DEFAULT_WAIT_TIME = 10
Locator = namedtuple('Locator', 'type value')


class AnswerWidget(object):
    answer_box = Locator(By.ID, 'zci-answer')
    results = Locator(By.CLASS_NAME, 'zci__result')
    
    def __init__(self, browser):
        self.browser = browser

    def read_the_result(self):
        response= self.browser.find_element_by_id(
            self.answer_box.value
        ).find_element_by_class_name(
            self.results.value
        ).text
        return response
