from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pytest

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_successful_login_and_redirection(setup_and_teardown):
    driver = setup_and_teardown
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    username_input = driver.find_element(By.ID, 'user-name')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    sleep(2)

    assert "/inventory.html" in driver.current_url, "Redirection failed"

    product_elements = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    product_count = len(product_elements)

    assert product_count == 6, f"Number of products is {product_count}, expected 6"