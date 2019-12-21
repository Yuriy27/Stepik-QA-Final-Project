from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()
        self.solve_quiz_and_get_code()
        # time.sleep(100000)

    def should_be_added_to_cart(self):
        self.should_be_message_product_was_added()
        self.should_be_message_with_cart_price()

    def should_be_message_product_was_added(self):
        product_title = self.browser\
            .find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_added_msg = self.browser\
            .find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert product_title == product_added_msg

    def should_be_message_with_cart_price(self):
        product_price = self.browser \
            .find_element(*ProductPageLocators.PRODUCT_PRICE).text
        car_price = self.browser \
            .find_element(*ProductPageLocators.CART_PRICE).text
        assert product_price == car_price
