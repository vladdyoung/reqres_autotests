import allure
import pytest
from pages.post_page import PostPage


@allure.feature('Test REQRES')
@allure.story('CREATE POST requests')
@allure.title('Test correct status code')
@allure.step('Checking that response status code is correct')
@pytest.mark.post_correct_status_code
def test_correct_status_code(browser, base_url):
    get_page = PostPage(browser, base_url)
    get_page.open()
    get_page.click_on_post_btn()
    get_page.post_request_with_positive_data()
    get_page.get_response_status_code()
    get_page.get_sample_response_status_code()
    get_page.should_be_correct_response_status_code()


@allure.feature('Test REQRES')
@allure.story('CREATE POST requests')
@allure.title('Test correct create nuw user with positive date')
@allure.step('Checking that correct create nuw user with positive data')
@pytest.mark.crate_new_user_with_positive_data
def test_crate_new_user_with_positive_data(browser, base_url):
    get_page = PostPage(browser, base_url)
    get_page.open()
    get_page.click_on_post_btn()
    get_page.post_request_with_positive_data()
    get_page.get_sample_json()
    get_page.get_response_json()
    get_page.should_be_post_response_with_positive_data()


@allure.feature('Test REQRES')
@allure.story('CREATE POST requests')
@allure.title('Test create nuw user with empty data')
@allure.step('Checking that nuw user with empty data is not created')
@pytest.mark.xfail
@pytest.mark.crate_new_user_with_empty_data
def test_crate_new_user_with_empty_data(browser, base_url):
    get_page = PostPage(browser, base_url)
    get_page.open()
    get_page.click_on_post_btn()
    get_page.post_request_with_empty_data()
    get_page.get_response_json_with_empty_data()
    get_page.should_be_post_response_with_empty_data()


@allure.feature('Test REQRES')
@allure.story('CREATE POST requests')
@allure.title('Test create nuw user with integer data')
@allure.step('Checking that nuw user with integer data is not created')
@pytest.mark.xfail
@pytest.mark.crate_new_user_with_integer_data
def test_crate_new_user_with_integer_data(browser, base_url):
    get_page = PostPage(browser, base_url)
    get_page.open()
    get_page.click_on_post_btn()
    get_page.post_request_with_integer_data()
    get_page.get_response_json_with_integer_data()
    get_page.should_be_post_response_with_integer_data()


@allure.feature('Test REQRES')
@allure.story('CREATE POST requests')
@allure.title('Test create nuw user with special characters')
@allure.step('Checking that nuw user with special characters is not created')
@pytest.mark.xfail
@pytest.mark.crate_new_user_with_special_characters
def test_crate_new_user_with_special_characters(browser, base_url):
    get_page = PostPage(browser, base_url)
    get_page.open()
    get_page.click_on_post_btn()
    get_page.post_request_with_special_characters()
    get_page.get_response_json_with_special_characters()
    get_page.should_be_post_response_with_special_characters()
