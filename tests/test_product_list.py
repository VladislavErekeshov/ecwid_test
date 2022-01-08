from utils.utils import Utils
from pages.product_list_page import ProductListPage
import pytest
import allure
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("set_up")
class TestProductList:

    __utils = Utils()
    __min_price = int(__utils.test_data('Price', 'min_price'))
    __max_price = int(__utils.test_data('Price', 'max_price'))

    @allure.feature('Buy in 10 seconds site')
    @allure.story('test_discounted_products')
    @allure.severity('critical')
    def test_discounted_products(self):
        product_list_page = ProductListPage()
        product_list_page.on_sale_checkbox_click()
        assert product_list_page.sale_filter_is_displayed() is True, 'The filter did not apply'
        assert product_list_page.products_load_wait() is True, 'Page has not been updated'
        assert product_list_page.discounted_products_check() is True, 'The number of regular and discounted products was not the same'

    @allure.feature('Buy in 10 seconds site')
    @allure.story('test_price_sort_by_slider')
    @allure.severity('critical')
    def test_price_sort_by_slider(self):
        product_list_page = ProductListPage()

        product_list_page.input_price_by_slider(self.__min_price, self.__max_price)
        assert product_list_page.price_filter_is_displayed() is True, 'The filter did not apply'
        assert product_list_page.price_filter_is_correct(self.__min_price, self.__max_price) is True, 'The filter is not correct'
        assert product_list_page.products_load_wait() is True, 'Page has not been updated'
        assert product_list_page.products_filtered_by_price(self.__min_price, self.__max_price) is True, 'Products are not sorted'

    @allure.feature('Buy in 10 seconds site')
    @allure.story('test_price_sort_by_textfield')
    @allure.severity('critical')
    def test_price_sort_by_textfield(self):
        product_list_page = ProductListPage()

        product_list_page.input_price_by_textfield(self.__min_price, self.__max_price)
        assert product_list_page.price_filter_is_displayed() is True, 'The filter did not apply' #эта штука действительно не работает на сайте
        assert product_list_page.price_filter_is_correct(self.__min_price,
                                                         self.__max_price) is True, 'The filter is not correct'
        assert product_list_page.products_load_wait() is True, 'Page has not been updated'
        assert product_list_page.products_filtered_by_price(self.__min_price, self.__max_price) is True, 'Products are not sorted'