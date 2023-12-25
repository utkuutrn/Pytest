from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def test_filter_product_count():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    sleep(2)

    username_input = driver.find_element(By.ID, 'user-name')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input.clear()
    password_input.clear()
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    sleep(2)

    category_dropdown = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    category_dropdown.click()
    sleep(1)

    driver.find_element(By.XPATH, "//option[text()='Price (low to high)']").click()
    sleep(2)

    filtered_product_elements = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(filtered_product_elements) > 0, "Product filtering failed"

    driver.quit()