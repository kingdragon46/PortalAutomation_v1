from time import sleep
import traceback
from Pages.BasePage import write_to_file
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest
from Pages.LoginPage import LoginPage

from mail_conf import send_email
import json

class Test_Login(BaseTest):

    def process_browser_log_entry(self,entry):
        response = json.loads(entry['message'])['message']
        return response

    def test_login_page(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(
                    TestData.USER_NAME, TestData.PASSWORD)
        try:
            p_log = bookinpage.p_log()
            events = [self.process_browser_log_entry(entry) for entry in p_log]
            events = [event for event in events if 'Network.response' in event['method']]
            with open("b_logs.json", "a", encoding="utf-8") as f:
                f.write("{")
                f.write(json.dumps(events)+",")
                f.write("}")
        except Exception as e:
            print(f"Exception: {e}\n{traceback.format_exc()}")
        print("Login done successfully")


    '''Send report'''
    # @pytest.mark.skip(reason="no need of currently testing this")
    def test_send_email_report(self):
        print("Sending report in mail....")
        # send_email()



sleep(5)