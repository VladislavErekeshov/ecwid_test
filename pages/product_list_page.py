from base_classes.base_form import BaseForm
from base_classes.button import Button
from selenium.webdriver.common.by import By
from base_classes.text import Text
from base_classes.text_field import TextField
from base_classes.slider import Slider


class ProductListPage(BaseForm):

    __on_sale_checkbox = Button((By.ID, 'checkbox-on_sale'), 'on_sale_checkbox')
    __sale_label_text = Text((By.XPATH,
        '//div[contains(@class,"grid-product__textblock") and contains(@class,"grid-product__price-label")]'),
                              'sale_label_text')
    __product_name = Text((By.CLASS_NAME, 'grid-product__title-inner'), 'product_name')
    __sale_filter = Text((By.XPATH, '//div[@class="ec-pill__text"]//span[contains(text(), "Со скидкой")]'),
                         'sale_filter')
    __min_price_input = TextField((By.XPATH, '//input[@class="form-control__text" and @aria-label="от"]'),
                                  'min_price_input')
    __max_price_input = TextField((By.XPATH, '//input[@class="form-control__text" and @aria-label="до"]'),
                                  'max_price_input')
    __min_price_slider = Slider((By.XPATH, '//div[contains(@class,"ec-range__runner--left")]'), 'min_price_slider')
    __max_price_slider = Slider((By.XPATH, '//div[contains(@class,"ec-range__runner--right")]'), 'max_price_slider')
    __price_filter = Text((By.XPATH, '//div[@class="ec-pill__text"]//span[contains(text(), "$")]'),
                         'price_filter')

    __price_label_text = Text((By.XPATH,
                              '//div[@class="grid__wrap"]//div[contains(@class,"grid-product__price-value") and contains(@class,"ec-price-item")]'),
                             'price_label_text')

    __products_loading_div = Text((By.XPATH,
                                  '//div[contains(@class,"grid__products--loading") and contains(@class,"grid__products--classic")]'), 'products_loading')


    def __init__(self):
        super().__init__(element=self.__on_sale_checkbox,
                         name='product_list_page_unique_element')

    def on_sale_checkbox_click(self):
        self.__on_sale_checkbox.click()

    def sale_filter_is_displayed(self):
        try:
            self.__sale_filter.is_displayed()
            return True
        except Exception:
            return False

    def discounted_products_check(self):
        if len(self.__product_name.find_elements()) == len(self.__sale_filter.find_elements()):
            return True
        else:
            return False

    def input_price_by_textfield(self, min_price, max_price):
        self.__min_price_input.send_keys(min_price)
        self.__max_price_input.send_keys(max_price)

    def input_price_by_slider(self, min_price, max_price):
        self.__min_price_slider.is_clickable()
        self.__min_price_slider.move(min_price * 40)
        self.__max_price_slider.is_clickable()
        self.__max_price_slider.move((5 - max_price) * -40)

    def price_filter_is_displayed(self):
        try:
            self.__price_filter.is_displayed()
            return True
        except Exception:
            return False

    def price_filter_is_correct(self, min_price, max_price):
        if self.__price_filter.get_text() == f"${min_price} - ${max_price}":
            return True
        else:
            return False

    def products_load_wait(self):
        return self.__products_loading_div.is_visible()

    def products_filtered_by_price(self, min_price, max_price):
        n = 0
        for element in self.__price_label_text.find_elements():
            if int(element.text[1:2]) in range(min_price, max_price + 1):
                n += 1

        if n == len(self.__price_label_text.find_elements()):
            return True
        else:
            return False




