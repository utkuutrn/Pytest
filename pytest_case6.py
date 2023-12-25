from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def test_add_product_to_cart():
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

    add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
    add_to_cart_button.click()
    sleep(2)

    shopping_cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_container')
    shopping_cart_icon.click()
    sleep(2)

    cart_item = driver.find_element(By.CLASS_NAME, 'cart_item')
    assert "Sauce Labs Backpack" in cart_item.text, "Product not Add to cart"
    sleep(4)
    driver.quit()