from selenium.common import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def add_product(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button.click()

    def search_name_book(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return book_name

    def check_add_name_book(self, book_name):
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME).text
        assert book_name == alert_book_name, "Error"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Wrong show success message"

    def is_disappered_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Wrong show success message"
