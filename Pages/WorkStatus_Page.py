import sys
import traceback
from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import traceback, sys


class WorkStatusPage(BasePage):
    TeamsDropdown = (By.XPATH, "//*[@class='font-semibold'][text()='Teams']/..//div[@class='ant-select-selector']")
    TeamsDropdown_Select = (By.XPATH, f"//*[@title='{TestData.TEAM_TO_BE_SELECTED}']")

    DateRange_StartDate = (By.XPATH, "//*[@placeholder='Start date']")
    DateRange_StartDate = (By.XPATH, "//*[@placeholder='End date']")

    MySchedule_NextDataRow = (By.XPATH, "//*[contains(@class,'ant-row bg-white shadow w-full hide-work-status-scrollbar')]//div[@id='small-work-status-this-week-item']")
    MySchedule_FirstItem = (By.XPATH, "(//*[text()='My Schedule']/..//*[@id='small-work-status-this-week-item'])[1]")
    MySchedule_Status_InOffice = (By.XPATH, "(//*[@class='p-1 hover:bg-coolGray-100 cursor-pointer'])[1]")
    MySchedule_Status_WFH = (By.XPATH, "(//*[@class='p-1 hover:bg-coolGray-100 cursor-pointer'])[2]")
    MySchedule_Status_NotWorking = (By.XPATH, "(//*[@class='p-1 hover:bg-coolGray-100 cursor-pointer'])[3]")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def hover_over_status_tile(self):
        try:
            # sleep(12)
            next_datarow = self.is_visible(self.MySchedule_NextDataRow)
            print("\nvisible: ", next_datarow)
            if next_datarow == True:
                self.hover_over_element(self.MySchedule_FirstItem)
                sleep(4)
                print("clicking")
                # self.hover_click(self.MySchedule_Status_WFH)
                print("clicking2")
                stat = self.is_present(self.MySchedule_Status_WFH)
                print("visible2: ", stat)
                self.action_chain_click(self.MySchedule_Status_WFH)
        except Exception as e:
            print(f"Exception: {e}\n{traceback.format_exc()}")