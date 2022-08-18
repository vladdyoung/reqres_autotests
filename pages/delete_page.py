from pages.base_page import BasePage
from pages.locators import DeletePageLocators
import requests


class DeletePage(BasePage):
    def click_on_delete_btn(self):
        self.logger.info(f'Click on DELETE button')
        del_btn = self.browser.find_element(*DeletePageLocators.BTN_DELETE_CREATE)
        del_btn.click()

    def delete_request(self):
        self.logger.info('DELETE request')
        self.json_path = self.browser.find_element(*DeletePageLocators.REQUEST_DELETE_JSON).text
        self.response = requests.delete(self.base_url + self.json_path)
        self.logger.info(f'OK! Original delete response gotten')

    def get_response_status_code(self):
        self.logger.info('Get response status code')
        self.response_status_code = self.response.status_code
        self.logger.info(f'OK! Response status code is {self.response_status_code}')

    def get_sample_response_status_code(self):
        self.logger.info('Get sample response status code')
        self.sample_response_status_code = int(self.browser.find_element(*DeletePageLocators.SAMPLE_RESPONSE_KEY).text)
        self.logger.info(f'OK! Sample response status code is {self.sample_response_status_code}')

    def should_be_correct_response_status_code(self):
        self.logger.info('Checking correct response status code')
        assert self.response_status_code == self.sample_response_status_code, \
            ('Response status code is mistake', self.logger.error('Response status code is mistake'))[0]
        self.logger.info('OK! Correct response status code')

    def get_response_json(self):
        self.logger.info('Get response JSON')
        self.response_text = self.response.text
        self.logger.info('OK! Response JSON gotten')

    def should_be_delete_success(self):
        self.logger.info('Checking delete success')
        assert len(self.response_text) == 0, \
            ('Wrong! Not delete', self.logger.error('Wrong! Not delete'))[0]
        self.logger.info('OK! Successfully delete')
