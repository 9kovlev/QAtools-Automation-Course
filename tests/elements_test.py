import random
import time
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


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

    class TestWebTable:
        def test_web_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_web_table_page_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            print(key_word)
            print(table_result)
            assert key_word in table_result, "The person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "The person card has been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found", "The person still exists in the page after deleting"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "The numbers of rows have not been changed"

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_on_different_buttton('double')
            right = buttons_page.click_on_different_buttton('right')
            click = buttons_page.click_on_different_buttton('click')

            assert double == "You have done a double click", "double click has not performed"
            assert right == "You have done a right click", "right click has not performed"
            assert click == "You have done a dynamic click", "dynamic click has not performed"


