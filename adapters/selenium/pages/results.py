from .base import BasePage

class ResultPage(BasePage):

    def read_the_result(self):
        return self.page_components.answer_widget.read_the_result()
