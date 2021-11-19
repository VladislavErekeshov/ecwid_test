from selenium import webdriver
from utils.utils import Utils
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory:

    @staticmethod
    def get_driver():
        if Utils().config_data('Browser', 'browser') == 'chrome':
            return webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif Utils().config_data('Browser', 'browser') == 'firefox':
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
