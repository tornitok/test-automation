from base.base_object import BaseObject
from selenium.webdriver.common.by import By
from support.assertions import Assertions

class CheckValidate(BaseObject):
    ENTER_VALUE_FIELD=(By.CSS_SELECTOR, '#dataInput')
    MESSAGE=(By.CSS_SELECTOR, '#validationSquare')

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions

    def enter_number(self, number):
        self.send_keys(self.ENTER_VALUE_FIELD, number)

    def is_message_correct(self, message):
        self.assertion.assert_equal(
            expected=message,
            actual=self.get_text(self.MESSAGE)
        )