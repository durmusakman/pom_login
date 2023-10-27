from abc import ABC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class AbstractDriver(ABC):

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_driver(self):
        return self.driver
