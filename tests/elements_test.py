import time
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_randon_checkbox()
            check_box_page.get_checked_list()
            input_checkbox = check_box_page.get_checked_list()
            output_result = check_box_page.get_output_result()
            assert input_checkbox in output_result, "checkboxes have not been selected"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "Yes has not been selected"
            assert output_impressive == "Impressive", "Impressive has not been selected"
            assert output_no == "No", "No has not been selected"



