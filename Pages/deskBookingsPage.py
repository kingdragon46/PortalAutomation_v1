from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import traceback


class deskBookingsPage(BasePage):

    '''By XPATH'''
    # Body Xpath
    BODY = (By.CSS_SELECTOR, "body")
    #
    DESK_NO = None
    # ------
    BOOKING_NAV = (
        By.XPATH, "//*[@class='navigation-AppName-1_BPN'][text()='Booking']")
    BOOK_SPACE_NAV = (By.XPATH, "//*[contains(text(), 'Book space')]")
    LOCATION_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[1]/div/div")
    GENPACT_IT_PARK = (
        By.XPATH, "//div[contains(text(), 'Genpact IT Park')]/parent::*/parent::*/parent::*/preceding-sibling::*[2]/span/child::*")
    BUSINESS_TOWER = (By.XPATH, "//div[contains(text(), 'Bussiness Tower')]")
    FREE_CLICK = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/p")
    SECOND_FLOOR = (By.ID, "1-floor")
    STATUS_DROPDOWN = (
        By.XPATH, f"//*[text()='Status']/following-sibling::*/child::*")
    AVAILABLE_STATUS = (By.CSS_SELECTOR, "span[title='Available']")
    BOOKED_STATUS = (By.CSS_SELECTOR, "span[title='Booked']")
    ASSIGNED_STATUS = (By.CSS_SELECTOR, "span[title='Assigned']")
    INACTIVE_STATUS = (By.CSS_SELECTOR, "span[title='Inactive']")
    ALL_STATUS = (By.CSS_SELECTOR, "span[title='All']")
    LIST_VIEW_BUTTON = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]")
    # DESK = (By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/button")
    DESK_AVAIL = "(//*[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button)"
    DESK_AVAIL_2 = (
        By.XPATH, "//*[text()='Available']/parent::*/parent::*/preceding-sibling::*/div/div")
    DESK_AVAIL_NAME = "(//div[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button)"
    DESK = "//*[text()='{}']/parent::*/parent::*/following-sibling::*[5]/button"
    DESK_205 = (
        By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr[6]/td[6]/button")
    DESK_NUMBER = (By.XPATH, f"//*[@class='desk-title']")

    # Resource Type
    RESOURCE_DROPDOWN = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div")
    RESOURCE_DESKS = (By.CSS_SELECTOR, "span[title='Desks']")

    # Book Space Date Selectors
    BS_DATE_DIV_CONTAINER = (By.XPATH, "//*[text()='Date & Time']/parent::*/child::*[4]/child::*/div")
    BS_DATE_DIV = (By.XPATH, "//input[@placeholder='Today']")
    BS_DSINGLE_DAY = (By.XPATH, "//*[@placeholder='Select date']")
    BS_DRecurringBookings_MULTIPLE_DAYS = (By.XPATH, "//p[text()='Multiple Days']")
    BS_DENDDATE = (By.XPATH, "//input[@placeholder='End date']")
    BS_DONE = (By.XPATH, "//button/span[text()='Done']")
    TDATA_ENDDATE = (By.XPATH, f"//*[@title='{TestData.BS_CAL_ENDDATE}']")
    TDATA_ENDDATE_1 = "//*[@title='{}']"
    CAL_NEXT_MONTH = (By.CLASS_NAME, "ant-picker-next-icon")
    CAL_OK_BUTTON = (By.XPATH, "//button/span[text()='Ok']")

    # 2nd Floor total desks
    TOTAL_DESKS_2ND_FLOOR = (
        By.XPATH, f"//*[@id='1-floor']/div/div[3]/div[1]/p")
    AVAILABLE_DESKS_2ND_FLOOR = (
        By.XPATH, f"//*[@id='1-floor']/div/div[3]/div[2]/p")

    # Booking Modal
    BookResource_Modal_MODAL_CLOSE = (By.CSS_SELECTOR, "*[title='Close']")
    BookResource_Modal_BOOKING_CONFIRM_BUTTON = (
        By.XPATH, "//span[text()='Confirm Booking']/..")
    BookResource_Modal_HOST_DROPDOWN = (
        By.CSS_SELECTOR, "*[title='Edit Details']")
    BookResource_Modal_HOST_INPUT = (
        By.XPATH, "//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[1]/div[1]/div/div[4]/div/div/div")
    BookResource_HOST_SELECT = (
        By.XPATH, f"//*[contains(text(), '{TestData.HOST2_FULLNAME}')]")

    BookResource_DATE_INPUT = (
        By.XPATH, "//input[@placeholder='Select date']")
    BookResource_DATE_CALENDER_BODY = (
        By.XPATH, "/html/body/div[9]/div/div/div/div/div[1]/div[2]")
    BookResource_DATE_SELECT_2nd = (
        By.XPATH, "/html/body/div[6]/div/div/div/div/div[1]/div[2]/table/tbody/tr[1]/td[7]/div")
    BookResource_TIME_SELECT_START = (
        By.XPATH, "(//*[@placeholder='Select time'])[1]")
    BookResource_TIME_SELECT_END = (
        By.XPATH, "(//*[@placeholder='Select time'])[2]")
    BookResource_RecurringBookings_MULTIPLE_DAYS_SINGLE_BOOKING = (
        By.XPATH, "//*[contains(text(), 'Multiple Days')]")
    BookResource_RecurringBookings_MULTIPLE_DAYS_SB_START = (
        By.XPATH, "//input[@placeholder='Start date']")
    BookResource_RecurringBookings_MULTIPLE_DAYS_SB_END = (
        By.XPATH, "//input[@placeholder='End date']")
    BookResource_TIME_SELECT_ERROR = (By.XPATH, "//p[@class='text-xs text-red-400']")
    # Booking confirmation
    BookResource_DESK_AFTER_BOOKING_DIV = (
        By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr/td[1]/div")
    # BookResource_DESK_AFTER_BOOKING_TITLE = (By.XPATH, f"//*[text()='{DESK_NO}']/parent::*/parent::*")
    BookResource_DESK_AFTER_BOOKING_TITLE = "//*[text()='{}']/parent::*/parent::*"

    # Resource Details
    ResourceDetails_RD_CALENDER_INPUT = (
        By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/input")
    ResourceDetails_SCHEDULE_LISTING = (
        By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[3]/div/div/div[2]")
    ResourceDetails_I_BUTTON = (By.XPATH, f"//*[@class='rbc-event-content']/span")
    ResourceDetails_I_INFO = (By.XPATH, f"//*[@class='ant-popover-content']")
    ResourceDetails_I_INFO2 = (By.XPATH, f"/html/body/div[7]/div/div/div")
    ResourceDetails_RD_TIME_CHECK = (By.CLASS_NAME, "rbc-event-label")
    BOOK_THIS_SPACE = (
        By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[4]/div/button")
    ResourceDetails_BOOKING_HOSTNAME = (
        By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[1]")
    ResourceDetails_BOOKING_HOSTEMAIL = (
        By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[2]")
    ResourceDetails_BOOKING_START = (
        By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[3]")
    ResourceDetails_BOOKING_END = (
        By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[4]")

    # Resource page confirmation
    DATE_CALENDER_RPAGE = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/input")
    BDATE_RPAGE_INPUT = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div/input")
    BDATE_CALENDER_DONE = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/button")
    DESK_RPAGE_CHECK_DIV = "//*[@title='{}']/parent::*/parent::div"
    DESK_RPAGE_CHECK_BOOK_BUTTON = "//div[@title='{}']/parent::*/parent::*/following-sibling::*[5]/button"
    DESK_RPAGE_STATUS_CHECK = "//*[@title='{}']/parent::*/parent::td/following-sibling::*[1]/div/div"

    # My Bookings
    MyBookings_C_TEXT = "//*[contains(text(), '{}')]"
    MY_BOOKING_NAV = (By.XPATH, f"//*[@id='sub-nav']/div[2]")
    # DESK_CHECK_NAME = (By.XPATH, "//p[text()='{}']".format(DESK_NO))
    MyBookings_DESK_CHECK_NAME = "//p[text()='{}']"
    # DESK_CHECK_NAME = (By.XPATH, MyBookings_C_TEXT)
    MyBookings_MyBookings_DESK_CHECK_DIV = "//p[text()='{}']/parent::*/parent::div"
    MyBookings_DESK_SCHEDULE_CHECK = "//p[text()='{}']/parent::*/following-sibling::*[1]"
    MyBookings_DESK_MEETING_OPTIONS_BUTTONS_CHECK = "//p[text()='{}']/parent::*/following-sibling::*[2]"
    MyBookings_DESK_MEETING_OPTIONS_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2]"
    # MyBookings_DESK_MEETING_OPTIONS_CANCEL_BUTTON = "(//p[text()='{}']/parent::*/parent::*/preceding-sibling::*/child::*[2]/child::*/child::*/*[@class='MuiSvgIcon-root'])"
    MyBookings_DESK_MEETING_OPTIONS_CANCEL_BUTTON = "//p[text()='{}']/parent::*/parent::*/preceding-sibling::*/child::*[2]/child::*/child::*/*[last()]"
    MyBookings_DESK_MEETING_OPTIONS_CANCEL_ALL_BUTTON = (By.XPATH, "//*[text()='Cancel All']")
    MyBookings_DESK_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/button)"
    MyBookings_MAIN_CARDS_CONTAINER = (By.XPATH, f"//*[@id='mainBookingCardsContainer']")

    # Booking Successfull message
    BK_SUCCESS = (By.XPATH, f"/html/body/div[5]/div/div/div/div/div/span[2]")
    BK_OVERLAPPING_ERROR = (By.XPATH, f"/html/body/div[12]/div/div/div/div")
    BK_OVERLAPPING_ERROR_MSG = (
        By.XPATH, "//span[contains(text(), 'Error')]")

    # Health Status
    HS_HEALTH_STATUS_MSG = 'You cannot book the desk since your health status is "Not Filled", Please fill your health status under "My Bookings"'
    HS_HEALTH_STATUS_PROMPT = (
        By.XPATH, f"//*[contains(text(), 'Update Health Status')]")
    HS_UPDATE_HEALTH_STATUS_BUTTON = (
        By.XPATH, f"//*[text()='Health status']/../following-sibling::*//button")
    HS_FULLY_VACCINATED = (
        By.XPATH, f"//*[contains(text(), 'Fully Vaccinated')]/preceding-sibling::*/child::*")
    HS_HEALTH_CONDITION_NONE = (
        By.XPATH, f"//*[contains(text(), 'None')]/preceding-sibling::*/child::*")
    HS_PROVIDING_CARE_NO = (
        By.XPATH, f"//*[contains(text(), 'If you are providing care to a confirmed /suspect/probable case')]/parent::*/following-sibling::*/child::div[2]/child::div[2]/child::div/child::div/child::div/child::*")
    HS_CONTACT_14DAYS_NO = (
        By.XPATH, f"//*[contains(text(), 'If you have come in contact with any COVID-19 positive case in the last 14 days')]/parent::*/following-sibling::*/child::div[2]/child::div[2]/child::div/child::div/child::div/child::*")
    HS_OFFICE_TO_VISIT_DROPDOWN = (By.XPATH, f"//*[@id='other_5014']/div")
    HS_OFFICE_TO_VISIT_SELECT = (
        By.XPATH, f"//*[contains(text(), 'Digicred HQ-New York')]")
    HS_PARKING_DROPDOWN = (By.XPATH, f"//*[@id='other_5015']/div")
    HS_PARKING_SELECT = (By.XPATH, f"//*[contains(text(), '2 Wheeler')]")
    HS_CONFIRM_DECLARATION = (
        By.XPATH, f"//*[contains(text(), 'Confirm Declaration')]")
    HS_Q1_OPTIONS = "(//*[@class='workflow-health']//*[@class='meeting-room-padding-cd0a98b0f8d88ac043f27d7a806873ed'][1]//*[@class='next_btn'])"
    HS_Q2_OPTIONS = "(//*[@class='workflow-health']//*[@class='meeting-room-padding-cd0a98b0f8d88ac043f27d7a806873ed'][2]//*[@class='next_btn'])"
    HS_Q3_OPTIONS = "(//*[@class='workflow-health']//*[@class='meeting-room-padding-cd0a98b0f8d88ac043f27d7a806873ed'][3]//*[@class='next_btn'])"
    HS_Q4_OPTIONS = "(//*[@class='workflow-health']//*[@class='meeting-room-padding-cd0a98b0f8d88ac043f27d7a806873ed'][4]//*[@class='next_btn'])"
    HS_ERROR_MSG = (By.XPATH, "//*[@class='ant-message-custom-content ant-message-error']//span[text()='Please fill all required data !']")
    
    # Recurring booking
    RecurringBookings_DESK_CHECK_RDIV = "//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]"
    RecurringBookings_DESK_RDIV_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]/parent::*/parent::*/parent::*/parent::*/following-sibling::*/div/div/button[2]"
    RecurringBookings_REPEAT_DIV = (
        By.CLASS_NAME, "css-1d8n9bt")
    RecurringBookings_REPEAT_DAILY = (By.XPATH, f"//*[contains(text(), 'Daily')]")
    RecurringBookings_REPEAT_WEEKLY = (By.XPATH, f"//*[contains(text(), 'Weekly')]")
    RecurringBookings_REPEAT_WEEKLY_DEFAULT_DAY = (By.XPATH, f"//*[contains(text(), 'Wed')]")
    RecurringBookings_REPEAT_WEEKLY_DAY = (By.XPATH, f"//*[contains(text(), 'Wed')]")
    # RecurringBookings_REPEAT_TILL_DATE = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div")
    RecurringBookings_REPEAT_TILL_DATE = (
        By.XPATH, f"//*[contains(text(), 'Ending (on Date)')]/following-sibling::*/child::*/child::*/input")
    RecurringBookings_MULTIPLE_DAYS = (By.XPATH, f"//*[contains(text(), 'Multiple Days')]")
    RecurringBookings_MULTIPLE_DAYS_START_DATE = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/input")
    RecurringBookings_MULTIPLE_DAYS_END_DATE = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/input")

    # MyBookings_EXTEND Booking
    MyBookings_PRE_MyBookings_EXTEND_TIME = "//p[text()='{}']/parent::*/following-sibling::*[1]/div/div"
    MyBookings_CHECKIN_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[1]"
    MyBookings_EXTEND_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2]"
    MyBookings_EXTEND_15_MINS = (By.CSS_SELECTOR, "p[text()='15 minutes']")
    MyBookings_EXTEND_30_MINS = (By.CSS_SELECTOR, "p[text()='30 minutes']")
    MyBookings_EXTEND_45_MINS = (By.CSS_SELECTOR, "p[text()='45 minutes']")
    MyBookings_EXTEND_60_MINS = (By.CSS_SELECTOR, "p[text()='60 minutes']")
    MyBookings_EXTEND_BOOKING_TEXT_CONFIRM = "//p[text()='{}']/parent::*/parent::*/following-sibling::div[2]/div"

    # Calender date selector
    MONTH_SELECTOR = (
        By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div/button[1]")
    MONTH_SELECT = (
        By.XPATH, f"//*[contains(text(), '{TestData.REPEAT_TILL_DATE2[3:5]}')]")
    CDATE_SELECT = (
        By.XPATH, f"//*[contains(text(), '{TestData.REPEAT_TILL_DATE2[:1]}')]")
    CDATE_OK_BTN = (
        By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div[2]/ul/li/button")

    # Logout
    LOGOUT_DROPDOWN = (
        By.XPATH, f"//*[@id='navigation']/div/div/div/div[3]/div/div[2]/div/div[2]/div")
    LOGOUT_BUTTON = (By.XPATH, f"//*[text()='Logout']")

    # Find my colleague
    FMC_SEARCH = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[4]/span/input")
    VIEW_ON_MAP = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[4]/div/div/div/div/div[2]/div[2]/button")

    # Amenities
    EDIT_AMENITIES = (
        By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[2]/div[2]/div")
    PRESENT_AMENITIES = (
        By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div")
    ADD_AMENITIES = (
        By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div/div[4]/div/child::*[2]")
    ADD_AMENITIES_SEARCH = (By.XPATH, "//*[text()='Search']")
    AMENITY_SELECT = (By.XPATH, "//*[contains(text(), 'Dual Monitor')]")
    AMENITIES_QUANTITY_INPUT = (
        By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div/div[4]/div/input")
    AMENITIES_RIGHT_CHECK = (
        By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div/div[4]/div/div[2]/child::*")
    AMENITIES_DONE = (
        By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[2]/div[2]/div")
    AMENITIES_REMOVE = (
        By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div/div[4]/div/child::*[5]")

    # <<=========================================================== Functions ======================================================>>

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for Bookings Page"""

    """selecting location"""

    def select_location(self):
        sleep(3)
        try:
            self.action_chain_click(self.LOCATION_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.GENPACT_IT_PARK)
            sleep(2)
            self.action_chain_click(self.BUSINESS_TOWER)
            sleep(2)
            self.action_chain_click(self.FREE_CLICK)
            assert "Location selection passed"
        except Exception as e:
            print(f"Select_location_room exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_location/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(2)

    def select_days_end_1(self):
        try:
            self.action_chain_click(self.BS_DATE_DIV)
            self.action_chain_click(self.BS_DSINGLE_DAY)
            d1 = TestData.cal_date_format(TestData.BOOKING_DATE)
            dselect = (By.XPATH, self.TDATA_ENDDATE_1.format(d1))
            print(f"End date: {dselect}")
            for i in range(2):
                d_isvisible = self.is_visible(dselect)
                print(f"{i}. visibility: {d_isvisible}")
                if d_isvisible == True:
                    self.action_chain_click(dselect)
                    break
                else:
                    self.action_chain_click(self.CAL_NEXT_MONTH)
            self.scroll_to_element_to_mid(self.BS_DONE)
            sleep(1)
            self.action_chain_click(self.BS_DONE)
            sleep(4)
        except Exception as e:
            print(f"select_days_end exception: {e} \n {traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_days_end_1/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_days_end(self):
        try:
            self.action_chain_click(self.BS_DATE_DIV)
            self.action_chain_click(self.BS_DRecurringBookings_MULTIPLE_DAYS)
            self.action_chain_click(self.BS_DENDDATE)
            print(f"End date: {self.TDATA_ENDDATE}")
            for i in range(2):
                d_isvisible = self.is_visible(self.TDATA_ENDDATE)
                print(f"{i}. visibility: {d_isvisible}")
                if d_isvisible == True:
                    self.action_chain_click(self.TDATA_ENDDATE)
                    break
                else:
                    self.action_chain_click(self.CAL_NEXT_MONTH)
            self.action_chain_click(self.CAL_OK_BUTTON)
            sleep(1)
            self.action_chain_click(self.BS_DONE)
            sleep(4)
        except Exception as e:
            print(f"select_days_end exception: {e}")
            self.take_screenshot(f"deskBooking/select_days_end/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_floor(self):
        try:
            self.action_chain_click(self.SECOND_FLOOR)
            sleep(2)
            assert "Floor selection done"
        except Exception as e:
            print(f"select_floor exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_floor/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_available_status(self):
        try:
            self.action_chain_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.AVAILABLE_STATUS)
            sleep(2)
            assert "Select Available status done"
        except Exception as e:
            print(f"select_available_status exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_available_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
    
    def select_available_resource(self, a=None):
        # self.action_chain_click(self.ROOM_AVAIL)
        try:
            print(f"a:{a}")
            for i in range(1, 6):
                title = self.get_element_text_by_xpath(
                    self.DESK_AVAIL_NAME+str([i]))
                if title not in TestData.DESK_W_ISSUE:
                    if a is None:
                        self.do_click_by_xpath(self.DESK_AVAIL+str([i]))
                    else:
                        self.do_click_by_xpath(self.DESK_AVAIL_NAME+str([a]))
                    break
                else:
                    pass
        except Exception as e:
            print(f"select_available_resource exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_available_resource/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(2)

    def select_booked_status(self):
        try:
            self.action_chain_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.BOOKED_STATUS)
            sleep(2)
            assert "Select Booked status done"
        except Exception as e:
            print(f"select_booked_status exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_booked_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_all_status(self):
        try:
            self.action_chain_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.ALL_STATUS)
            sleep(2)
            assert "Select All status done"
        except Exception as e:
            print(f"select_all_status exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_all_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_resource_type_desk(self):
        try:
            self.action_chain_click(self.RESOURCE_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.RESOURCE_DESKS)
            self.action_chain_click(self.FREE_CLICK)
            sleep(3)
        except Exception as e:
            print(f"select_resource_type exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_resource_type_desk/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def get_desk_name(self):
        try:
            dval = self.get_element_text(self.DESK_NUMBER)
            print("dval: ", dval)
            return dval
        except Exception as e:
            print(f"get_room_name exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/get_desk_name/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def resource_details_page_check(self):
        try:
            self.scroll_to_element(self.ResourceDetails_SCHEDULE_LISTING)
            sleep(2)
            try:
                self.action_chain_click(self.ResourceDetails_I_BUTTON)
                sleep(3)
                eltext = self.get_element_text(self.I_INFO).split('\n')
                print("eltext: ", eltext)
                sleep(3)
                print("At the resource details page, booking should be available: Passed")
            except Exception as e:
                print(f"ResourceDetails_I_BUTTON exce: {e}\n{traceback.format_exc()}")
                self.take_screenshot(f"deskBooking/select_days_end_1/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            self.do_send_keys(self.BODY, Keys.PAGE_UP)
        except Exception as e:
            print(f"resource_details_page_check exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/resource_details_page_check/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def selecting_date(self, btype=None):
        try:
            if btype is None:
                self.date_selection_chain(self.BookResource_DATE_INPUT, TestData.BOOKING_DATE, 2)
            else:
                self.date_selection_chain(self.BookResource_DATE_INPUT, TestData.WEEKLY_RecurringBookings_REPEAT_DATE1, 2)
            dcheck = self.get_element_text(self.BookResource_DATE_INPUT)
            print("dcheck: ", dcheck)
        except Exception as e:
            print(f"selecting_date exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/selecting_date/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_time(self):
        sleep(2)
        try:
            self.time_selection(self.BookResource_TIME_SELECT_START, TestData.TIME_START)
            self.time_selection(self.BookResource_TIME_SELECT_END, TestData.TIME_END)
        except Exception as e:
            print(f"select_time exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/select_time/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def check_my_booking(self):
        try:
            self.action_chain_click(self.MY_BOOKING_NAV)
            sleep(3)
            self.scroll_to_element_to_mid_by_xpath(self.MyBookings_DESK_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = self.get_element_text_by_xpath(
                self.DESK_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            self.do_click_by_xpath(self.MyBookings_DESK_CHECK_DIV)
            sleep(3)
        except Exception as e:
            print(f"check_my_deskbooking exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/check_my_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def resource_page_booking_check(self):
        try:
            rpage_status = self.get_element_text_by_xpath(
                self.DESK_RPAGE_STATUS_CHECK)
            assert rpage_status == "Booked"
            print("rpage_status passed as: ", rpage_status)
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        except Exception as e:
            print(f"resource_page_booking_check exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/resource_page_booking_check/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def resource_details_date_select(self):
        try:
            self.date_selection_chain(
                    self.ResourceDetails_RD_CALENDER_INPUT, TestData.BOOKING_DATE, 2)
        except Exception as e:
            print(f"resource_details_date_select exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/resource_details_date_select/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(2)

    def resource_page_date_select(self):
        try:
            self.action_chain_click(self.DATE_CALENDER_RPAGE)
            sleep(2)
            self.date_selection_chain(
                self.BDATE_RPAGE_INPUT, TestData.BOOKING_DATE, 2)
            dcheck = self.get_element_text(self.BDATE_RPAGE_INPUT)
            # assert dcheck == TestData.BOOKING_DATE
            sleep(2)
            self.action_chain_click(self.BDATE_CALENDER_DONE)
            print("dcheck: ", dcheck)
            sleep(2)
        except Exception as e:
            print(f"resource_page_date_select exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/resource_page_date_select/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def resource_page_multiple_date_select(self):
        try:
            self.action_chain_click(self.DATE_CALENDER_RPAGE)
            sleep(2)
            self.action_chain_click(self.RecurringBookings_MULTIPLE_DAYS)
            sleep(2)
            # self.mdate_selection_chain(self.RecurringBookings_MULTIPLE_DAYS_START_DATE, TestData.BOOKING_DATE1, 8)
            self.action_chain_click(self.RecurringBookings_MULTIPLE_DAYS_END_DATE)
            print("Clicked on multiple days end_date")
            # dcheck = self.get_element_text(self.RecurringBookings_MULTIPLE_DAYS_START_DATE)
            sleep(2)
            vcheck = self.is_enabled(self.MONTH_SELECTOR)
            print("vcheck: ", vcheck)
            self.action_chain_click(self.MONTH_SELECTOR)
            sleep(2)
            self.action_chain_click(self.MONTH_SELECT)
            sleep(2)
            self.action_chain_click(self.CDATE_SELECT)
            sleep(2)
            self.action_chain_click(self.CDATE_OK_BTN)
            # self.mdate_selection_chain(self.RecurringBookings_MULTIPLE_DAYS_END_DATE, TestData.REPEAT_TILL_DATE2, 8)
            # dcheck = self.get_element_text(self.RecurringBookings_MULTIPLE_DAYS_END_DATE)
            # assert dcheck == TestData.BOOKING_DATE
            sleep(2)
            self.action_chain_click(self.BDATE_CALENDER_DONE)
            # print("dcheck: ", dcheck)
            sleep(2)
        except Exception as e:
            print(f"resource_page_multiple_date_select exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/resource_page_multiple_date_select/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def overlapping_error_check(self):
        # Selecting time
        try:
            self.time_selection(self.BookResource_TIME_SELECT_START,
                                TestData.TIME_OVERLAPPING_START)
            self.time_selection(self.BookResource_TIME_SELECT_END,
                                TestData.TIME_OVERLAPPING_END)
            print("Selecting datetime done")
            start_check = self.get_element_text(self.BookResource_TIME_SELECT_START)
            print("startcheck: ", start_check)
            end_check = self.get_element_text(self.BookResource_TIME_SELECT_END)
            print("endcheck: ", end_check)
            sleep(1)
            self.action_chain_click(deskBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
            sleep(1)

            enabled_check = self.is_visible(self.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == True:
                error_msg = self.get_element_text(
                    self.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
            self.driver_get_url(TestData.MY_BOOKING_URL)
            sleep(3)
        except Exception as e:
            print(f"overlapping_error_check: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/overlapping_error_check/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def daily_RecurringBookings_REPEAT(self):
        try:
            self.action_chain_click(self.RecurringBookings_REPEAT_DIV)
            sleep(2)
            self.action_chain_click(self.RecurringBookings_REPEAT_DAILY)
            sleep(2)
            self.date_selection_chain(
                self.RecurringBookings_REPEAT_TILL_DATE, TestData.RecurringBookings_REPEAT_TILL_DATE[:12], 2)
        except Exception as e:
            print(f"daily_RecurringBookings_REPEAT exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/daily_RecurringBookings_REPEAT/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def weekly_RecurringBookings_REPEAT(self):
        try:
            self.action_chain_click(self.RecurringBookings_REPEAT_DIV)
            sleep(2)
            self.action_chain_click(self.RecurringBookings_REPEAT_WEEKLY)
            sleep(2)
            # self.action_chain_click(self.RecurringBookings_REPEAT_WEEKLY_DEFAULT_DAY)
            # sleep(2)
            # self.action_chain_click(self.RecurringBookings_REPEAT_WEEKLY_DAY)
            # sleep(2)
            self.date_selection_chain(
                self.RecurringBookings_REPEAT_TILL_DATE, TestData.WEEKLY_RecurringBookings_REPEAT_TILL_DATE, 2)
        except Exception as e:
            print(f"weekly_RecurringBookings_REPEAT exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/weekly_RecurringBookings_REPEAT/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def MyBookings_EXTEND_booking(self, etime):
        try:
            MyBookings_PRE_MyBookings_EXTEND_TIME = self.get_element_text_by_xpath(
                self.MyBookings_PRE_MyBookings_EXTEND_TIME)
            print("MyBookings_PRE_MyBookings_EXTEND_TIME: ", MyBookings_PRE_MyBookings_EXTEND_TIME)
            self.do_click_by_xpath(self.MyBookings_CHECKIN_BOOKING)
            sleep(12)
            self.do_click_by_xpath(self.MyBookings_EXTEND_BOOKING)
            sleep(5)
            self.action_chain_click(etime)
            sleep(12)
            tMyBookings_EXTEND_confirm = self.get_element_text_by_xpath(
                self.MyBookings_EXTEND_BOOKING_TEXT_CONFIRM)
            print("text: ", tMyBookings_EXTEND_confirm)
            assert tMyBookings_EXTEND_confirm == "In Use, Booking MyBookings_EXTENDed"
            post_MyBookings_EXTEND_time = self.get_element_text_by_xpath(
                self.MyBookings_PRE_MyBookings_EXTEND_TIME)
            print("post_MyBookings_EXTEND_time: ", post_MyBookings_EXTEND_time)
            assert MyBookings_PRE_MyBookings_EXTEND_TIME != post_MyBookings_EXTEND_time
        except Exception as e:
            print(f"MyBookings_EXTEND_booking exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/MyBookings_EXTEND_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def do_logout(self):
        try:
            self.action_chain_click(self.LOGOUT_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.LOGOUT_BUTTON)
        except Exception as e:
            print(f"do_logout exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/do_logout/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def start_selection(self):
        try:
            sleep(3)
            print("Selecting Location")
            self.select_location()
            print("Selecting Floor")
            self.select_floor()
            # Checking available resources
            self.select_available_status()
            # Selecting resource type
            self.select_resource_type_desk()
            # Clicking on list view
            self.action_chain_click(self.LIST_VIEW_BUTTON)
            sleep(3)
        except Exception as e:
            print(f"start_selection exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/start_selection/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def update_health_status(self):
        try:
            val = self.is_enabled(self.HEALTH_STATUS_PROMPT)
            if val == 1:
                self.action_chain_click(self.HEALTH_STATUS_PROMPT)
                sleep(2)
                self.action_chain_click(self.UPDATE_HEALTH_STATUS_BUTTON)
                sleep(2)
                self.action_chain_click(self.FULLY_VACCINATED)
                sleep(2)
                self.action_chain_click(self.HEALTH_CONDITION_NONE)
                sleep(2)
                self.action_chain_click(self.PROVIDING_CARE_NO)
                sleep(2)
                self.action_chain_click(self.CONTACT_14DAYS_NO)
                sleep(2)
                self.action_chain_click(self.OFFICE_TO_VISIT_DROPDOWN)
                sleep(2)
                self.action_chain_click(self.OFFICE_TO_VISIT_SELECT)
                sleep(2)
                self.action_chain_click(self.CONFIRM_DECLARATION)
                sleep(2)
                self.action_chain_click(self.BOOK_SPACE_NAV)
                sleep(2)
                self.action_chain_click(self.DESK)
            else:
                pass
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")


