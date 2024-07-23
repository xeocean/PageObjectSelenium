from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")


class LoginPageLocators:
    LOGIN_FORM = (By.NAME, 'login_submit')
    REG_FORM = (By.NAME, 'registration_submit')
    LOGIN_URL = 'login'
    REG_EMAIL = (By.NAME, 'registration-email')
    REG_PASS1 = (By.NAME, 'registration-password1')
    REG_PASS2 = (By.NAME, 'registration-password2')


class ProductPageLocators:
    BUTTON_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.XPATH, "//div[2]/h1")
    ALERT_BOOK_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

