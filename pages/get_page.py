from pages.base_page import BasePage
from pages.locators import GetPageLocators
import requests
import json
from selenium.webdriver.common.by import By


class GetPage(BasePage):
    def click_on_get_btn(self, GET_BTNS):
        self.logger.info(f'Click on GET button {GET_BTNS}')
        get_btn = self.browser.find_element(By.CSS_SELECTOR, GET_BTNS)
        get_btn.click()

    def get_response(self):
        self.logger.info('Get original response')
        self.json_path = self.browser.find_element(*GetPageLocators.REQUEST_GET_JSON).text
        self.response = requests.get(self.base_url + self.json_path)
        self.logger.info(f'OK! Original response gotten')

    def get_response_status_code(self):
        self.logger.info('Get response status code')
        self.response_status_code = self.response.status_code
        self.logger.info(f'OK! Response status code is {self.response_status_code}')

    def get_sample_response_status_code(self):
        self.logger.info('Get sample response status code')
        self.sample_response_status_code = int(self.browser.find_element(*GetPageLocators.SAMPLE_RESPONSE_KEY).text)
        self.logger.info(f'OK! Sample response status code is {self.sample_response_status_code}')

    def get_response_json(self):
        self.logger.info('Get response JSON')
        self.response_json = self.response.json()
        self.logger.info('OK! Response JSON gotten')

    def get_sample_json(self):
        self.logger.info('Get sample response JSON')
        sample_json_text = self.browser.find_element(*GetPageLocators.SAMPLE_JSON).text
        self.sample_json = json.loads(sample_json_text)
        self.logger.info('OK! Sample response JSON gotten')

    def should_be_correct_response_status_code(self):
        self.logger.info('Checking correct response status code')
        assert self.response_status_code == self.sample_response_status_code, \
            ('Response status code is mistake', self.logger.error('Response status code is mistake'))[0]
        self.logger.info('OK! Correct response status code')

    def should_be_equals_jsons(self):
        self.logger.info('Checking equals JSONs')
        assert self.sample_json == self.response_json, \
            ('Wrong! JSONs is not equals', self.logger.error('Wrong! JSONs is not equals'))[0]
        self.logger.info('OK! JSONs is equals')
