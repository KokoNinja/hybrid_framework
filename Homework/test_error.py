import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestError:
    @pytest.fixture(scope="function", autouse=True)
    def test_error(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://www.redbus.in/")
        driver.find_element(By.ID,"'i-icon-profile").click()



        # actual_header = driver.find_element(By.XPATH,"//h5[text()='Login']").text
        # assert_that("Login").is_equal_to(actual_header)
