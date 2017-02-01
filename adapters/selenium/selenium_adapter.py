from .pages import HomePage, ResultPage
from .page_components import SearchBox, AnswerWidget

class Placeholder(object):
    pass

class SeleniumAdapter(object):

    URL='http://www.duckduckgo.com'

    def __init__(self, browser):
        self.pages = Placeholder()
        self.pages.search_page = HomePage(
            browser, self.URL, search_box=SearchBox(browser)
            #example of composition, using different browser for widget and home page,
            #can see it by the fact that searchbox requires a browser 
        )
        self.pages.result_page = ResultPage(
            browser, self.URL, answer_widget=AnswerWidget(browser)
        )

    def get_search_result(self, search_term):
        self.pages.search_page.search(search_term)
        return self.pages.result_page.read_the_result()

    def parse_arithmetic_result(self, search_result):
        return int(search_result)


