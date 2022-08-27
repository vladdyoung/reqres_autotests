import allure
import pytest
from pages.get_page import GetPage


@allure.feature('Test REQRES')
@allure.story('GET requests')
@allure.title('Test correct status code')
@allure.step('Checking that response status code is correct')
@pytest.mark.get_correct_status_code
@pytest.mark.parametrize('GET_BTNS', ['[data-id="users"]',
                                      '[data-id="users-single"]',
                                      '[data-id="users-single-not-found"]',
                                      '[data-id="unknown"]',
                                      '[data-id="unknown-single"]',
                                      '[data-id="unknown-single-not-found"]',
                                      '[data-id="delay"]'])
def test_correct_status_code(browser, base_url, GET_BTNS):
    get_page = GetPage(browser, base_url)
    get_page.open()
    get_page.click_on_get_btn(GET_BTNS)
    get_page.get_response()
    get_page.get_response_status_code()
    get_page.get_sample_response_status_code()
    get_page.should_be_correct_response_status_code()


@allure.feature('Test REQRES')
@allure.story('GET requests')
@allure.title('Test equals JSONs')
@allure.step('Checking that sample response JSON and JSON is equals')
@pytest.mark.equals_jsons
@pytest.mark.parametrize('GET_BTNS', ['[data-id="users-single"]',
                                      '[data-id="users-single-not-found"]',
                                      '[data-id="unknown"]',
                                      '[data-id="unknown-single"]',
                                      '[data-id="unknown-single-not-found"]',
                                      '[data-id="delay"]'])
def test_equals_jsons(browser, base_url, GET_BTNS):
    get_page = GetPage(browser, base_url)
    get_page.open()
    get_page.click_on_get_btn(GET_BTNS)
    get_page.get_response()
    get_page.get_sample_json()
    get_page.get_response_json()
    get_page.should_be_equals_jsons()
