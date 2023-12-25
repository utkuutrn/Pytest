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

def test_login_with_empty_username(setup_and_teardown):
    driver = setup_and_teardown
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    sleep(2)
    
    username_input = driver.find_element(By.ID, 'user-name')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')
    
    username_input.clear()
    password_input.clear()
    login_button.click()
    sleep(2)
    
    assert "Epic sadface: Username is required" in driver.page_source, "Warning message not displayed"