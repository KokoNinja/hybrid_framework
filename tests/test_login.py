import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper


class TestLogin(WebDriverWrapper):

    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_text)

    def test_invalid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("pass")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_text1 = self.driver.find_element(By.XPATH, "//p[contains(normalize-space() = 'Invalid credentials')]").text
        assert_that("Invalid credentials").is_equal_to(actual_text1)
        time.sleep(5)




class TestLoginUI(WebDriverWrapper):

    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5").text
        assert_that("Login").is_equal_to(actual_header)
