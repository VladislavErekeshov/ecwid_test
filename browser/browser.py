import weakref
from browser.browser_factory import BrowserFactory


class Browser(object):

    __driver = None
    _alive = []

    def __new__(cls):
        if cls not in cls._alive:
            cls.instance = super(Browser, cls).__new__(cls)
            Browser._alive.append(cls.instance)
            cls.__driver = BrowserFactory().get_driver()
        return weakref.proxy(cls.instance)

    def tear_down(self):
        self.__driver.close()
        self.__driver.quit()
        self._alive.remove(self)

    @classmethod
    def webdriver(cls):
        return cls.__driver

    @classmethod
    def get(cls, url):
        return cls.__driver.get(url)

    @classmethod
    def switch_to_alert(cls):
        return cls.__driver.switch_to_alert()

    @classmethod
    def current_url(cls):
        return cls.__driver.current_url

    @classmethod
    def back(cls):
        return cls.__driver.back()

    @classmethod
    def switch_to_iframe_by_id(cls, id):
        return cls.__driver.switch_to.frame(cls.__driver.find_element_by_id(id))

    @classmethod
    def switch_to_default_content(cls):
        return cls.__driver.switch_to.default_content()

    @classmethod
    def execute_script(cls, *args):
        return cls.__driver.execute_script(*args)


