from .base import BasePage

class HomePage(BasePage):

    def search(self, term):
        self.visit()
        return self.page_components.search_box.search(term)
    
