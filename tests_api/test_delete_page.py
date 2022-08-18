import allure
import pytest
from pages.delete_page import DeletePage


@allure.feature('Test REQRES')
@allure.story('DELETE requests')
@allure.title('Test correct delete status code')
@allure.step('Checking that delete successfully')
@pytest.mark.delete_correct_status_code
def test_correct_status_code(browser, base_url):
    del_page = DeletePage(browser, base_url)
    del_page.open()
    del_page.click_on_delete_btn()
    del_page.delete_request()
    del_page.get_response_status_code()
    del_page.get_sample_response_status_code()
    del_page.should_be_correct_response_status_code()


@allure.feature('Test REQRES')
@allure.story('DELETE requests')
@allure.title('Test correct delete')
@allure.step('Checking that delete successfully')
@pytest.mark.delete_successfully
def test_delete(browser, base_url):
    del_page = DeletePage(browser, base_url)
    del_page.open()
    del_page.click_on_delete_btn()
    del_page.delete_request()
    del_page.get_response_json()
    del_page.should_be_delete_success()