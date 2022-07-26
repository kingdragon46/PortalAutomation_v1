import sys
import traceback
from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from WebConfig.time_functions import WebConfigFunctions as Config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import traceback, sys


class DownloadReportsPage(BasePage):

    # Status Dropdown
    Status_dropdown = (By.XPATH, "//*[@class='download-center-Label-zULWb'][text()='Status']/following-sibling::*//*[@class='ant-select-selector']")
    Status_selector_All = (By.CSS_SELECTOR, "*[title='All']")
    Status_selector_Processing = (By.CSS_SELECTOR, "*[title='Processing']")
    Status_selector_Completed = (By.CSS_SELECTOR, "*[title='Completed']")
    Status_selector_Failed = (By.CSS_SELECTOR, "*[title='Failed']")
    Status_selector_Cancelled = (By.CSS_SELECTOR, "*[title='Cancelled']")

    # Module Dropdown
    Module_dropdown = (By.XPATH, "//*[@class='download-center-Label-zULWb'][text()='Module']/following-sibling::*//*[@class='ant-select-selector']")
    Module_selector_All = (By.CSS_SELECTOR, "*[title='All']")
    Module_selector_VMS = (By.CSS_SELECTOR, "*[title='VMS']")
    Module_selector_Members = (By.CSS_SELECTOR, "*[title='Members']")
    Module_selector_Bookings = (By.CSS_SELECTOR, "*[title='Bookings']")

    # Date Selectors
    Date_select_startdate = (By.CSS_SELECTOR, "*[placeholder='Start date']")
    Date_select_enddate = (By.CSS_SELECTOR, "*[placeholder='End date']")
    Date_select_specific_sdate = (By.XPATH, f"//*[contains(@class,'ant-picker-cell-in-view')][@title='{Config.repeat_till_date2(-1)}']")
    Date_select_specific_edate = (By.XPATH, f"//*[contains(@class,'ant-picker-cell-in-view')][@title='{Config.repeat_till_date2(10)}']")

    # Table Selectors
    Table_status_tr_value = "(//tr/td[5]//*[@class='download-center-Name-3N7W9'])"
    Table_tr_name_value = "(//tr/td[1]//*[@class='download-center-Name-3N7W9'])"



    # <<=========================================================== Functions ======================================================>>

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for Download Report Page"""

    def select_status(self, stat=None):
        self.action_chain_click(self.Status_dropdown)
        if stat == 1 or None:
            self.action_chain_click(self.Status_selector_All)
        if stat == 2:
            self.action_chain_click(self.Status_selector_Processing)
        if stat == 3:
            self.action_chain_click(self.Status_selector_Completed)
        if stat == 4:
            self.action_chain_click(self.Status_selector_Failed)
        if stat == 5:
            self.action_chain_click(self.Status_selector_Cancelled)
        sleep(5)

    def select_module(self, stat=None):
        self.action_chain_click(self.Module_dropdown)
        if stat == 1 or None:
            self.action_chain_click(self.Module_selector_All)
        if stat == 2:
            self.action_chain_click(self.Module_selector_VMS)
        if stat == 3:
            self.action_chain_click(self.Module_selector_Members)
        if stat == 4:
            self.action_chain_click(self.Module_selector_Bookings)
        sleep(5)

    def select_startdate(self):
        self.action_chain_click(self.Date_select_startdate)
        self.action_chain_click(self.Date_select_specific_sdate)

    def select_enddate(self):
        self.action_chain_click(self.Date_select_enddate)
        self.action_chain_click(self.Date_select_specific_edate)