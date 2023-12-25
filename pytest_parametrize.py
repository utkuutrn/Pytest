import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Parametrize ile farklı kullanıcı adları ve şifreler
@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"), ("locked_out_user", "secret_sauce"), ("problem_user", "secret_sauce")])
def test_login_with_different_credentials(setup_and_teardown, username, password):
    driver = setup_and_teardown
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    username_input = driver.find_element(By.ID, 'user-name')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input.clear()
    password_input.clear()
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    # Sayfanın yüklenmesini bekleyin
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # Girişin başarısız olduğunu kontrol et
    if username == "locked_out_user":
        # Eğer kullanıcı hesabı kilitliyse
        assert "Epic sadface: Sorry, this user has been locked out." in driver.page_source, "Lockout message not displayed"
    else:
        # Diğer durumlar için
        assert "/inventory.html" in driver.current_url, "Login unsuccessful"