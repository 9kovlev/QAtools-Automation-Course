import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            fullname, email, current_address, permanet_address = text_box_page.fill_all_fields_text_box()
            created_name, created_email, created_current_address, created_permanent_address = text_box_page.check_filled_field()

            assert fullname == created_name, "The full name does not match"
            assert email == created_email, "The email does not match"
            assert current_address == created_current_address, "The current address does not match"
            assert permanet_address == created_permanent_address, "The permanet address does not match"



