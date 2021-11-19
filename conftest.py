from browser.browser import Browser
import pytest


@pytest.fixture(scope='function')
def set_up():
    current_browser = Browser()
    Browser.get('https://buy-in-10-seconds.company.site/search')
    yield
    current_browser.tear_down()