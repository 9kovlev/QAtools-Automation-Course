import random

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def fill_all_fields_text_box(self):
        person_info = next(generated_person())
        fullname = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanet_address = person_info.current_address

        self.element_is_visible(self.locators.ELEMENTS_MENU).click()
        self.element_is_visible(self.locators.TEXT_BOX_SUB_MENU).click()
        self.element_is_visible(self.locators.FULL_NAME_FIELD).send_keys(fullname)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_FIELD).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS_FIELD).send_keys(permanet_address)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return fullname, email, current_address, permanet_address

    def check_filled_field(self):
        fullname = self.element_is_present(self.locators.NAME_CREATED).text.split(':')[1]
        email = self.element_is_present(self.locators.EMAIL_CREATED).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CURRENT_ADDRESS_CREATED).text.split(':')[1]
        permanet_address = self.element_is_present(self.locators.PERMANENT_ADDRESS_CREATED).text.split(':')[1]
        return fullname, email, current_address, permanet_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_randon_checkbox(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_list(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, ".//ancestor::span[@class='rct-text']")
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email,  str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.split('\n'))
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, ".//ancestor::div[@class='rt-tr-group']")
        return row.text.split('\n')
