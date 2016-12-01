from selenium import webdriver

from adapters.selenium.pages import HomePage, ResultPage
from adapters.selenium.page_components import AnswerWidget, SearchBox

class Placeholder(object):
    pass


URL='http://www.duckduckgo.com'


def before_all(context):
    context.browser = webdriver.Chrome('./chromedriver')
    
    context.pages = Placeholder()
    context.pages.search_page = HomePage(
        context.browser, URL, search_box=SearchBox(context.browser)
    )

    context.pages.result_page = ResultPage(
        context.browser, URL, answer_widget=AnswerWidget(context.browser)
    )

def after_all(context):
    pass
