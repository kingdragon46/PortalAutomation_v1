from time import sleep
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest
from Pages.LoginPage import LoginPage

class Test_Login(BaseTest):

    def test_tag_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(
                    TestData.USER_NAME, TestData.PASSWORD)
        sleep(5)
        print("Login done successfully")
        bookinpage.quit_driver()