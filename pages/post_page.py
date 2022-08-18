from pages.base_page import BasePage
from pages.locators import PostPageLocators
import requests
import json


class PostPage(BasePage):
    def click_on_post_btn(self):
        self.logger.info(f'Click on CREATE POST button')
        post_btn = self.browser.find_element(*PostPageLocators.BTN_POST_CREATE)
        post_btn.click()

    def post_request_with_positive_data(self):
        self.logger.info('POST request with positive data')
        self.json_path = self.browser.find_element(*PostPageLocators.REQUEST_POST_JSON).text
        positive_data_text = (
            (self.browser.find_element(*PostPageLocators.POSITIVE_DATA).text).replace('\n', '')).replace(' ', '')
        positive_data_json = json.loads(positive_data_text)
        self.response = requests.post(self.base_url + self.json_path, data=positive_data_json)
        self.logger.info(f'OK! Original post response with positive data gotten')

    def get_response_status_code(self):
        self.logger.info('Get response status code')
        self.response_status_code = self.response.status_code
        self.logger.info(f'OK! Response status code is {self.response_status_code}')

    def get_sample_response_status_code(self):
        self.logger.info('Get sample response status code')
        self.sample_response_status_code = int(self.browser.find_element(*PostPageLocators.SAMPLE_RESPONSE_KEY).text)
        self.logger.info(f'OK! Sample response status code is {self.sample_response_status_code}')

    def get_response_json(self):
        self.logger.info('Get response JSON')
        self.response_text = self.response.text
        self.response_json = json.loads(self.response_text)
        self.logger.info('OK! Response JSON gotten')

    def get_sample_json(self):
        self.logger.info('Get sample response JSON')
        self.sample_json_text = (
            (self.browser.find_element(*PostPageLocators.POSITIVE_DATA).text).replace('\n', '')).replace(' ', '')
        self.sample_json = json.loads(self.sample_json_text)
        self.logger.info('OK! Sample response JSON gotten')

    def should_be_correct_response_status_code(self):
        self.logger.info('Checking correct response status code')
        assert self.response_status_code == self.sample_response_status_code, \
            ('Response status code is mistake', self.logger.error('Response status code is mistake'))[0]
        self.logger.info('OK! Correct response status code')

    def should_be_post_response_with_positive_data(self):
        self.logger.info('Checking that new user is create with positive data')
        assert self.sample_json['name'] == self.response_json['name'] and \
               self.sample_json['name'] == self.response_json['name'], \
            ('Wrong! New user is not create', self.logger.error('Wrong! New user is not create'))[0]
        self.logger.info('OK! New user is create')

    def post_request_with_empty_data(self):
        self.logger.info('POST request with empty data')
        self.json_path = self.browser.find_element(*PostPageLocators.REQUEST_POST_JSON).text
        self.response_empty_data = requests.post(self.base_url + self.json_path, data='{}')
        self.logger.info(f'OK! Original post response with empty data gotten')

    def get_response_json_with_empty_data(self):
        self.logger.info('Get response JSON')
        self.response_integer_data_text = self.response_empty_data.text
        self.response_empty_data_text_json = json.loads(self.response_integer_data_text)
        self.logger.info('OK! Response JSON gotten')

    def should_be_post_response_with_empty_data(self):
        self.logger.info('Checking that new user is create with empty data')
        assert self.response_empty_data_text_json.get('name', False) != False, \
            ('Wrong! New user is not create with empty data',
             self.logger.error('Wrong! New user is not create with empty data'))[0]
        self.logger.info('OK! New user is create')

    def post_request_with_integer_data(self):
        self.logger.info('POST request with integer data')
        self.json_path = self.browser.find_element(*PostPageLocators.REQUEST_POST_JSON).text
        int_data = {"name": "111", "job": "111"}
        self.response_integer_data = requests.post(self.base_url + self.json_path, data=int_data)
        self.logger.info(f'OK! Original post response with integer data gotten')

    def get_response_json_with_integer_data(self):
        self.logger.info('Get response JSON')
        self.response_integer_data_text = self.response_integer_data.text
        self.response_integer_data_text_json = json.loads(self.response_integer_data_text)
        self.logger.info('OK! Response JSON gotten')

    def should_be_post_response_with_integer_data(self):
        self.logger.info('Checking that new user is create with integer data')
        assert self.response_integer_data_text_json.get('name', False) == False, \
            ('Wrong! New user is not create with integer data',
             self.logger.error('Wrong! New user is not create with integer data'))[0]
        self.logger.info('OK! New user is create')

    def post_request_with_special_characters(self):
        self.logger.info('POST request with special characters')
        self.json_path = self.browser.find_element(*PostPageLocators.REQUEST_POST_JSON).text
        cpec_data = {"name": "!@#", "job": "!@#"}
        self.response_special_characters = requests.post(self.base_url + self.json_path, data=cpec_data)
        self.logger.info(f'OK! Original post response with special characters gotten')

    def get_response_json_with_special_characters(self):
        self.logger.info('Get response JSON')
        self.response_special_characters_text = self.response_special_characters.text
        self.response_special_characters_text_json = json.loads(self.response_special_characters_text)
        self.logger.info('OK! Response JSON gotten')

    def should_be_post_response_with_special_characters(self):
        self.logger.info('Checking that new user is create with special characters')
        assert self.response_special_characters_text_json.get('name', False) == False, \
            ('Wrong! New user is not create with special_characters',
             self.logger.error('Wrong! New user is not create with special_characters'))[0]
        self.logger.info('OK! New user is create')
