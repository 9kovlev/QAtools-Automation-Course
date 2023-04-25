from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxLocators


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

        #assert 'Nika Teylor' == self.driver.find_element(By.ID, 'name').text[5:]
        # assert('1@i.ua', self.driver.find_element(self.locators.EMAIL_ROW).text[6:])
        # assert('Naymova 23 street', self.driver.find_element(self.locators.CURRENT_ADDRESS_ROW).text[17:])
