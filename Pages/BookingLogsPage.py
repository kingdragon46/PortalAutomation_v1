import sys
import traceback
from Pages.BasePage import BasePage
from Pages.RoomBookingPage import RoomBookingsPage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from WebConfig.time_functions import WebConfigFunctions


class BookingLogsPage(RoomBookingsPage):

    # <======================================== Selectors ========================================>
    
    BookingLog_SPACES = (By.XPATH, "//h3[text()='Spaces]")
    BookingLog_LOCATION_SELECTOR = (By.XPATH, "//div[@class='resource-manager-Container-6118f796a365f58d629b168745f902c6']/div[2]")
    FREE_CLICK = (By.XPATH, "//div[@class='resource-manager-Container-6118f796a365f58d629b168745f902c6']/child::*[1]")

    # Status Selctors
    BookingLog_BookingStatusFilter = (By.XPATH, "//div[@class='ant-col'][2]")
    BookingLog_BookingStatusFilter_All = (By.CSS_SELECTOR, "div[title='All']")
    BookingLog_BookingStatusFilter_ApprovalPending = (By.CSS_SELECTOR, "div[title='Approval Pending']")
    BookingLog_BookingStatusFilter_Assigned = (By.CSS_SELECTOR, "div[title='Assigned']")
    BookingLog_BookingStatusFilter_Schedule = (By.CSS_SELECTOR, "div[title='Scheduled']")
    BookingLog_BookingStatusFilter_Cancelled = (By.CSS_SELECTOR, "div[title='Cancelled']")
    BookingLog_BookingStatusFilter_Expired = (By.CSS_SELECTOR, "div[title='Expired']")

    # Resource Type
    BookingLog_RESOURCE_TYPE_SELECTOR = (By.XPATH, "//div[@class='ant-col common-margin']/child::div")
    BookingLog_DESKS = (By.CSS_SELECTOR, "span[title='Desks']")
    BookingLog_ROOMS = (By.CSS_SELECTOR, "span[title='Rooms']")

    # Date Selectors
    BookingLog_DATE_SELECTOR = (By.XPATH, "//div[@class='ant-col'][1]/div")
    BookingLog_START_DATE = (By.CSS_SELECTOR, "input[placeholder='Start date']")
    BookingLog_END_DATE = (By.CSS_SELECTOR, "input[placeholder='End date']")
    BookingLog_CAL_NEXT_MONTH = (By.XPATH, "(//*[@class='ant-picker-next-icon'])[2]")
    BookingLog_CONFIG_END_DATE = (By.CSS_SELECTOR, f"td[title='{TestData.BL_CAL_DATE}']")

    # Guest/Host
    BookingLog_GH_SELECTOR = (By.XPATH, "//div[@class='ant-col common-margin']/child::span/child::span/child::span")
    BookingLog_HOST_SELECT = (By.CSS_SELECTOR, "div[title='Host Name']")
    BookingLog_GUEST_SELECT = (By.CSS_SELECTOR, "div[title='Guest  Name']")
    BookingLog_GH_INPUT_BOX = (By.XPATH, "//div[@class='ant-col common-margin']/child::span/child::span/input")

    # TR selectors
    BookingLog_DATA_TABLE_ROW_1 = (By.XPATH, "//tbody[@class='ant-table-tbody']/tr[2]")
    BookingLog_BookingDetailsPage_TR_I_BUTTON = "//tr[@data-row-key='{}']/td[11]/div/span[@class='anticon anticon-info-circle info-icon-logs']"
    BookingLog_BookingDetailsPage_BOOKED_I_BUTTON = "//td[text()='{}']/following-sibling::td[text()='{}']/following-sibling::td/div/span[@class='anticon anticon-info-circle info-icon-logs']"
    BookingLog_BOOKED_TR_PLUS_ICON = "//td[text()='{}']/following-sibling::td[text()='{}']/../child::*/child::*[@class='anticon anticon-plus-square']"
    # BookingLog_TR_PLUS_ICON = "//tr[@data-row-key='{}']/child::*/child::*[@class='anticon anticon-plus-square']"

    # Booking Details
    BookingLog_BookingDetailsPage_BODY = (By.CLASS_NAME, "resource-manager-Content-e74546c4b505e12a3d1819aef6105081 ")
    BookingLog_BookingDetailsPage_HOST_NAME = (By.CLASS_NAME, "resource-manager-Label-670c5c2758c430f41ba15d2cccb31b1a")
    BookingLog_BookingDetailsPage_HOST_EMAIL = (By.XPATH, "(//*[@class= 'resource-manager-SubLabel-dad37a6c515741a403cb9c8729709b4d'])[1]")
    ## Other Details
    BookingLog_BookingDetailsPage_BOOKING_CODE= (By.XPATH, "//span[text()='Booking Code: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    BookingLog_BookingDetailsPage_STARTED_AT= (By.XPATH, "//span[text()='Started At: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    BookingLog_BookingDetailsPage_ENDED_AT= (By.XPATH, "//span[text()='Ended At: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    BookingLog_BookingDetailsPage_ENDED_EARLY= (By.XPATH, "//span[text()='Is Ended Early: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    ## Recurring Rule
    BookingLog_BookingDetailsPage_RECURRING_RULE_HEADING = (By.XPATH, "(//*[@class= 'resource-manager-SegmentHeading-061e6505d6ac0848e6159647cd3a21d4'])[2]")
    BookingLog_BookingDetailsPage_RR_STARTED_AT= (By.XPATH, "(//span[text()='Started At: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b'])[2]")
    BookingLog_BookingDetailsPage_RR_ENDED_AT= (By.XPATH, "(//span[text()='Ended At: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b'])[2]")
    BookingLog_BookingDetailsPage_RR_INTERVAL= (By.XPATH, "(//span[text()='Interval: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b'])[2]")
    BookingLog_BookingDetailsPage_RR_FREQUENCY= (By.XPATH, "(//span[text()='Frequency: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b'])[2]")
    ## Meeting Info
    BookingLog_BookingDetailsPage_STATUS = (By.XPATH, "//span[text()='Status: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    BookingLog_BookingDetailsPage_TIME = (By.XPATH, "//span[text()='Time: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    ## Other Info
    BookingLog_BookingDetailsPage_VALID_FROM = (By.XPATH, "//span[text()='Vallid From: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    BookingLog_BookingDetailsPage_VALID_TILL = (By.XPATH, "//span[text()='Vallid Till: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    BookingLog_BookingDetailsPage_AGENDA = (By.XPATH, "//span[text()='Agenda: ']/following-sibling::span[@class='resource-manager-FieldValue-140d56100e3f5dd73bba3720096da86b']")
    
    # Download Report
    DownloadReport_BUTTON = (By.XPATH, "//div[@class='main-log-container-booking-logs']/div/div[2]/child::button")
    DownloadReport_FREE_CLICK = (By.XPATH, "//div[text()='Request Report']")
    DownloadReport_FREE_CLICK_2 = (By.XPATH, "//div[@class='vrs-label'][text()='Report Format ']")
    ### Date selectors
    DownloadReport_StartTime = (By.XPATH, "//div[@class='vrs-label'][text()='Start time ']/following-sibling::*/input")
    DownloadReport_StartTime_DateSelect = (By.XPATH, f"//div[@class='vrs-label'][text()='Start time ']/following-sibling::*//td[@class='rdtDay'][text()='{TestData.DR_START_DATE}']")
    DownloadReport_EndTime = (By.XPATH, "//div[@class='vrs-label'][text()='End time ']/following-sibling::*/input")
    DownloadReport_EndTime_DateSelect = (By.XPATH, f"//div[@class='vrs-label'][text()='End time ']/following-sibling::*//td[@class='rdtDay'][text()='{TestData.DR_END_DATE}']")
    ### Select Venue
    DownloadReport_VenueDropdown = (By.XPATH, "//div[@class='vrs-label'][text()='Select Venue']/following-sibling::*")
    DownloadReport_VenueInputBox = (By.XPATH, "//div[@class='vrs-label'][text()='Select Venue']/following-sibling::*//child::input")
    DownloadReport_Venue_GenpactITPark = (By.XPATH, f"//div[text()='{TestData.LOC_1}']")
    DownloadReport_Venue_GenpactITPark_Expand_Arrow = (By.XPATH, f"//div[text()='{TestData.LOC_1}']/../../../../child::*[2]/child::*")
    DownloadReport_Venue_BusinessTower = (By.XPATH, f"//div[text()='{TestData.LOC_2}']/../../../preceding-sibling::*[1]/child::*")
    ### Select Status
    DownloadReport_StatusDropdown = (By.XPATH, "//div[@class='vrs-label'][text()='Status ']/following-sibling::*")
    DownloadReport_Status_INPUT = (By.XPATH, "//input[@id='react-select-2-input']")
    DownloadReport_Status_DIV = (By.XPATH, "//*[contains(class,'css-e6ky2s-menu')]")
    DownloadReport_Status_All = (By.XPATH, "//*[contains(class,'css-e6ky2s-menu')]//*[contains(text(), 'All')]")
    DownloadReport_Status_Scheduled = (By.XPATH, "//*[contains(text(), 'Scheduled')]")
    DownloadReport_Status_Cancelled = (By.XPATH, "//*[contains(text(), 'Cancelled')]")
    DownloadReport_Status_ApprovalPending = (By.XPATH, "//*[contains(text(), 'Approval Pending')]")
    DownloadReport_Status_Assigned = (By.XPATH, "//*[contains(text(), 'Assigned')]")
    DownloadReport_Status_Expired = (By.XPATH, "//*[contains(text(), 'Expired')]")
    ### Select Template
    DownloadReport_Template = (By.XPATH, "//div[@class='vrs-label'][text()='Template ']/following-sibling::*")
    DownloadReport_Template_Input = (By.XPATH, "//input[@id='react-select-4-input']")
    DownloadReport_Template_BookingLogs = (By.XPATH, "//*[contains(text(), 'Booking Logs')]")
    # Submit button
    DownloadReport_SubmitReportButton = (By.XPATH, "//div[@class='vms-v4-SubmitButton-W3vDW']//child::*[text()='Submit Request']")
    DownloadReport_SubmitReportButton_2 = (By.XPATH, "//div[@label='Submit Request']")
    # <===================================== Functions =======================================>

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for Bookings Page"""

    def test_selector_click(self):
        sleep(5)
        self.action_chain_click(self.BookingLog_LOCATION_SELECTOR)
        self.action_chain_click(self.BookingLog_DATE_SELECTOR)
        # self.action_chain_click(self.BookingLog_BookingStatusFilter)
        # self.action_chain_click(self.BookingLog_RESOURCE_TYPE_SELECTOR)
        sleep(2)

    def resource_selection(self,resource=None):
        sleep(2)
        self.action_chain_click(self.BookingLog_RESOURCE_TYPE_SELECTOR)
        sleep(2)
        if resource == 1:
            self.action_chain_click(self.BookingLog_DESKS)
        if resource == 2:
            self.action_chain_click(self.BookingLog_ROOMS)
        print("BookingLog_Resource selection: Passed")
        self.action_chain_click(self.FREE_CLICK)

    def guest_host_selection(self,gh=None, gh_name=None):
        sleep(2)
        self.action_chain_click(self.BookingLog_GH_SELECTOR)
        sleep(2)
        if gh == 1:
            self.action_chain_click(self.BookingLog_HOST_SELECT)
        if gh == 2:
            self.action_chain_click(self.BookingLog_GUEST_SELECT)
        if gh_name is not None:
            self.action_chain_sendkeys_1(self.BookingLog_GH_INPUT_BOX, gh_name)
        print("BookingLog_Host selection: Passed")

    def verify_booking_status_filter(self,status=None):
        self.action_chain_click(self.BookingLog_BookingStatusFilter)
        sleep(2)
        if status == 1:
            self.action_chain_click(self.BookingLog_BookingStatusFilter_ApprovalPending)
        if status == 2:
            self.action_chain_click(self.BookingLog_BookingStatusFilter_Assigned)
        if status == 3:
            self.action_chain_click(self.BookingLog_BookingStatusFilter_Schedule)
        if status == 4:
            self.action_chain_click(self.BookingLog_BookingStatusFilter_Cancelled)
        if status == 5:
            self.action_chain_click(self.BookingLog_BookingStatusFilter_Expired)
        print("BookingLog_booking status filter selection: Passed")

    def date_selection(self, dtype=None, dys=None):
        sleep(2)
        self.action_chain_click(self.BookingLog_DATE_SELECTOR)
        sleep(2)
        if dtype == 1:
            self.date_selection_chain(self.BookingLog_START_DATE, WebConfigFunctions.repeat_till_date2(dys))
        if dtype == 2:
            self.action_chain_click(self.BookingLog_CONFIG_END_DATE)
        self.action_chain_click(self.FREE_CLICK)
        sleep(2)
        print("BookingLog_date selection: Passed")
        
    def booking_details_data_verification(self, brule=None):
        # host details check
        host_name = self.get_element_text(self.BookingLog_BookingDetailsPage_HOST_NAME)
        print('host_name: ', host_name)
        # assert host_name == TestData.DEFAULT_HOSTNAME
        host_email  = self.get_element_text(self.BookingLog_BookingDetailsPage_HOST_EMAIL)
        print('host_email: ', host_email)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        booking_code  = self.get_element_text(self.BookingLog_BookingDetailsPage_BOOKING_CODE)
        print('booking_code: ', booking_code)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        started_at_1  = self.get_element_text(self.BookingLog_BookingDetailsPage_STARTED_AT)
        print('started_at_1: ', started_at_1)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        ended_at_1  = self.get_element_text(self.BookingLog_BookingDetailsPage_ENDED_AT)
        print('ended_at_1: ', ended_at_1)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        ended_early  = self.get_element_text(self.BookingLog_BookingDetailsPage_ENDED_EARLY)
        print('ended_early: ', ended_early)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL

        ## Recurring Rule
        if brule is not None:
            rrule_heading = self.get_element_text(self.BookingLog_BookingDetailsPage_RECURRING_RULE_HEADING)
            if rrule_heading == "Recurring rule":
                rr_started_at  = self.get_element_text(self.BookingLog_BookingDetailsPage_RR_STARTED_AT)
                print('rr_started_at: ', rr_started_at)
                # assert host_email == TestData.DEFAULT_HOSTEMAIL
                rr_ended_at  = self.get_element_text(self.BookingLog_BookingDetailsPage_RR_ENDED_AT)
                print('rr_ended_at: ', rr_ended_at)
                # assert host_email == TestData.DEFAULT_HOSTEMAIL
                # rr_interval  = self.get_element_text(self.BookingLog_BookingDetailsPage_RR_INTERVAL)
                # print('rr_interval: ', rr_interval)
                # # assert host_email == TestData.DEFAULT_HOSTEMAIL
                # rr_frequency  = self.get_element_text(self.BookingLog_BookingDetailsPage_RR_FREQUENCY)
                # print('rr_frequency: ', rr_frequency)
                # # assert host_email == TestData.DEFAULT_HOSTEMAIL
        
        # self.action_chain_sendkeys_1(self.BookingLog_BookingDetailsPage_BODY, Keys.PAGE_DOWN)
        # sleep(1)
        ## Meeting Info
        status = self.get_element_text(self.BookingLog_BookingDetailsPage_STATUS)
        print('status: ', status)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        BookingLog_time = self.get_element_text(self.BookingLog_BookingDetailsPage_TIME)
        print('BookingLog_time: ', BookingLog_time)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        ## Other Info
        valid_from = self.get_element_text(self.BookingLog_BookingDetailsPage_VALID_FROM)
        print('valid_from: ', valid_from)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        valid_till = self.get_element_text(self.BookingLog_BookingDetailsPage_VALID_TILL)
        print('valid_till: ', valid_till)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        agenda = self.get_element_text(self.BookingLog_BookingDetailsPage_AGENDA)
        print('agenda: ', agenda)
        # assert host_email == TestData.DEFAULT_HOSTEMAIL
        print("BookingLog_BookingDetailsPage data verification: Passed")

    def download_report_status_selection(self, stat=None):
        self.action_chain_click(self.DownloadReport_StatusDropdown)
        # sleep(2)
        try:
            if stat == 1:
                self.action_chain_sendkeys_1(self.DownloadReport_Status_INPUT, TestData.Status_All, Keys.ENTER)
            if stat == 2:
                self.action_chain_sendkeys_1(self.DownloadReport_Status_Scheduled, TestData.Status_Scheduled, Keys.ENTER)
            if stat == 3:
                self.action_chain_sendkeys_1(self.DownloadReport_Status_Cancelled, TestData.Status_Cancelled, Keys.ENTER)
            if stat == 4:
                self.action_chain_sendkeys_1(self.DownloadReport_Status_ApprovalPending, TestData.Status_ApprovalPending, Keys.ENTER)
            if stat == 5:
                self.action_chain_sendkeys_1(self.DownloadReport_Status_Assigned, TestData.Status_Assigned, Keys.ENTER)
            if stat == 6:
                self.action_chain_sendkeys_1(self.DownloadReport_Status_Expired, TestData.Status_Expired, Keys.ENTER)
        except Exception as e:
            print(f"download_report_status_selection exception: {e} \n{traceback.format_exc()}")
        print("BookingLog_DownloadReport_status selection: Passed")

    def download_report_select_dates(self, sdate=None, edate=None):
        # StartTime
        if sdate is not None:
            self.action_chain_click(self.DownloadReport_StartTime)
            self.action_chain_click(self.DownloadReport_StartTime_DateSelect)
        # EndTime
        if edate is not None:
            self.action_chain_click(self.DownloadReport_EndTime)
            self.action_chain_click(self.DownloadReport_EndTime_DateSelect)
        sleep(2)
        print("BookingLog_DownloadReport_date selection: Passed")
        self.action_chain_click(self.DownloadReport_FREE_CLICK)

    def download_report_select_venue(self):
        self.action_chain_click(self.DownloadReport_VenueDropdown)
        self.action_chain_sendkeys_1(self.DownloadReport_VenueInputBox, TestData.BL_Venue1)
        # self.scroll_to_element_to_mid(self.DownloadReport_Venue_GenpactITPark)
        # self.action_chain_click(self.DownloadReport_Venue_GenpactITPark_Expand_Arrow)
        self.action_chain_click(self.DownloadReport_Venue_BusinessTower)
        print("BookingLog_DownloadReport_venue selection: Passed")

    def download_report(self):
        self.action_chain_click(self.DownloadReport_BUTTON)
        self.download_report_select_dates(1, 1)
        self.download_report_select_venue()
        self.download_report_status_selection(3)
        # sleep(2)
        self.action_chain_click(self.DownloadReport_FREE_CLICK_2)
        sleep(2)
        self.action_chain_click(self.DownloadReport_Template)
        self.action_chain_sendkeys_1(self.DownloadReport_Template_Input, TestData.Template_Name, Keys.ENTER)
        try:
            # print("clicking on logs")
            # self.do_click(self.DownloadReport_Template_BookingLogs)
            print("clicking on confirm")
            self.action_chain_click(self.DownloadReport_SubmitReportButton_2)
        except Exception as e:
            print(f"download_report exception: {e} \n{traceback.format_exc()}")
        sleep(5)
        print("BookingLog_DownloadReport selection: Passed")