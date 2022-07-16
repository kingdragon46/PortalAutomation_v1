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
    
    # @pytest.mark.login
    @pytest.mark.skip
    def test_teamsNavLink_not_visible_to_employee(self):
        self.loginPage = LoginPage(self.driver)
        login_page = self.loginPage.do_rlogin(
                    TestData.USER_NAME_3, TestData.PASSWORD_3)
        workstatuspage = WorkStatusPage(self.driver)
        sleep(3)
        workstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(7)

        teams_invisible = workstatuspage.is_invisible(WorkStatusPage.TEAMS_NAV_LINK)
        print('invisible: ', teams_invisible)
        assert teams_invisible == True
        sleep(2)
        workstatuspage.logout()
        sleep(2)

    # Login
    @pytest.mark.selected
    @pytest.mark.login
    def test_login(self):
        print("Start time: ", self.start_time)
        self.loginPage = LoginPage(self.driver)
        login_page = self.loginPage.do_rlogin(
                    TestData.USER_NAME, TestData.PASSWORD)
    
    @pytest.mark.login
    def test_change_self_status(self):
        workstatuspage = WorkStatusPage(self.driver)
        sleep(3)
        workstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(7)
        workstatuspage.workstatuspage_teams_filter()
        sleep(2)
        workstatuspage.workstatuspage_hover_over_status_tile()
        sleep(2)

    # @pytest.mark.login
    def test_change_teamEmployee_status(self):
        workstatuspage = WorkStatusPage(self.driver)
        sleep(3)
        workstatuspage.driver_get_url(TestData.WORK_STATUS_TEAMS_URL)
        sleep(7)
        workstatuspage.teamspage_teams_filter()
        sleep(2)
        workstatuspage.teamspage_changeEmployeeStatus()
        sleep(2)

    # @pytest.mark.login
    def test_teamEmployee_status_change_visible_in_insights(self):
        workstatuspage = WorkStatusPage(self.driver)
        sleep(3)
        workstatuspage.driver_get_url(TestData.WORK_STATUS_INSIGHTS_URL)
        sleep(7)
        workstatuspage.insightspage_employeestatus_filter()
        stat1 = workstatuspage.get_element_text(WorkStatusPage.InsightsPage_Office_FirstDate)
        print('\nstat1: ', stat1)
        # Teams Page Start
        workstatuspage.driver_get_url(TestData.WORK_STATUS_TEAMS_URL)
        sleep(7)
        workstatuspage.teamspage_teams_filter()
        sleep(2)
        workstatuspage.teamspage_changeEmployeeStatus()
        sleep(2)
        # Teams Page End
        workstatuspage.driver_get_url(TestData.WORK_STATUS_INSIGHTS_URL)
        sleep(7)
        workstatuspage.insightspage_employeestatus_filter()
        stat2 = workstatuspage.get_element_text(WorkStatusPage.InsightsPage_Office_FirstDate)
        print('stat2: ', stat2)
        workstatuspage.insightspage_summary()

        assert stat1!=stat2

    # @pytest.mark.login
    def test_change_employee_status_visibility_in_userStatus(self):
        workstatuspage = WorkStatusPage(self.driver)
        sleep(3)
        workstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(7)
        workstatuspage.workstatuspage_teams_filter()
        sleep(2)
        employee_stat = workstatuspage.get_element_text(WorkStatusPage.WorkStatusPage_TeamMember_status)
        print("previous status value: ", employee_stat)
        workstatuspage.driver_get_url(TestData.WORK_STATUS_TEAMS_URL)
        sleep(7)
        workstatuspage.teamspage_teams_filter()
        sleep(2)
        workstatuspage.teamspage_changeEmployeeStatus(WorkStatusPage.TeamsPage_Employee_SecondStatus)
        sleep(2)
        workstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(7)
        workstatuspage.workstatuspage_teams_filter()
        sleep(2)
        employee_stat2 = workstatuspage.get_element_text(WorkStatusPage.WorkStatusPage_TeamMember_status)
        print("current status value: ", employee_stat)
        assert employee_stat != employee_stat2
        