import time
import pytest
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from assertpy import assert_that
from utilities import test_employee_datasource


class TestAddEmployee(WebDriverWrapper):

    def test_invalid_profile_upload(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.LINK_TEXT, "PIM").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        #self.driver.find_element(By.CLASS_NAME,"employee-image").click()
        self.driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Users\110796\Downloads\Bluetooth\Bluetooth\A2DP.TS.p17.pdf")
        actual_error=self.driver.find_element(By.XPATH,"span[contains(normalize-space(),'not allowed')]").text
        assert_that(actual_error).is_equal_to("File type not allowed")

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
        # wait=WebDriverWait(self.driver,30)
        # wait.until(expected_conditions.text_t)
        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that(expected_profile).is_equal_to(actual_profile_header)
        assert_that(expected_firstname).is_equal_to(actual_first_name)
