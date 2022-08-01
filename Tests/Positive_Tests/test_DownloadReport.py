import json
from time import time, sleep
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from Pages.LoginPage import LoginPage
from Pages.DownloadReportsPage import DownloadReportsPage
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

    # Login
    @pytest.mark.selected
    @pytest.mark.login
    def test_login(self):
        try:
            self.loginPage = LoginPage(self.driver)
            login_page = self.loginPage.do_rlogin(
                        TestData.USER_NAME, TestData.PASSWORD)
        except Exception as e:
            print("download login error: ", e)
    
    @pytest.mark.selected
    def test_status_all_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_status(1)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_status_tr_value)))
        print("results: ", results_num)

        if results_num > 0:
            print("Table populated results: ", results_num)
        else:
            print("Table was empty. No results to show")
        sleep(2)
    
    @pytest.mark.selected
    def test_status_processing_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_status(2)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_status_tr_value)))
        print("results: ", results_num)

        if results_num > 0:
            for i in range(1,results_num):
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_status_tr_value}[{i}]")
                assert eltext == "Processing"
        else:
            print("Table was empty. No results to show")
        sleep(2)
    
    @pytest.mark.selected
    def test_status_completed_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_status(3)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_status_tr_value)))
        print("results: ", results_num)

        if results_num > 0:
            for i in range(1,results_num):
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_status_tr_value}[{i}]")
                assert eltext == "Complete"
        else:
            print("Table was empty. No results to show")
        sleep(2)
    
    @pytest.mark.selected
    def test_status_failed_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_status(4)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_status_tr_value)))
        print("results: ", results_num)

        if results_num > 0:
            for i in range(1,results_num):
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_status_tr_value}[{i}]")
                assert eltext == "Failed"
        else:
            print("Table was empty. No results to show")
        sleep(2)
    
    @pytest.mark.skip
    def test_status_cancelled_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_status(5)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_status_tr_value)))
        print("results: ", results_num)

        if results_num > 0:
            for i in range(1,results_num):
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_status_tr_value}[{i}]")
                assert eltext == "Cancelled"
        else:
            print("Table was empty. No results to show")
        sleep(2)
    
    @pytest.mark.selected
    def test_module_all_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_module(1)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_tr_name_value)))
        print("results: ", results_num)
    
    @pytest.mark.selected
    def test_module_vms_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_module(2)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_tr_name_value)))
        print("results: ", results_num)
        
        if results_num > 0:
            print("in if")
            for i in range(1,results_num):
                print("in for")
                print(f"{DownloadReportsPage.Table_tr_name_value}[{i}]")
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_tr_name_value}[{i}]")
                print(f"{i}. eltext: {eltext}")
                assert eltext in ["Invites Report", "Activity Report"]
        else:
            print("Table was empty. No results to show")
        sleep(2)
    
    @pytest.mark.selected
    def test_module_members_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_module(3)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_tr_name_value)))
        print("results: ", results_num)
        
        if results_num > 0:
            print("in if")
            for i in range(1,results_num):
                print("in for")
                print(f"{DownloadReportsPage.Table_tr_name_value}[{i}]")
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_tr_name_value}[{i}]")
                print(f"{i}. eltext: {eltext}")
                assert eltext in ["Members Report"]
        else:
            print("Table was empty. No results to show")
        sleep(2)
    
    @pytest.mark.selected
    def test_module_bookings_selector(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_module(4)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_tr_name_value)))
        print("results: ", results_num)
        
        if results_num > 0:
            print("in if")
            for i in range(1,results_num):
                print("in for")
                print(f"{DownloadReportsPage.Table_tr_name_value}[{i}]")
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_tr_name_value}[{i}]")
                print(f"{i}. eltext: {eltext}")
                assert eltext in ["Bookings Report"]
        else:
            print("Table was empty. No results to show")
        sleep(2)
    
    @pytest.mark.selected
    def test_date_select_filters(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_startdate()

        downloadreport.select_enddate()

        sleep(5)

    # @pytest.mark.selected
    def test_status_module_date_combo(self):
        downloadreport = DownloadReportsPage(self.driver)
        sleep(3)
        downloadreport.driver_get_url(TestData.DOWNLOAD_REPORTS_URL)
        sleep(3)

        downloadreport.select_startdate()

        downloadreport.select_enddate()

        downloadreport.select_module(2)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_tr_name_value)))
        print("results: ", results_num)
        
        if results_num > 0:
            print("in if")
            for i in range(1,results_num):
                print("in for")
                print(f"{DownloadReportsPage.Table_tr_name_value}[{i}]")
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_tr_name_value}[{i}]")
                print(f"{i}. eltext: {eltext}")
                assert eltext in ["Invites Report", "Activity Report"]
        else:
            print("Table was empty. No results to show")
        sleep(2)

        downloadreport.select_status(3)

        results_num = len(downloadreport.get_elements((By.XPATH, DownloadReportsPage.Table_status_tr_value)))
        print("results: ", results_num)

        if results_num > 0:
            for i in range(1,results_num):
                eltext = downloadreport.get_element_text_by_xpath(f"{DownloadReportsPage.Table_status_tr_value}[{i}]")
                assert eltext == "Complete"
        else:
            print("Table was empty. No results to show")
        sleep(2)