from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url,\
            "It is not login page"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "Register form is not presented"

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        login.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        pass2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_FORM)
        button.click()
