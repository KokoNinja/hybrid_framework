import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestTask1:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.redbus.in/")
        yield
        self.driver.quit()

    def test_title(self):
        actual_title = self.driver.title
        assert_that("Book Bus Travels, AC Volvo Bus, rPool & Bus Hire - redBus India").is_equal_to(actual_title)

    def test_login(self):
        self.driver.find_element(By.XPATH, "//i[@id='i-icon-profile']").click()
        self.driver.find_element(By.XPATH,"//li[@id='signInLink']").click()
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH,"//input[@id='mobileNoInp']").send_keys("7898")
        actual_error=self.driver.find_element(By.XPATH,"//span[text()='Please enter valid mobile number']").text
        assert_that("Please enter valid mobile number").is_equal_to(actual_error)
        print(actual_error)

        time.sleep(5)
