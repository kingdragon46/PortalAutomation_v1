from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
from pytz import timezone
from random_name_generator import ran_name, ran_name_2
from WebConfig.time_functions import WebConfigFunctions as Config

class TestData:
    
    CHROME_EXECUTABLE_PATH = "chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "C:\WebDrivers\geckodriver-v0.30.0-win64\geckodriver"

    # Local ----------------------------------------------------------------------------
    LOCAL_BASE_URL = "https://ndl.veris.in/login/NewLogin"
    LOCAL_USER_NAME = "neeraj.dhiman@veris.in"
    LOCAL_PASSWORD = "Passw0rd@123"
    LOCAL_USER_NAME_2 = "shailendra.tiranga@veris.in"
    LOCAL_PASSWORD_2 = "Ttpl@12345"
    LOCAL_USER_NAME_3 = "vivek.anand@veris.in"
    LOCAL_PASSWORD_3 = "J^6txV!uM3x5"
    # LOCATION
    LOCAL_LOCATION_1 = "Genpact IT Park"
    LOCAL_LOCATION_2 = "Bussiness Tower"
    LOCAL_URL_DOMAIN = "ndl"
    # Guests
    LOCAL_CONTACT_1_IS_DRAFTED_FALSE = "test veris"
    LOCAL_CONTACT_1_IS_MEMBER = "Johnathan Gracer"
    LOCAL_CONTACT_2_IS_MEMBER = "Mark Jacob"
    LOCAL_CONTACT_3_IS_MEMBER = "Shailendra Tiranga"
    

    # LIVE -----------------------------------------------------------------------------
    LIVE_BASE_URL = "https://mrmindia.veris.in/login/NewLogin"
    LIVE_USER_NAME = "shailendra.tiranga@veris.in"
    LIVE_PASSWORD = "Passw0rd@98765"
    # LOCATION
    LIVE_LOCATION_1 = "KLJ Complex"
    LIVE_LOCATION_2 = "Complex 1"
    LIVE_URL_DOMAIN = "mrmindia"
    # Guests
    LIVE_CONTACT_1_IS_DRAFTED_FALSE = "fresh user"
    LIVE_CONTACT_1_IS_MEMBER = "Shailendra Tiranga"
    LIVE_CONTACT_2_IS_MEMBER = "Neeraj Dhiman"
    LIVE_CONTACT_3_IS_MEMBER = "Shailendra Tiranga"


    # VALUES ------------------------------------------------------------------------------------
    BASE_URL = LOCAL_BASE_URL
    USER_NAME = LOCAL_USER_NAME
    PASSWORD = LOCAL_PASSWORD
    USER_NAME_2 = LOCAL_USER_NAME_2
    PASSWORD_2 = LOCAL_PASSWORD_2
    USER_NAME_3 = LOCAL_USER_NAME_3
    PASSWORD_3 = LOCAL_PASSWORD_3
    LOC_1 = LOCAL_LOCATION_1
    LOC_2 = LOCAL_LOCATION_2
    URL_DOMAIN = LOCAL_URL_DOMAIN

    # URL FORMATING 
    LOGIN_PAGE_TITLE = "Veris | Powering Future Workplaces"

    RESOURCE_PAGE_URL = f"https://{URL_DOMAIN}.veris.in/meeting-room/find-resource"

    MY_BOOKING_URL = f"https://{URL_DOMAIN}.veris.in/meeting-room/my-bookings"

    AFTER_LOGIN_URL = f"https://{URL_DOMAIN}.veris.in/resource-manager"

    BOOKING_LOGS_URL = f"https://{URL_DOMAIN}.veris.in/resource-manager/booking-logs"

    WORK_STATUS_USERSTATUS_URL = f"https://{URL_DOMAIN}.veris.in/work-status/user-status"

    WORK_STATUS_TEAMS_URL = f"https://{URL_DOMAIN}.veris.in/work-status/teams"

    WORK_STATUS_INSIGHTS_URL = f"https://{URL_DOMAIN}.veris.in/work-status/work-insights"

    DOWNLOAD_REPORTS_URL = f"https://{URL_DOMAIN}.veris.in/download-center/reports"

    INVITES_PAGE_URL = f"https://{URL_DOMAIN}.veris.in/vms-v4/invites"


    '''-----------------------------POSITIVE TESTING-----------------------------'''

    '''Guests'''
    CONTACT_1_IS_DRAFTED_FALSE = LOCAL_CONTACT_1_IS_DRAFTED_FALSE
    CONTACT_1_IS_MEMBER = LOCAL_CONTACT_1_IS_MEMBER
    CONTACT_2_IS_MEMBER = LOCAL_CONTACT_2_IS_MEMBER
    CONTACT_3_IS_MEMBER = LOCAL_CONTACT_3_IS_MEMBER

    '''Desk Booking details'''
    DEFAULT_HOSTNAME = "Neeraj Dhiman"
    DEFAULT_HOSTEMAIL = "neeraj.dhiman@veris.in"
    HOST1_NAME = "Shail"
    HOST1_FULLNAME = "Shailendra Tiranga"
    HOST1_EMAIL = "shailendra.tiranga@veris.in"
    HOST2_NAME = "Himans"
    HOST2_FULLNAME = "Himanshi Sharma"
    HOST2_EMAIL = "himanshi.sharma@veris.in"
    BOOKING_DATE = Config.booking_date(5)
    BOOKING_DATE1 = Config.booking_date(5)
    TIME_START = Config.time_select(15)
    TIME_END = Config.time_select(30)
    TIME_END2 = Config.time_select(20)
    TIME_START3 = Config.time_select(25)
    TIME_END3 = Config.time_select(45)
    TIME_OVERLAPPING_START = Config.time_select(25)
    TIME_OVERLAPPING_END = Config.time_select(45)
    TILL_NEXT_DAY_START_TIME = f"{Config.till_next_day_date()} 23:55"
    TILL_NEXT_DAY_END_TIME = f"{Config.till_next_day_date(1)} 01:30"
    REPEAT_TILL_DATE = f"{Config.repeat_till_date(30)} 01:00"
    REPEAT_TILL_DATE2 = f"{Config.repeat_till_date(30)} 23:00"
    REPEAT_TILL_DATE3 = Config.repeat_till_date(6)
    WEEKLY_REPEAT_DATE1 = Config.booking_date(7)
    WEEKLY_REPEAT_CAL_DATE = Config.cal_date_format(WEEKLY_REPEAT_DATE1)
    WEEKLY_REPEAT_TILL_DATE = f"{Config.repeat_till_date(28)}"
    DESK_NO_1 = None
    DESK_W_ISSUE = ['202', 202]

    '''Room booking'''
    # ROOM_W_ISSUE = ['Room Booking rule', '107', '108', '109', '120', 'Board Room', '105']
    ROOM_W_ISSUE = 'WS 5'
    ROOM_W_ISSUE_2 = 'WS 16'
    ROOM_AGENDA = "Automation testing"
    ROOM_START_DATE = Config.room_datetime(2,15)
    ROOM_END_DATE = Config.room_datetime(2,35)
    ROOM_OVERLAPPING_TIME_START = Config.room_start_overlapping_datetime()
    ROOM_OVERLAPPING_TIME_END = Config.room_end_overlapping_datetime()
    ROOM_OVERLAPPING_TIME_END_2 = "27 Apr 2022 01:10"
    ROOM_OVERLAPPING_TIME_START_1 = "27 Apr 2022 01:15"
    ROOM_OVERLAPPING_TIME_END_1 = "27 Apr 2022 01:30"

    '''Weekly'''
    ROOM_WSTART_DATE = Config.room_datetime(7,15)
    ROOM_WEND_DATE = Config.room_datetime(7,35)
    REPEAT_FREQUENCY = "1"
    WEEKLY_REPEAT_TILL_DATE = Config.repeat_till_date(21)
    WEEKLY_REPEAT_TILL_DATE2 = "24 Apr 2022"

    '''Amenities'''
    AM_1 = "Dual"
    DUAL_MONITOR = "Dual Monitor"
    AM_QUANTITY = "2"
    BS_CAL_ENDDATE = Config.repeat_till_date2(30)

    CDATE = Config.current_datetime()

    '''Tag'''
    TAG = "Engineering Deck"


    '''-------------------------NEGATIVE-------------------------'''

    INCORRECT_USERNAME = "AB!^C"
    INCORRECT_PASSWORD = "XYZ@!#"

    '''Desk Booking'''
    PAST_BOOKING_DATE = Config.booking_date(-5)
    PAST_TIME_START = Config.time_select(-15)
    PAST_TIME_END = Config.time_select(-30)
    NEGATIVE_TIME_START_1 = Config.time_select(15)
    NEGATIVE_TIME_END_1 = Config.time_select(18)
    NEGATIVE_TIME_END_2 = Config.time_select(120)

    """--------------------------------------- Booking Logs ----------------------------"""
    BL_CAL_DATE = Config.repeat_till_date2(22)
    BL_Venue1= "Genpact IT"
    '''Download Report'''
    # Status
    Status_All = "All"
    Status_Scheduled = "Scheduled"
    Status_Cancelled = "Cancelled"
    Status_ApprovalPending = "Approval Pending"
    Status_Assigned = "Assigned"
    Status_Expired = "Expired"
    # Template
    Template_Name = "Booking Logs"
    # Dates
    DR_START_DATE = 1
    DR_END_DATE = 30

    """--------------------------------------- Health Status ----------------------------"""
    HS_Reassess = "Reassess"
    HS_Error_msg = "Please fill all required data !"


    """--------------------------------------- Work Status ----------------------------"""
    TEAM_TO_BE_SELECTED = "Bosch group"

    '''TeamsPage'''
    TeamsPage_Team = "Bosch group"
    TeamsPage_Employee = "Himanshi"

    '''Insights'''
    Insights_Team_LOCAL = "Bosch group"
    Insights_Team_LIVE = "MRM India admin group"


    """--------------------------------------- Invites Page ----------------------------"""
    
    '''Single Invite'''
    Single_invite_agenda = "Automation Testing Of Invites"
    MandatoryFields_to_skip = 4
    InvitesVenue = "Digicred Headquarters"
    Invites_HostName = "QA Admin"
    Invites_GuestName = "Manoj"
    Invites_cstatus = "Scheduled"

    '''Bulk Invite'''
    BulkInvite_Rows = 10
    BulkInvite_idNo = "0"

    """--------------------------------------- Activities Page ----------------------------"""

    CreateActivity_activityType_CheckIn = "Check-In"
    CreateActivity_activityType_CheckOut = "Check-out"
    CreateActivity_contactInput = "shailendra.tiranga@veris.in"
    CreateActivity_companyName = "Test Company"
    CreateActivity_vehicleNumber = "HR26AB1234"
    CreateActivity_visitorCategory = "Interview Candidate"
    CreateActivity_Yes = "Yes"
    CreateActivity_NotTrueEmail = "abc"

    
print(f"{TestData.ROOM_START_DATE} ---------- {TestData.ROOM_END_DATE, 18}")