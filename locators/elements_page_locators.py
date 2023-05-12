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


class RadioButtonPageLocators:
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    OUTPUT_RESULT = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p/span')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.ID, 'addNewRecordButton')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = (By.XPATH, ".//ancestor::div[@class='rt-tr-group']")
    AMOUNT_OF_ROWS_IN_TABLE = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')

    # message
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CLICK_ME_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinkPageLocators:
    SIMPL_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')


class UploadAndDownloadPageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')

