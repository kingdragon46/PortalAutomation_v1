from time import sleep
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest
from Pages.LoginPage import LoginPage

from mail_conf import send_email

class Test_Login(BaseTest):

    def test_login_page(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(
                    TestData.USER_NAME, TestData.PASSWORD)
        print("Login done successfully")


    '''Send report'''
    # @pytest.mark.skip(reason="no need of currently testing this")
    def test_send_email_report(self):
        print("Sending report in mail....")
        # send_email()



sleep(5)