import time
import pytest
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from assertpy import assert_that
from utilities import test_employee_datasource

class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize("username,password,firstname,middlename,lastname,expected_profile,expected_firstname",test_employee_datasource.test_add_valid_employee_data)
    def test_add_valid_employee(self,username,password,firstname,middlename,lastname,expected_profile,expected_firstname):
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        self.driver.find_element(By.LINK_TEXT,"PIM").click()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        actual_profile_header = self.driver.find_element(By.XPATH,f"//h6[contains(normalize-space(),'{firstname}')]").text
        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that(expected_profile).is_equal_to(actual_profile_header)
        assert_that(expected_firstname).is_equal_to(actual_first_name)
