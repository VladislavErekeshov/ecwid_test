from base_classes.base_еlement import BaseElement
from utils.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
from browser.browser import Browser


class Slider(BaseElement):
    def __init__(self, locator, name):
        self.__locator = locator
        self.__name = name
        super().__init__(locator, name)

    def move(self, x):
        ActionChains(Browser.webdriver()).click_and_hold(self.find_element()).move_by_offset(x, 0).release().perform()
        Logger().log('INFO', f"Slider of element {self.__name} moved successfully")
