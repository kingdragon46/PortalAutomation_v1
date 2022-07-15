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
    '''Header'''
    LOGOUT_DROPDOWN = (
        By.XPATH, "//*//*[@class='navigation-ProfileLink-l2Suz']")
    LOGOUT_BUTTON = (By.XPATH, "//*[text()='Logout']")
    TEAMS_NAV_LINK = (By.XPATH, "//*[@id='sub-nav']//*[text()='Teams']")

    '''Work Status Page'''
    WorkStatusPage_TeamsDropdown = (By.XPATH, "//*[@class='font-semibold'][text()='Teams']/..//div[@class='ant-select-selector']")
    WorkStatusPage_TeamsDropdown_Select = (By.XPATH, f"//*[@title='{TestData.TEAM_TO_BE_SELECTED}']")

    WorkStatusPage_TeamMember_status = (By.XPATH, "(//*[text()='Himanshi Sharma']/../..//*[@id='small-work-status-this-week-item']//*[@class='text-left']/p[2])[2]")

    # Date Filter WorkStatus Page
    WorkStatusPage_DateRange_StartDate = (By.XPATH, "//*[@placeholder='Start date']")
    WorkStatusPage_DateRange_StartDate = (By.XPATH, "//*[@placeholder='End date']")

    WorkStatusPage_MySchedule_NextDataRow = (By.XPATH, "//*[contains(@class,'ant-row bg-white shadow w-full hide-work-status-scrollbar')]//div[@id='small-work-status-this-week-item']")
    WorkStatusPage_MySchedule_FirstItem = (By.XPATH, "(//*[text()='My Schedule']/..//*[@id='small-work-status-this-week-item'])[1]")
    WorkStatusPage_MySchedule_Status_InOffice = (By.XPATH, "(//*[@class='p-1 hover:bg-coolGray-100 cursor-pointer'])[1]")
    WorkStatusPage_MySchedule_Status_WFH = (By.XPATH, "(//*[@class='p-1 hover:bg-coolGray-100 cursor-pointer'])[2]")
    WorkStatusPage_MySchedule_Status_NotWorking = (By.XPATH, "(//*[@class='p-1 hover:bg-coolGray-100 cursor-pointer'])[3]")

    ''' Teams Page '''
    TeamsPage_SelectTeamDropdown = (By.XPATH, "//*[@class='font-bold'][text()='Select Teams']/..//div[@class='ant-select-selector']")
    TeamsPage_SelectTeam = (By.CSS_SELECTOR, f"[title='{TestData.TeamsPage_Team}']")

    TeamsPage_UpdateStatus = (By.XPATH, "//button/*[text()='Update Status']")
    TeamsPage_UpdateStatus_SuccessMsg = (By.XPATH, "//*[text()='Status updated successfully!']")

    # TeamsPage grid
    TeamsPage_Employee_FirstStatus = (By.XPATH, f"//tr//td[text()='{TestData.TeamsPage_Employee}']/following-sibling::*[3]")
    TeamsPage_Employee_SecondStatus = (By.XPATH, f"//tr//td[text()='{TestData.TeamsPage_Employee}']/following-sibling::*[4]")
    TeamsPage_WFH = (By.XPATH, "//*[@class='ant-select-item-option-content'][contains(text(), 'Work From Home')]")
    TeamsPage_InOffice = (By.XPATH, "//*[@class='ant-select-item-option-content'][contains(text(), 'In-Office')]")
    TeamsPage_NotWorking = (By.XPATH, "//*[@class='ant-select-item-option-content'][contains(text(), 'Not Working')]")
    TeamsPage_Employee_CurrentStatus = (By.XPATH, f"//tr//td[text()='{TestData.TeamsPage_Employee}']/following-sibling::*[3]//*[@class='ant-select-selection-item']")
    TeamsPage_Employee_CurrentSecondStatus = (By.XPATH, f"//tr//td[text()='{TestData.TeamsPage_Employee}']/following-sibling::*[4]//*[@class='ant-select-selection-item']")

    ''' Work Insights Page '''
    InsightsPage_Office_FirstDate = (By.XPATH, "//*[text()='Bosch group']/../following-sibling::*/div[1]")
    InsightsPage_Teams_DropdownSelector = (By.XPATH, "//label[text()='Employee Status']/following-sibling::*")
    InsightsPage_EmployeeStatus_Dropdown = (By.XPATH, "//*[text()='Employee Status']/following-sibling::*")
    InsightsPage_WFH = (By.XPATH, "//*[@class='ant-select-item-option-content'][contains(text(), 'Work from Home')]")
    InsightsPage_InOffice = (By.XPATH, "//*[@class='ant-select-item-option-content'][contains(text(), 'In Office')]")
    InsightsPage_NotWorking = (By.XPATH, "//*[@class='ant-select-item-option-content'][contains(text(), 'Not working')]")
    # Summary
    InsightsPage_Summary_TotalEmployees_Count = (By.XPATH, "//*[text()='Total Employees']/following-sibling::*")
    InsightsPage_Summary_WFO_Percent = (By.XPATH, "//*[@id='card-content-view']//*[@class='font-semibold text-xs']/child::*[1]")
    InsightsPage_Summary_WFH_Percent = (By.XPATH, "//*[@id='card-content-view']//*[@class='font-semibold text-xs']/child::*[2]")
    InsightsPage_Summary_NW_Percent = (By.XPATH, "//*[@id='card-content-view']//*[@class='font-semibold text-xs']/child::*[3]")


    # --------------------------------------- Functions -----------------------------------------

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def workstatuspage_teams_filter(self):
        self.action_chain_click(self.WorkStatusPage_TeamsDropdown)
        self.action_chain_click(self.WorkStatusPage_TeamsDropdown_Select)

    def workstatuspage_date_range_filter(self):
        self.action_chain_click(self.WorkStatusPage_DateRange_StartDate)
        print("verify workstatuspage hover_over_status_tile: Passed")

    def workstatuspage_hover_over_status_tile(self):
        try:
            # sleep(12)
            next_datarow = self.is_visible(self.WorkStatusPage_MySchedule_NextDataRow)
            print("\nvisible: ", next_datarow)
            if next_datarow == True:
                self.hover_over_element(self.WorkStatusPage_MySchedule_FirstItem)
                sleep(4)
                print("clicking")
                # self.hover_click(self.MySchedule_Status_WFH)
                print("clicking2")
                stat = self.is_present(self.WorkStatusPage_MySchedule_Status_NotWorking)
                print("visible2: ", stat)
                self.action_chain_click(self.WorkStatusPage_MySchedule_Status_NotWorking)
            print("verify workstatuspage hover_over_status_tile: Passed")
        except Exception as e:
            print(f"Exception: {e}\n{traceback.format_exc()}")

    
    def teamspage_teams_filter(self):
        self.action_chain_click(self.TeamsPage_SelectTeamDropdown)
        self.action_chain_click(self.TeamsPage_SelectTeam)
        print("verify teams page teams filter: Passed")

    def teamspage_changeEmployeeStatus(self, by_locator=None):
        if by_locator == None:
            ele1 = self.get_element(self.TeamsPage_Employee_CurrentStatus)
            title1 = ele1.get_attribute('title')
            print("title1: ", title1)
            self.action_chain_click(self.TeamsPage_Employee_FirstStatus)
        else:
            ele1 = self.get_element(self.TeamsPage_Employee_CurrentSecondStatus)
            title1 = ele1.get_attribute('title')
            print("title1: ", title1)
            self.action_chain_click(by_locator)
        print('click')
        if "In-Office" in title1 :
            self.action_chain_click(self.TeamsPage_WFH)
        if "Work From Home" in title1 :
            self.action_chain_click(self.TeamsPage_InOffice)
        if "Not working" in title1 :
            self.action_chain_click(self.TeamsPage_InOffice)
        self.action_chain_click(self.TeamsPage_UpdateStatus)
        sleep(2)
        success_msg = self.is_visible(self.TeamsPage_UpdateStatus_SuccessMsg)
        print("verify every confirmation msg: Passed")
        assert success_msg == True
        if by_locator == None:
            ele2 = self.get_element(self.TeamsPage_Employee_CurrentStatus)
            title2 = ele2.get_attribute('title')
            print("title2: ", title2)
        else:
            ele1 = self.get_element(self.TeamsPage_Employee_CurrentSecondStatus)
            title1 = ele1.get_attribute('title')
            print("title1: ", title1)
            self.action_chain_click(by_locator)
        print("verify teams page employee status filter: Passed")

    def insightspage_employeestatus_filter(self, stat=None):
        self.action_chain_click(self.InsightsPage_EmployeeStatus_Dropdown)
        if stat == 1 or stat is None:
            self.action_chain_click(self.InsightsPage_InOffice)
        if stat == 2:
            self.action_chain_click(self.InsightsPage_WFH)
        if stat == 3:
            self.action_chain_click(self.InsightsPage_NotWorking)
        print("verify insights page employee status filter: Passed")

    def insightspage_summary(self):
        employee_count = self.get_element_text(self.InsightsPage_Summary_TotalEmployees_Count)
        print("Employee Count: ", employee_count)
        summary_wfo_percent = self.get_element_text(self.InsightsPage_Summary_WFO_Percent)
        print("summary_wfo_percent: ", summary_wfo_percent)
        summary_wfh_percent = self.get_element_text(self.InsightsPage_Summary_WFH_Percent)
        print("summary_wfh_percent: ", summary_wfh_percent)
        summary_nw_percent = self.get_element_text(self.InsightsPage_Summary_NW_Percent)
        print("summary_nw_percent: ", summary_nw_percent)

    def logout(self):
        self.action_chain_click(self.LOGOUT_DROPDOWN)
        self.action_chain_click(self.LOGOUT_BUTTON)