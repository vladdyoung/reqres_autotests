from selenium.webdriver.common.by import By


class GetPageLocators:
    SAMPLE_RESPONSE_KEY = (By.CSS_SELECTOR, '[data-key="response-code"]')
    SAMPLE_JSON = (By.CSS_SELECTOR, '[data-key="output-response"]')
    REQUEST_GET_JSON = (By.CSS_SELECTOR, '[data-key="url"]')


class PostPageLocators:
    SAMPLE_RESPONSE_KEY = (By.CSS_SELECTOR, '[data-key="response-code"]')
    BTN_POST_CREATE = (By.CSS_SELECTOR, '[data-id="post"]')
    REQUEST_POST_JSON = (By.CSS_SELECTOR, '[data-key="url"]')
    POSITIVE_DATA = (By.CSS_SELECTOR, '[data-key="output-request"]')
    SAMPLE_JSON = (By.CSS_SELECTOR, '[data-key="output-response"]')


class DeletePageLocators:
    REQUEST_DELETE_JSON = (By.CSS_SELECTOR, '[data-key="url"]')
    SAMPLE_JSON = (By.CSS_SELECTOR, '[data-key="output-response"]')
    BTN_DELETE_CREATE = (By.CSS_SELECTOR, '[data-id="delete"]')
    SAMPLE_RESPONSE_KEY = (By.CSS_SELECTOR, '[data-key="response-code"]')
