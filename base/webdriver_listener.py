import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities import read_util

class WebDriverWrapper:
    driver=None
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name=read_util.get_value_from_json("../test_data/data.json","browser")

        if browser_name=="edge":
            self.driver=webdriver.Edge()
        elif browser_name=="ff":
            self.driver==webdriver.Firefox()
        else:
            self.driver=webdriver.Chrome()

    # def setup(self):
    #     serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")
    #     self.driver = webdriver.Chrome(service=serv_driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()
