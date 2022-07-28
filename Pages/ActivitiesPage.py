import sys
import traceback
from itertools import count
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from WebConfig.time_functions import WebConfigFunctions as Config


class ActivitiesPage(BasePage):
    # Headers
    Activities_Header_Link = (By.XPATH, "//a[text()='Activities'][@href='/vms-v4/activities']")
    CreateActivity_link = (By.XPATH, "//div[text()='Create Activity'][contains(@class,'vms-v4-PageHeader-lZcjR')]")

    '''Create Activity'''

    CreateActivity_Venue_dropdown = (By.XPATH, "//*[text()='Invite Venue *'][@class='vrs-label']/..//*[@class='ant-select-selector']")
    CreateActivity_Venue_select = (By.XPATH, f"//div[contains(text(),'{TestData.InvitesVenue}')]")
    CreateActivity_contactInput = (By.XPATH, "//input[@id='contact']")
    CreateActivity_ActivityType_dropdown = (By.XPATH, "//*[@id='activityType']")
    CreateActivity_ActivityType_optionSelect = (By.XPATH, f"//div[contains(text(),'{TestData.CreateActivity_activityType_CheckIn}')]")
    CreateActivity_VisitorCategory_dropdown = (By.XPATH, "//*[@id='visitorCategory']")
    CreateActivity_VisitorCategory_select_visitor= (By.XPATH, f"//*[contains(text(),'{TestData.CreateActivity_visitorCategory}')]")
    # Covid Questions
    CreateActivity_CovidQuestion1_ans = (By.XPATH, "(//*[@class='form-group']/following-sibling::*//*[@class='css-1dbjc4n'][2])[1]")
    CreateActivity_CovidQuestion2_ans = (By.XPATH, "(//*[@class='form-group']/following-sibling::*//*[@class='css-1dbjc4n'][2])[2]")
    CreateActivity_CovidQuestion3_ans = (By.XPATH, "(//*[@class='form-group']/following-sibling::*//*[@class='css-1dbjc4n'][2])[3]")
    CreateActivity_CovidQuestion4_ans = (By.XPATH, "(//*[@class='form-group']/following-sibling::*//*[@class='css-1dbjc4n'][2])[4]")
    # 
    CreateActivity_FirstName = (By.XPATH, "//input[@id='first_name_646']")
    CreateActivity_LastName = (By.XPATH, "//input[@id='last_name_647']")
    CreateActivity_Email = (By.XPATH, "//input[@id='email_648']")
    CreateActivity_HostName_dropdown = (By.XPATH, "//*[@id='meeting_with_649']//*[@class=' css-10rby8i']")
    CreateActivity_HostName = (By.XPATH, f"//*[contains(text(),'{TestData.LOCAL_CONTACT_3_IS_MEMBER}')]")
    CreateActivity_NDAcheckbox = (By.XPATH, "//button[@id='gdprAccept']/..//input")
    CreateActivity_CompanyName = (By.XPATH, "//input[@id='other_657']")
    # Wifi
    CreateActivity_Wifi = (By.XPATH, "//*[@id='other_4949']")
    CreateActivity_Wifi_input = (By.XPATH, "//*[@id='other_4949']//input")
    # Parking
    CreateActivity_ParkingDropdown = (By.XPATH, "//*[@id='other_4950']")
    CreateActivity_ParkingDropdown_input = (By.XPATH, "//*[@id='other_4950']//input")
    CreateActivity_VehicleNumber = (By.XPATH, "//input[@id='other_4952']")
    # Areas to Visit
    CreateActivity_AreasToVisit = (By.XPATH, "//*[@id='other_4951']")
    CreateActivity_AreasToVisit_select = (By.XPATH, "//div[contains(text(),'Floor A')]")
    # Confirm Checkin
    CreateActivity_Confirm = (By.XPATH, "//div[contains(text(),'Confirm check-in')]")
    CreateActivity_error_alert = (By.XPATH, "//*[contains(text(),'Please fill all required data !')]")
    CreateActivity_mandatory_error1 = (By.XPATH, "//*[contains(text(),'This field is required.')]")
    CreateActivity_mandatory_error_covidQuestions = (By.XPATH, "//*[contains(text(),'You need to select 1 option')]")
    CreateActivity_mandatory_fields = (By.XPATH, "//*[@class='vms-v4-CreateActivityContent-1nJWK']//*[contains(text(),'*')]")
    CreateActivity_emailField_inputError = (By.XPATH, "//input[@id='email_648']/..//following-sibling::*[contains(text(),'Enter valid email')]")


    
    # --------------------------------------- Functions -----------------------------------------

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Create Activity Functions'''
    
    def createActivity_selectVenue(self):
        self.action_chain_click(self.CreateActivity_Venue_dropdown)
        self.action_chain_click(self.CreateActivity_Venue_select)

    def createActivity_contactInput(self, contact):
        self.action_chain_click(self.CreateActivity_contactInput)
        self.action_chain_sendkeys_1(self.CreateActivity_contactInput, contact)

    def createActivity_activityType(self):
        self.action_chain_click(self.CreateActivity_ActivityType_dropdown)
        self.action_chain_click(self.CreateActivity_ActivityType_optionSelect)

    def createActivity_visitorCategory(self):
        self.action_chain_click(self.CreateActivity_VisitorCategory_dropdown)
        self.action_chain_click(self.CreateActivity_VisitorCategory_select_visitor)

    def createActivity_covidQuestions(self):
        self.action_chain_click(self.CreateActivity_CovidQuestion1_ans)
        self.action_chain_click(self.CreateActivity_CovidQuestion2_ans)
        self.action_chain_click(self.CreateActivity_CovidQuestion3_ans)
        self.action_chain_click(self.CreateActivity_CovidQuestion4_ans)

    def createActivity_visitorDetails(self, fname, lname, cmail):
        # fname
        self.action_chain_click(self.CreateActivity_FirstName)
        self.action_chain_sendkeys_1(self.CreateActivity_FirstName, fname)
        # lname
        self.action_chain_click(self.CreateActivity_LastName)
        self.action_chain_sendkeys_1(self.CreateActivity_LastName, lname)
        # email
        self.action_chain_click(self.CreateActivity_Email)
        self.action_chain_sendkeys_1(self.CreateActivity_Email, cmail)

    def createActivity_selectHost(self):
        self.action_chain_click(self.CreateActivity_HostName_dropdown)
        self.action_chain_sendkeys_1(self.CreateActivity_HostName_dropdown, TestData.HOST1_NAME)
        sleep(3)
        self.action_chain_click(self.CreateActivity_HostName)

    def createActivity_checkbox_NDA(self):
        self.action_chain_click(self.CreateActivity_NDAcheckbox)

    def createActivity_companyName(self):
        self.action_chain_click(self.CreateActivity_CompanyName)
        self.action_chain_sendkeys_1(self.CreateActivity_CompanyName, TestData.CreateActivity_companyName)

    def createActivity_wifi(self):
        self.action_chain_click(self.CreateActivity_Wifi)
        self.action_chain_sendkeys_1(self.CreateActivity_Wifi_input, TestData.CreateActivity_Yes, Keys.ENTER)

    def createActivity_parking(self):
        self.action_chain_click(self.CreateActivity_ParkingDropdown)
        self.action_chain_sendkeys_1(self.CreateActivity_ParkingDropdown_input, TestData.CreateActivity_Yes, Keys.ENTER)
        self.action_chain_click(self.CreateActivity_VehicleNumber)
        self.action_chain_sendkeys_1(self.CreateActivity_VehicleNumber, TestData.CreateActivity_vehicleNumber)

    def createActivity_areasToVisit(self):
        self.action_chain_click(self.CreateActivity_AreasToVisit)
        self.action_chain_click(self.CreateActivity_AreasToVisit_select)

    def createActivity_confirmCheckIn(self):
        self.action_chain_click(self.CreateActivity_Confirm)

    def createActivity_mandatory_error(self):
        enum = len(self.get_elements(self.CreateActivity_mandatory_error1))
        enum2 = len(self.get_elements(self.CreateActivity_mandatory_error_covidQuestions))
        count1 = int(enum + enum2)
        return count1

    def createActivity_mandatoryFields(self):
        mfields = len(self.get_elements(self.CreateActivity_mandatory_fields))
        return mfields

    def createActivity_emailField_InputError_check(self, cmail):
        self.action_chain_click(self.CreateActivity_Email)
        self.action_chain_sendkeys_1(self.CreateActivity_Email, cmail)
        self.action_chain_click(self.CreateActivity_CompanyName)
        return self.is_visible(self.CreateActivity_emailField_inputError)
        