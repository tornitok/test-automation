import allure

from base.base_object import BaseObject
from selenium.webdriver.common.by import By
from config import Secrets, URL
from support.assertions import Assertions

class IndexPage(BaseObject):
    USER_NAME_FIELD=(By.CSS_SELECTOR, '#username')
    PASSWORD_FIELD=(By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON=(By.CSS_SELECTOR, '.login-button')
    ERROR_MESSAGE=(By.CSS_SELECTOR, '#message')

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions


    def enter_user_name(self, user_name=Secrets.USER_NAME):
        with allure.step(f'Ввод имени пользователя:{user_name}'):
            self.send_keys(self.USER_NAME_FIELD, user_name)

    def enter_password(self, password=Secrets.PASSWORD):
        with allure.step(f'Ввод имени пользователя:{password}'):
            self.send_keys(self.PASSWORD_FIELD, password)

    @allure.step('Нажатие на кнопку входа')
    def click_button(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step('Проверка валидности ссылки')
    def is_url_valid(self):
        self.assertion.assert_equal(
            expected=URL.HOVER_AND_SELECT_PAGE,
            actual=self.get_current_url()
        )

    def is_error_message_correct(self, message):
        self.assertion.assert_equal(
            expected=message,
            actual=self.get_text(self.ERROR_MESSAGE)
        )