import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestTask1:

    @pytest.fixture(scope="function", autouse=True)
    #fixture is
    def setup(self):
        serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://phptravels.net/home/")
        yield
        self.driver.quit()

    def test_flight(self):   #always start with test
        # actual_flight= self.driver.find_element(By.XPATH,"//a[@title='flights']").text
        # assert_that("Flights").is_equal_to(actual_flight)
        self.driver.find_element(By.XPATH,"//a[@title='flights']").click()
        self.driver.find_element(By.XPATH, " //input[@id='autocomplete']").send_keys("LAX")
        self.driver.find_element(By.XPATH,"// strong[normalize-space()='Los Angeles Intl']").click()
        self.driver.find_element(By.XPATH, " //input[@id='autocomplete2']").send_keys("DAL")
        self.driver.find_element(By.XPATH,"//b[text()='DAL']").click()
        #not working
        actions=webdriver.ActionChains(self.driver)
        actions.key_up(webdriver.Keys.SHIFT)\
                .send_keys()
        # self.driver.find_element(By.XPATH,"//input[@class ='depart form-control']").send_keys("30-05-2022")
        time.sleep(5)

# 5. Set the travel date “2022-05-30”
# 6. Adult as 2
# 7. Get the first flight details and print
# 8. Close the browser

# actions=webdriver.ActionChains(driver)
# actions.key_down((webdriver.Keys.SHIFT)\
#                  .send_keys("Hello World").key_up(webdriver.Keys.SHIFT).pause(1)\
#                  .send_keys(webdriver.Keys.ARROW_DOWN).send_keys(webdriver.Keys.ARROW_DOWN)\
#                  .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).send_keys(webdriver.Keys.ENTER)