import json
from time import time, sleep
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from Pages.LoginPage import LoginPage
from Pages.WorkStatus_Page import WorkStatusPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest

import traceback, sys

from random_name_generator import ran_name, ran_name_2
from WebConfig.time_functions import WebConfigFunctions as Config

# '''Logger'''
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# Note: Sending only pnr


class Test_WorkStatus(BaseTest):

    start_time = time()

    def process_browser_log_entry(self,entry):
        response = json.loads(entry['message'])['message']
        return response

    # Login
    @pytest.mark.pnr
    @pytest.mark.prsc
    @pytest.mark.prs
    @pytest.mark.pr
    @pytest.mark.prw
    @pytest.mark.pcnclb
    @pytest.mark.extndb
    @pytest.mark.misc
    @pytest.mark.hostrltd
    @pytest.mark.custom
    @pytest.mark.selected
    @pytest.mark.login
    def test_login(self):
        print("Start time: ", self.start_time)
        self.loginPage = LoginPage(self.driver)
        login_page = self.loginPage.do_rlogin(
                    TestData.USER_NAME, TestData.PASSWORD)
    

    @pytest.mark.login
    def test_hover(self):
        workstatuspage = WorkStatusPage(self.driver)
        sleep(3)
        workstatuspage.driver_get_url(TestData.Work_Status_URL)
        sleep(7)
        workstatuspage.hover_over_status_tile()
        sleep(2)