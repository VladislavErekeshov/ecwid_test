from abc import ABC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser.browser import Browser
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import Logger


class BaseElement(ABC):
    def __init__(self, locator: tuple, name: str):
        self.__locator = locator
        self.__name = name

    def find_element(self, time=10):
        try:
            element = WebDriverWait(Browser.webdriver(), time).until(EC.presence_of_element_located(self.__locator),
                                                      message=f"Can't find element by locator {self.__locator}")
            Logger().log('INFO', f"Element {self.__name} found successfully")
            return element
        except NoSuchElementException:
            Logger().log('ERROR', f"Element {self.__name} not found, error: {NoSuchElementException}")
        except TimeoutException:
            Logger().log('ERROR', f"Element {self.__name} not found, error: {TimeoutException}")

    def click(self):
        self.find_element().click()
        Logger().log('INFO', f"Element {self.__name} clicked successfully")

    def is_clickable(self, time=10):
        WebDriverWait(Browser.webdriver(), time).until(EC.element_to_be_clickable(self.__locator),
                                                            message=f"Can't find clickable element by locator {self.__locator}")

    def is_visible(self, time=10):
        try:
            WebDriverWait(Browser.webdriver(), time).until(EC.invisibility_of_element(self.__locator),
                                                            message=f"Element still visible {self.__locator}")
            return True
        except Exception:
            return False

    def is_displayed(self) -> bool:
        element = self.find_element().is_displayed()
        Logger().log('INFO', f"Element {self.__name} displayed successfully")
        return element

    def get_attribute(self, attr_name):
        attr = self.find_element().get_attribute(attr_name)
        Logger().log('INFO', f"Attribute {attr_name} of element {self.__name} got successfully")
        return attr

    def move_cursor(self):
        ActionChains(Browser.webdriver()).move_to_element(self.find_element()).perform()
        Logger().log('INFO', f" Cursor moved to element {self.__name} successfully")

    def send_keys(self, text):
        self.find_element().send_keys(text)
        Logger().log('INFO', f" Keys send successfully to element {self.__name}")

    def clear(self):
        self.find_element().click().clear()
        Logger().log('INFO', f" Element {self.__name} cleared successfully")

    def get_text(self):
        text = self.find_element().text
        Logger().log('INFO', f"Text of element {self.__name} got successfully")
        return text

    def find_elements(self):
        elements = Browser.webdriver().find_elements(self.__locator[0], self.__locator[1])
        Logger().log('INFO', f"All elements {self.__name} found successfully")
        return elements

    def click_via_js(self):
        Browser.execute_script("arguments[0].click();", self.find_element())