from itertools import count
import sys
import traceback
from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import traceback
import sys


class InvitesPage(BasePage):
    # Links
    Invites_Link = (By.XPATH, "//a[contains(text(),'Invites')]")
    # Headers
    Single_invite_link = (By.XPATH, "//div[contains(text(),'Single Visitor')]")
    InvitesList_link = (By.XPATH, "//div[contains(text(),'Invites List')]")
    MultipleVisitors_link = (By.XPATH, "//div[contains(text(),'Multiple Visitors')]")
    InvitesList_VisitorInvites_header = (By.XPATH, "//*[@class='vms-v4-Container-ENphv']//h2")
    InviteDetails_heading = (By.XPATH, "//*[@class='vms-v4-Heading-E2X5i']")

    '''---------Single Invite Details------------'''

    SingleInvite_InviteVenue_dropdown = (
        By.XPATH, "//div[contains(text(),'Invite Venue *')]/following-sibling::*//*[@class='ant-select-selector']")
    # Dates
    # # Start Date
    SingleInvite_StartsAt_input = (By.XPATH, "//div[contains(text(),'Starts At *')]/following-sibling::*//input")
    SingleInvite_StartDate_select = "(//td[@data-value='{}'][not(contains(@class,'rdtDisabled'))])[1]"
    SingleInvite_StartDate_presentDate = (By.XPATH, "(//td[contains(@class,'rdtToday')])[1]")
    SingleInvite_StartDate_NextMonth = (By.XPATH, "(//th[contains(@class,'rdtNext')]/child::*)[1]")
    SingleInvite_StartDate_TimeToggle = (By.XPATH, "(//*[@class='rdtTimeToggle'])[1]")
    SingleInvite_StartDate_Hour_UpArrow = (By.XPATH, "(//*[@class='rdtBtn'][text()='▲'])[1]")
    SingleInvite_StartDate_Hour_DownArrow = (By.XPATH, "(//*[@class='rdtBtn'][text()='▼'])[1]")

    # # End Date
    SingleInvite_EndsAt_input = (By.XPATH, "//div[contains(text(),'Ends At *')]/following-sibling::*//input")
    SingleInvite_EndsAt_select = "(//td[@data-value='{}'][not(contains(@class,'rdtDisabled'))])[2]"
    SingleInvite_EndsAt_presentDate = (By.XPATH, "(//td[contains(@class,'rdtToday')])[2]")
    SingleInvite_EndsAt_NextMonth = (By.XPATH, "(//th[contains(@class,'rdtNext')]/child::*)[2]")
    SingleInvite_EndsAt_TimeToggle = (By.XPATH, "(//*[@class='rdtTimeToggle'])[1]")
    SingleInvite_EndsAt_Hour_UpArrow = (By.XPATH, "(//*[@class='rdtBtn'][text()='▲'])[4]")
    SingleInvite_EndsAt_Hour_DownArrow = (By.XPATH, "(//*[@class='rdtBtn'][text()='▼'])[4]")

    SingleInvite_HostName_Dropdown = (By.XPATH, "//div[@id='hostName']")
    SingleInvite_HostName = (By.XPATH, f"//*[contains(text(),'{TestData.LOCAL_CONTACT_3_IS_MEMBER}')]")
    SingleInvite_HostName_cross = (By.XPATH, "//*[@id='hostName']//*[@class=' css-183o9pv-indicatorContainer']/child::*")

    SingleInvite_Agenda = (By.XPATH, "//input[@id='agenda']")

    SingleInvite_FirstName= (By.XPATH, "//div[@id='firstName']")
    SingleInvite_FirstName_NewGuest= (By.XPATH, "//*[contains(text(),'New Guest')]")
    SingleInvite_LastName= (By.XPATH, "//input[@id='lastName']")
    SingleInvite_Contact= (By.XPATH, "//input[@id='contact']")

    SingleInvite_VisitorCategory= (By.XPATH, "//div[@id='visitorCategory']")
    SingleInvite_VisitorCategory_input= (By.XPATH, "//input[@id='react-select-5-input']")
    SingleInvite_VisitorCategory_select_visitor= (By.XPATH, "//*[contains(text(),'Interview Candidate')]")

    SingleInvite_AreasToVisit= (By.XPATH, "//div[@id='other_4953']")
    SingleInvite_CompanyName= (By.XPATH, "//input[@id='other_671']")
    SingleInvite_NeedWifi= (By.XPATH, "//input[@id='react-select-16-input']")
    SingleInvite_VehicleNumber= (By.XPATH, "//input[@id='other_4956']")

    SingleInvite_EscortName_cross= (By.XPATH, "//*[@id='escort_name_668']//*[@class=' css-183o9pv-indicatorContainer']/child::*")
    SingleInvite_EscortName_checkbox= (By.XPATH, "//*[@id='escort_name_668']//input")

    SingleInvite_SendInvite= (By.XPATH, "//div[@label='Send Invite']")

    SingleInvite_mandatoryFields_error = (By.XPATH, "//*[@class='vrs-error'][text()='This field is required.']")
    SingleInvite_pastDate_error = (By.XPATH, "//*[@class='vrs-error'][text()='Invite cannot be created in past']")
    SingleInvite_datatype_error = (By.XPATH, "//*[@class='vrs-error'][text()='Enter valid value']")
    SingleInvite_mandatoryFields = (By.XPATH, "//*[contains(text(),'*')][@class='vrs-label']")


    '''------------Invites List------------'''

    InvitesList_Venue_dropdown = (By.XPATH, "//*[@class='Header locationDropdown inviteList']")
    InvitesList_Venue_dropdown_input = (By.XPATH, "//*[@class='Header locationDropdown inviteList']//input")
    InvitesList_Venue_dropdown_select = (By.XPATH, f"//div[text()='{TestData.InvitesVenue}']")

    InvitesList_GuestSelect_dropdown = (By.XPATH, "//*[@class=' css-10rby8i']")
    InvitesList_GuestSelect_selectGuestName = (By.XPATH, "//div[text()='Guest Name']")
    InvitesList_GuestSelect_selectHostName = (By.XPATH, "//div[text()='Host Name']")
    InvitesList_Guest_input = (By.XPATH, "//*[@class='vrs-input vms-v4-Input-yq9CS']")

    InvitesList_StartDate_Cal = (By.XPATH, "(//*[@id='vms-custom-date-time-invites']//input)[1]")
    InvitesList_EndDate_Cal = (By.XPATH, "(//*[@id='vms-custom-date-time-invites']//input)[2]")

    InvitesList_DataTable_GuestName = "(//*[@id='vms-v4-invites-list']//td[1])"
    InvitesList_DataTable_HostName = "(//*[@id='vms-v4-invites-list']//td[6])"
    InvitesList_DataTable_numOfrows = "(//*[@id='vms-v4-invites-list']//tbody/tr)"

    InvitesList_MoreFilters = (By.XPATH, "//*[@class='vms-v4-CaretIconContainer-6xDmY']")
    InvitesList_CurrentStatus_Dropdown = (By.XPATH, "//*[@class='vrs-label'][text()='Current Status ']/following-sibling::*/child::*")
    InvitesList_CurrentStatus_Input = (By.XPATH, "//*[@class='vrs-label'][text()='Current Status ']/following-sibling::*//input")
    InvitesList_InviteType_Dropdown = (By.XPATH, "//*[@class='vrs-label'][text()='Invite Type ']/following-sibling::*/child::*")


    '''------------Bulk Invite------------'''
    BulkInvite_SelectCategory = (By.XPATH, "//*[@class='css-pqjb38']")

    # Data Table
    BulkInvite_TableDiv = (By.XPATH, "//*[@class='rdg-viewport']")
    BulkInvite_Table_FirstName = "(//*[@id='{}_firstName'])"
    BulkInvite_Table_LastName = "(//*[@id='{}_lastName'])"
    BulkInvite_Table_Contact = "(//*[@id='{}_contact'])"
    BulkInvite_Table_HostName = "(//*[@id='{}_hostName'])"
    BulkInvite_Table_HostName_Input = (By.XPATH, "//*[@id='vms-v4-bulk-invites-editor']//*[@class='css-pqjb38']//input")
    BulkInvite_Table_StartsAt = "(//*[@id='{}_startsAt'])"
    BulkInvite_Table_EndsAt = "(//*[@id='{}_endsAt'])"
    BulkInvite_Table_Agenda = "(//*[@id='{}_agenda'])"
    BulkInvite_Table_Agenda_Heading = (By.XPATH, "(//*[@class='vms-v4-Container-YcrXb'])[7]")
    BulkInvite_Table_AddRow = (By.XPATH, "(//*[@class='vms-v4-AddRowButton-nAEql'])")
    BulkInvite_Table_AddRow_Input = (By.XPATH, "(//*[@class='vms-v4-rowAddText-KakMs'])/..//input")


    # --------------------------------------- Functions -----------------------------------------

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Single Invite Functions'''

    def singleInvite_selectVenue(self):
        self.action_chain_click(self.SingleInvite_InviteVenue_dropdown)

    def singleInvite_StartsAt(self, days:int=None):
        self.action_chain_click(self.SingleInvite_StartsAt_input)
        if days is not None:
            cdate = self.get_element(self.SingleInvite_StartDate_presentDate)
            cdate_val = int(cdate.get_attribute('data-value')) + days
            if cdate_val > 30:
                cdate_val = cdate_val-1
                self.action_chain_click(self.SingleInvite_StartDate_NextMonth)
            self.SingleInvite_StartDate_select = self.SingleInvite_StartDate_select.format(cdate_val)
            self.action_chain_click((By.XPATH, self.SingleInvite_StartDate_select))

    def singleInvite_StartsAt_time(self, clicks:int=1, dir:int=0):
        self.action_chain_click(self.SingleInvite_StartsAt_input)
        self.action_chain_click(self.SingleInvite_StartDate_TimeToggle)
        for i in range(clicks):
            if dir == 0:
                self.action_chain_click(self.SingleInvite_StartDate_Hour_DownArrow)
            if dir == 1:
                self.action_chain_click(self.SingleInvite_StartDate_Hour_UpArrow)

    def singleInvite_EndsAt(self, days:int=None):
        self.action_chain_click(self.SingleInvite_EndsAt_input)
        if days is not None:
            cdate = self.get_element(self.SingleInvite_EndsAt_presentDate)
            cdate_val = int(cdate.get_attribute('data-value')) + days
            if cdate_val > 30:
                cdate_val = cdate_val-1
                self.action_chain_click(self.SingleInvite_EndsAt_NextMonth)
            self.SingleInvite_EndsAt_select = self.SingleInvite_EndsAt_select.format(cdate_val)
            self.action_chain_click((By.XPATH, self.SingleInvite_EndsAt_select))

    def singleInvite_hostName(self):
        self.action_chain_click(self.SingleInvite_HostName_Dropdown)
        self.action_chain_sendkeys_1(self.SingleInvite_HostName_Dropdown, TestData.HOST1_NAME)
        sleep(3)
        self.action_chain_click(self.SingleInvite_HostName)

    def singleInvite_Agenda(self):
        self.action_chain_click(self.SingleInvite_Agenda)
        self.action_chain_sendkeys_1(self.SingleInvite_Agenda, TestData.Single_invite_agenda)

    def singleInvite_firstName(self, fname):
        self.action_chain_click(self.SingleInvite_FirstName)
        self.action_chain_sendkeys_1(self.SingleInvite_FirstName, fname)
        visible = self.is_visible(self.SingleInvite_FirstName_NewGuest)
        if visible == True:
            self.action_chain_click(self.SingleInvite_FirstName_NewGuest)

    def singleInvite_lastName(self, lname):
        self.action_chain_click(self.SingleInvite_LastName)
        self.action_chain_sendkeys_1(self.SingleInvite_LastName, lname)

    def singleInvite_Contact(self, cmail):
        self.action_chain_click(self.SingleInvite_Contact)
        self.action_chain_sendkeys_1(self.SingleInvite_Contact, cmail)

    def singleInvite_visitorCategory(self):
        self.action_chain_click(self.SingleInvite_VisitorCategory)
        vis = self.is_visible(self.SingleInvite_VisitorCategory_select_visitor)
        print("Visible: ", vis)
        if vis == True:
            self.action_chain_click(self.SingleInvite_VisitorCategory_select_visitor)
        # self.action_chain_sendkeys_1(self.SingleInvite_VisitorCategory_input, vtype, Keys.ENTER)

    def singleInvite_AreasToVisit(self):
        self.action_chain_click(self.SingleInvite_AreasToVisit)

    def singleInvite_companyName(self):
        self.action_chain_click(self.SingleInvite_CompanyName)

    def singleInvite_vehicleNumber(self):
        self.action_chain_click(self.SingleInvite_VehicleNumber)

    def singleInvite_escortName(self):
        self.action_chain_click(self.SingleInvite_EscortName_checkbox)

    def singleInvite_get_no_of_mandate_fields(self):
        mfileds_visibility = self.is_visible(self.SingleInvite_mandatoryFields)
        print("mfileds_visibility: ", mfileds_visibility)
        if mfileds_visibility == True:
            num_of_mfields = len(self.get_elements(self.SingleInvite_mandatoryFields))
            print("No of mfields: ", num_of_mfields)
            return num_of_mfields
        return None

    def singleInvite_mandatory_error_check(self):
        error_visibility = self.is_visible(self.SingleInvite_mandatoryFields_error)
        print("error_visibility: ", error_visibility)
        if error_visibility == True:
            num_of_error = len(self.get_elements(self.SingleInvite_mandatoryFields_error))
            print("No of errors: ", num_of_error)
            return num_of_error
        return None

    def singleInvite_pastDate_error_check(self):
        pastDate_error_visibility = self.is_visible(self.SingleInvite_pastDate_error)
        print("pastDate_error_visibility: ", pastDate_error_visibility)
        if pastDate_error_visibility == True:
            num_of_errors = len(self.get_elements(self.SingleInvite_pastDate_error))
            print("No of past date errors: ", num_of_errors)
            return num_of_errors
        return None

    def singleInvite_datatype_error_check(self):
        datatype_error_visibility = self.is_visible(self.SingleInvite_datatype_error)
        print("datatype_error_visibility: ", datatype_error_visibility)
        if datatype_error_visibility == True:
            num_of_errors = len(self.get_elements(self.SingleInvite_datatype_error))
            print("No of past date errors: ", num_of_errors)
            return num_of_errors
        return None

    def singleInvite_sendInvite(self):
        self.action_chain_click(self.SingleInvite_SendInvite)
        sleep(3)

    
    '''Invites List Functions'''
    
    def invitesList_venue_select(self):
        self.action_chain_click(self.InvitesList_Venue_dropdown)
        self.action_chain_sendkeys_1(self.InvitesList_Venue_dropdown, "Digi")
        # self.scroll_to_element(self.InvitesList_Venue_dropdown_select)
        self.action_chain_click(self.InvitesList_Venue_dropdown_select)
    
    def invitesList_select_host_dropdown(self):
        self.action_chain_click(self.InvitesList_GuestSelect_dropdown)
        self.action_chain_click(self.InvitesList_GuestSelect_selectHostName)
        self.action_chain_click(self.InvitesList_Guest_input)
        self.action_chain_sendkeys_1(self.InvitesList_Guest_input, TestData.Invites_HostName)
    
    def invitesList_select_guest_dropdown(self):
        self.action_chain_click(self.InvitesList_GuestSelect_dropdown)
        self.action_chain_click(self.InvitesList_GuestSelect_selectGuestName)
        self.action_chain_click(self.InvitesList_Guest_input)
        self.action_chain_sendkeys_1(self.InvitesList_Guest_input, TestData.Invites_GuestName)

    def invitesList_StartsAt(self, days:int=None):
        self.action_chain_click(self.InvitesList_StartDate_Cal)
        if days is not None:
            cdate = self.get_element(self.SingleInvite_StartDate_presentDate)
            cdate_val = int(cdate.get_attribute('data-value')) + days
            if cdate_val > 30:
                cdate_val = cdate_val-1
                self.action_chain_click(self.SingleInvite_StartDate_NextMonth)
            self.SingleInvite_StartDate_select = self.SingleInvite_StartDate_select.format(cdate_val)
            self.action_chain_click((By.XPATH, self.SingleInvite_StartDate_select))

    def invitesList_EndsAt(self, days:int=None):
        self.action_chain_click(self.InvitesList_EndDate_Cal)
        if days is not None:
            cdate = self.get_element(self.SingleInvite_EndsAt_presentDate)
            cdate_val = int(cdate.get_attribute('data-value')) + days
            if cdate_val > 30:
                cdate_val = cdate_val-1
                self.action_chain_click(self.SingleInvite_EndsAt_NextMonth)
            self.SingleInvite_EndsAt_select = self.SingleInvite_EndsAt_select.format(cdate_val)
            self.action_chain_click((By.XPATH, self.SingleInvite_EndsAt_select))

    def invitesList_verify_TableData(self, hcheck=None, guest=None):
        sleep(4)
        num_of_rows = len(self.get_elements((By.XPATH, self.InvitesList_DataTable_numOfrows)))
        print("num_of_rows: ", num_of_rows)
        if num_of_rows is not None:
            for i in range(1, num_of_rows):
                if guest is None:
                    # print(f"selector: {self.InvitesList_DataTable_HostName}[{i}]")
                    host_name = self.get_element_text((By.XPATH, f"{self.InvitesList_DataTable_HostName}[{i}]"))
                    print("Host Name: ", host_name)
                    if hcheck is not None:
                        assert TestData.Invites_HostName in host_name
                else:
                    # print(f"selector: {self.InvitesList_DataTable_HostName}[{i}]")
                    guest_name = self.get_element_text((By.XPATH, f"{self.InvitesList_DataTable_GuestName}[{i}]"))
                    print("Guest Name: ", guest_name)
                    if hcheck is not None:
                        assert TestData.Invites_GuestName in guest_name
        sleep(2)

    def invitesList_currentStatus_selector(self):
        self.action_chain_click(self.InvitesList_CurrentStatus_Dropdown)
        self.action_chain_sendkeys_1(self.InvitesList_CurrentStatus_Input, TestData.Invites_cstatus, Keys.ENTER)
        sleep(2)

    

    '''Bulk Invite Functions'''
    def bulkInvite_visitor_category_select(self):
        self.action_chain_click(self.BulkInvite_SelectCategory)
        vis = self.is_visible(self.SingleInvite_VisitorCategory_select_visitor)
        print("Visible: ", vis)
        if vis == True:
            self.action_chain_click(self.SingleInvite_VisitorCategory_select_visitor)


    def bulkInvite_add_data_to_table(self, fname, lname, cmail, sdate, edate, agenda, i=0):
        print("bulk i: ", i)
        BulkInvite_Table_FirstName = InvitesPage.BulkInvite_Table_FirstName.format(i)
        BulkInvite_Table_LastName = InvitesPage.BulkInvite_Table_LastName.format(i)
        BulkInvite_Table_Contact = InvitesPage.BulkInvite_Table_Contact.format(i)
        BulkInvite_Table_HostName = InvitesPage.BulkInvite_Table_HostName.format(i)
        BulkInvite_Table_StartsAt = InvitesPage.BulkInvite_Table_StartsAt.format(i)
        BulkInvite_Table_EndsAt = InvitesPage.BulkInvite_Table_EndsAt.format(i)
        BulkInvite_Table_Agenda = InvitesPage.BulkInvite_Table_Agenda.format(i)

        print("First name xpath: ", BulkInvite_Table_FirstName)

        # first name
        self.scroll_to_element_to_mid((By.XPATH, BulkInvite_Table_FirstName))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_FirstName))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_FirstName))
        self.action_chain_sendkeys_1(
            (By.XPATH, BulkInvite_Table_FirstName), fname)
        # last name
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_LastName))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_LastName))
        self.action_chain_sendkeys_1(
            (By.XPATH, BulkInvite_Table_LastName), lname)
        # contact email
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_Contact))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_Contact))
        self.action_chain_sendkeys_1(
            (By.XPATH, BulkInvite_Table_Contact), cmail)
        # host
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_HostName))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_HostName))
        self.action_chain_sendkeys_1(
            InvitesPage.BulkInvite_Table_HostName_Input, TestData.HOST1_NAME)
        sleep(3)
        self.action_chain_click(InvitesPage.SingleInvite_HostName)
        # date starts at
        self.scroll_to_element((By.XPATH, BulkInvite_Table_StartsAt))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_StartsAt))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_StartsAt))
        self.action_chain_sendkeys_1(
            (By.XPATH, BulkInvite_Table_StartsAt), sdate, Keys.ENTER)
        # date ends at
        self.scroll_to_element((By.XPATH, BulkInvite_Table_EndsAt))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_EndsAt))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_EndsAt))
        self.action_chain_sendkeys_1(
            (By.XPATH, BulkInvite_Table_EndsAt), edate, Keys.ENTER)
        # agenda
        self.scroll_to_element((By.XPATH, BulkInvite_Table_Agenda))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_Agenda))
        self.action_chain_doubleClick((By.XPATH, BulkInvite_Table_Agenda))
        self.action_chain_sendkeys_1(
            (By.XPATH, BulkInvite_Table_Agenda), agenda)

        # Scrolling to left
        self.action_chain_click(InvitesPage.BulkInvite_Table_Agenda_Heading)
        self.scroll_horizontally_left((By.XPATH, BulkInvite_Table_Contact))
        self.scroll_horizontally_left((By.XPATH, BulkInvite_Table_LastName))
        self.scroll_horizontally_left((By.XPATH, BulkInvite_Table_FirstName))
        sleep(2)
    
    def bulkInvite_add_rows(self, rows):
        # rows
        self.scroll_to_element_to_mid(self.BulkInvite_Table_AddRow_Input)
        self.action_chain_click(self.BulkInvite_Table_AddRow_Input)
        self.action_chain_sendkeys_1(self.BulkInvite_Table_AddRow_Input, Keys.BACKSPACE, rows)
        self.action_chain_click(self.BulkInvite_Table_AddRow)
