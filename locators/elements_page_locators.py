from selenium.webdriver.common.by import By


class TextBoxLocators:
    ELEMENTS_MENU = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    TEXT_BOX_SUB_MENU = (By.ID, 'item-0')
    FULL_NAME_FIELD = (By.ID, 'userName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    CURRENT_ADDRESS_FIELD = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS_FIELD = (By.ID, 'permanentAddress')
    SUBMIT_BUTTON = (By.ID, 'submit')
    NAME_CREATED = (By.XPATH, '//*[@id="name"]')
    EMAIL_CREATED = (By.XPATH, '//*[@id="email"]')
    CURRENT_ADDRESS_CREATED = (By.XPATH, '//p[@id="currentAddress"]')
    PERMANENT_ADDRESS_CREATED = (By.XPATH, '//p[@id="permanentAddress"]')

