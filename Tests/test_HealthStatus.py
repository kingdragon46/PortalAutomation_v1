from time import sleep
import logging

from selenium.webdriver.common.keys import Keys
from Pages.LoginPage import LoginPage
from Pages.HealthStatusPage import HealthStatusPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest
from selenium.webdriver.common.by import By

from mail_conf import send_email

import traceback

class Test_HealthStatus(BaseTest):

    @pytest.mark.custom
    @pytest.mark.healthstat
    @pytest.mark.login
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        healthstatuspage = self.loginPage.do_login(
            TestData.USER_NAME, TestData.PASSWORD)

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    def test_health_status_case1(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        try:
            healthstatuspage.negative_test_health_status(1)
            error_msg = healthstatuspage.get_element_text(HealthStatusPage.HS_ERROR_MSG)
            assert TestData.HS_Error_msg in error_msg
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    def test_health_status_case2(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        try:
            healthstatuspage.negative_test_health_status(2)
            healthstatuspage.action_chain_click(HealthStatusPage.HS_Refresh_Div_2)
            sleep(5)
            button_txt = healthstatuspage.get_element_text(HealthStatusPage.HS_WS_UPDATE_HEALTH_STATUS_BUTTON)
            assert button_txt == TestData.HS_Reassess
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    def test_health_status_case3(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        try:
            healthstatuspage.negative_test_health_status(3)
            healthstatuspage.action_chain_click(HealthStatusPage.HS_Refresh_Div_2)
            sleep(5)
            button_txt = healthstatuspage.get_element_text(HealthStatusPage.HS_WS_UPDATE_HEALTH_STATUS_BUTTON)
            assert button_txt == TestData.HS_Reassess
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    def test_health_status_case4(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        try:
            healthstatuspage.negative_test_health_status(4)
            healthstatuspage.action_chain_click(HealthStatusPage.HS_Refresh_Div_2)
            sleep(5)
            button_txt = healthstatuspage.get_element_text(HealthStatusPage.HS_WS_UPDATE_HEALTH_STATUS_BUTTON)
            assert button_txt == TestData.HS_Reassess
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    @pytest.mark.login
    def test_health_status_case5(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        try:
            healthstatuspage.negative_test_health_status(5)
            healthstatuspage.action_chain_click(HealthStatusPage.HS_Refresh_Div_2)
            sleep(5)
            button_txt = healthstatuspage.get_element_text(HealthStatusPage.HS_WS_UPDATE_HEALTH_STATUS_BUTTON)
            assert button_txt == TestData.HS_Reassess
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # assert False

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    def test_health_status_case6(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        try:
            healthstatuspage.negative_test_health_status(6)
            error_msg = healthstatuspage.get_element_text(HealthStatusPage.HS_ERROR_MSG)
            assert TestData.HS_Error_msg in error_msg
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    def test_health_status_case7(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        try:
            healthstatuspage.negative_test_health_status(7)
            error_msg = healthstatuspage.get_element_text(HealthStatusPage.HS_ERROR_MSG)
            assert TestData.HS_Error_msg in error_msg
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    def test_health_status_case8(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        try:
            healthstatuspage.negative_test_health_status(8)
            error_msg = healthstatuspage.get_element_text(HealthStatusPage.HS_ERROR_MSG)
            assert TestData.HS_Error_msg in error_msg
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.xpass(reason="The test is expected to fail as stesting negative health status update cases")
    @pytest.mark.healthstat
    # @pytest.mark.login
    def test_health_status_case9(self):
        healthstatuspage = HealthStatusPage(self.driver)
        sleep(3)
        healthstatuspage.driver_get_url(TestData.WORK_STATUS_USERSTATUS_URL)
        sleep(3)
        # with pytest.raises(Exception) as e_info:
        try:
            healthstatuspage.negative_test_health_status(9)
            error_msg = healthstatuspage.get_element_text(HealthStatusPage.HS_ERROR_MSG)
            assert TestData.HS_Error_msg in error_msg
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            healthstatuspage.take_screenshot(f"HealthStatusPage/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")