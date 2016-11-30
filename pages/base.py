class Placeholder(object):
    pass
    

class BasePage(object):

    """Shared functionality for the Pages"""

    def __init__(self, browser, url, **kwargs):
        self.url = url
        self.browser = browser
        self.page_components = Placeholder()
        for k, v in kwargs.items():
            setattr(self.page_components, k, v)

    def visit(self):
        self.browser.get(self.url)
