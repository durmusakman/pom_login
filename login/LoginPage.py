from AbstractDriver import AbstractDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from utils.TestDataPrepareHandler import TestDataHelperHandler as Data


class LoginPage:

    def __init__(self, username, password, driver):
        self.driver = driver
        self.driver.get('your_test_login_link')
        time.sleep(2)
        self.driver.maximize_window()
        self.username = username
        self.password = password
        self.username_xpath = (
            By.XPATH, "your_path")
        self.password_xpath = (
            By.XPATH, "your_path")
        self.login_button_xpath = (
            By.XPATH, "your_path")

    def set_username(self):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(self.username_xpath))
        element.clear()
        element.send_keys(self.username)

    def set_password(self):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(self.password_xpath))
        element.clear()
        element.send_keys(self.password)

    def click_login_button(self):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(self.login_button_xpath))
        element.click()


class LoginPageTestCase(AbstractDriver):

    def __init__(self):
        super(LoginPageTestCase, self).__init__()

    def positive_login_test(self):
        login_page = LoginPage('true_email', 'true_password', self.driver)
        login_page.set_username()
        time.sleep(2)
        login_page.set_password()
        time.sleep(2)
        login_page.click_login_button()
        time.sleep(5)
        self.driver.quit()

    def negative_login_test(self):
        negative_login_page_test = LoginPage(Data.generate_email(), Data.generate_password(), self.driver)
        negative_login_page_test.set_username()
        time.sleep(2)
        negative_login_page_test.set_password()
        time.sleep(2)
        negative_login_page_test.click_login_button()
        time.sleep(5)
        self.driver.quit()
