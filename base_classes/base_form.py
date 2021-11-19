from abc import ABC
from base_classes.base_еlement import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from browser.browser import Browser


class BaseForm(ABC):
    def __init__(self, element: BaseElement, name: str):
        self.__element = element
        self.__name = name

    def is_displayed(self):
        return self.__element.is_displayed()

    def wait_for_open(self, time=10):
        WebDriverWait(Browser.webdriver(), time).until(self.is_displayed())

    def scroll_down(self, offset=0):
        if offset:
            Browser.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            Browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        if offset:
            Browser.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            Browser.execute_script('window.scrollTo(0, -document.body.scrollHeight);')
