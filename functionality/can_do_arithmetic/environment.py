from selenium import webdriver

from adapters.selenium.selenium_adapter import SeleniumAdapter


def before_all(context):
    context.browser = webdriver.Chrome('./chromedriver') #is this the best way to do it?
    
    context.adapter = SeleniumAdapter(context.browser)
    
def after_all(context):
    pass

