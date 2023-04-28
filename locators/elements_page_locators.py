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


class CheckBoxPageLocators:
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    HOME_BUTTON = '//*[@id="tree-node"]/ol/li/span/label/span[1]'
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    SELECTED_ALL = '//*[@id="result"]/span'
    EXPAND_ALL_BUTTON = (By.XPATH, '//*[@id="tree-node"]/div/button[1]')
    HOME_FOLDER = '//*[@id="tree-node"]/ol/li/span/label'
    DESKTOP_FOLDER = '//*[@id="tree-node"]/ol/li/ol/li[1]/span'
    NOTES_FILE = '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[1]'
    COMMANDS_FILE = '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[2]/span'
    DOCUMENTS_FOLDER = '//*[@id="tree-node"]/ol/li/ol/li[2]/span'
    WORKSPACE_FOLDER = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span'
    REACT_FILE = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span'
    ANGULAR_FILE = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]'
    VEU_FILE = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span'
    OFFICE_FOLDER = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span'
    PUBLIC_FILE = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]'
    PRIVATE_FILE = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span'
    CLASSIFIED_FILE = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]'
    GENERAL_FILE = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]'
    DOWNLOADS_FOLDER = '//*[@id="tree-node"]/ol/li/ol/li[3]/span'
    WORD_FILE_DOC = '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span'
    EXCEL_FILE_DOC = '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]'
    COLLAPSE_ALL_BUTTON = '//*[@id="tree-node"]/div/button[2]'
