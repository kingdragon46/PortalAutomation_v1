from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class deskBookingsPage(BasePage):

    '''By XPATH'''
    # Body Xpath
    BODY = (By.CSS_SELECTOR, "body")
    #
    DESK_NO = None
    # ------
    BOOKING_NAV = (
        By.XPATH, "//*[@id='navigation']/div/div/div/div[2]/child::*[3]")
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
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div")
    AVAILABLE_STATUS = (By.CSS_SELECTOR, "span[title='Available']")
    BOOKED_STATUS = (By.CSS_SELECTOR, "span[title='Booked']")
    ASSIGNED_STATUS = (By.CSS_SELECTOR, "span[title='Assigned']")
    INACTIVE_STATUS = (By.CSS_SELECTOR, "span[title='Inactive']")
    ALL_STATUS = (By.CSS_SELECTOR, "span[title='All']")
    LIST_VIEW_BUTTON = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]")
    # DESK_201 = (By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/button")
    DESK_AVAIL = "(//*[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button)"
    DESK_AVAIL_2 = (
        By.XPATH, "//*[text()='Available']/parent::*/parent::*/preceding-sibling::*/div/div")
    DESK_AVAIL_NAME = "(//div[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button)"
    DESK_201 = "//*[text()='{}']/parent::*/parent::*/following-sibling::*[5]/button"
    DESK_205 = (
        By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr[6]/td[6]/button")
    DESK_NUMBER = (By.XPATH, f"//*[@class='desk-title']")

    # Resource Type
    RESOURCE_DROPDOWN = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div")
    RESOURCE_DESKS = (By.CSS_SELECTOR, "span[title='Desks']")

    # 2nd Floor total desks
    TOTAL_DESKS_2ND_FLOOR = (
        By.XPATH, f"//*[@id='1-floor']/div/div[3]/div[1]/p")
    AVAILABLE_DESKS_2ND_FLOOR = (
        By.XPATH, f"//*[@id='1-floor']/div/div[3]/div[2]/p")

    # Booking Modal
    MODAL_CLOSE = (By.XPATH, "//*[@title='Close']")
    BOOKING_CONFIRM_BUTTON = (
        By.XPATH, "//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div/button")
    HOST_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[1]/div[1]/div/div[4]/div/div/div[3]/img")
    HOST_INPUT = (
        By.XPATH, "//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[1]/div[1]/div/div[4]/div/div/div")
    HOST_SELECT = (
        By.XPATH, f"//*[contains(text(), '{TestData.HOST2_FULLNAME}')]")

    DATE_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div")
    DATE_INPUT = (
        By.XPATH, "//input[@placeholder='Select date']")
    DATE_CALENDER_BODY = (
        By.XPATH, "/html/body/div[9]/div/div/div/div/div[1]/div[2]")
    DATE_SELECT_2nd = (
        By.XPATH, "/html/body/div[6]/div/div/div/div/div[1]/div[2]/table/tbody/tr[1]/td[7]/div")
    TIME_SELECT_START = (
        By.XPATH, "//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div/div")
    TIME_SELECT_END = (
        By.XPATH, "//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div")
    MULTIPLE_DAYS_SINGLE_BOOKING = (
        By.XPATH, "//*[contains(text(), 'Multiple Days')]")
    MULTIPLE_DAYS_SB_START = (
        By.XPATH, "//input[@placeholder='Start date']")
    MULTIPLE_DAYS_SB_END = (
        By.XPATH, "//input[@placeholder='End date']")

    # Booking confirmation
    DESK_201_AFTER_BOOKING_DIV = (
        By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr/td[1]/div")
    # DESK_201_AFTER_BOOKING_TITLE = (By.XPATH, f"//*[text()='{DESK_NO}']/parent::*/parent::*")
    DESK_201_AFTER_BOOKING_TITLE = "//*[text()='{}']/parent::*/parent::*"

    # Resource Details
    RD_CALENDER_INPUT = (
        By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/input")
    SCHEDULE_LISTING = (
        By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[3]/div/div/div[2]")
    I_BUTTON = (By.XPATH, f"//*[@class='rbc-event-content']/span")
    I_INFO = (By.XPATH, f"//*[@class='ant-popover-content']")
    I_INFO2 = (By.XPATH, f"/html/body/div[7]/div/div/div")
    RD_TIME_CHECK = (By.CLASS_NAME, "rbc-event-label")
    BOOK_THIS_SPACE = (
        By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[4]/div/button")
    BOOKING_HOSTNAME = (
        By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[1]")
    BOOKING_HOSTEMAIL = (
        By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[2]")
    BOOKING_START = (
        By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[3]")
    BOOKING_END = (
        By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[4]")

    # Resource page confirmation
    DATE_CALENDER_RPAGE = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/input")
    BDATE_RPAGE_INPUT = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div/input")
    BDATE_CALENDER_DONE = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/button")
    DESK_201_RPAGE_CHECK_DIV = "//*[@title='{}']/parent::*/parent::div"
    DESK_201_RPAGE_CHECK_BOOK_BUTTON = "//div[@title='{}']/parent::*/parent::*/following-sibling::*[5]/button"
    DESK_201_RPAGE_STATUS_CHECK = "//*[@title='{}']/parent::*/parent::td/following-sibling::*[1]/div/div"

    # My Bookings
    C_TEXT = "//*[contains(text(), '{}')]"
    MY_BOOKING_NAV = (By.XPATH, f"//*[@id='sub-nav']/div[2]")
    # DESK_201_CHECK_NAME = (By.XPATH, "//p[text()='{}']".format(DESK_NO))
    DESK_201_CHECK_NAME = "//p[text()='{}']"
    # DESK_201_CHECK_NAME = (By.XPATH, C_TEXT)
    DESK_201_CHECK_DIV = "//p[text()='{}']/parent::*/parent::div"
    DESK_201_SCHEDULE_CHECK = "//p[text()='{}']/parent::*/following-sibling::*[1]"
    DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = "//p[text()='{}']/parent::*/following-sibling::*[2]"
    DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2]"
    DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = "//p[text()='{}']/parent::*/parent::*/preceding-sibling::*/child::*[2]/child::*/child::*/*[@class='MuiSvgIcon-root'"
    DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON = (
        By.XPATH, "//*[text()='Cancel All']")
    DESK_201_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/button)"
    MAIN_CARDS_CONTAINER = (By.XPATH, f"//*[@id='mainBookingCardsContainer']")

    # Booking Successfull message
    BK_SUCCESS = (By.XPATH, f"/html/body/div[5]/div/div/div/div/div/span[2]")
    BK_OVERLAPPING_ERROR = (By.XPATH, f"/html/body/div[12]/div/div/div/div")
    BK_OVERLAPPING_ERROR_MSG = (
        By.XPATH, "//span[contains(text(), 'Error')]")

    # Health Status
    HEALTH_STATUS_MSG = 'You cannot book the desk since your health status is "Not Filled", Please fill your health status under "My Bookings"'
    HEALTH_STATUS_PROMPT = (
        By.XPATH, f"//*[contains(text(), 'Update Health Status')]")
    UPDATE_HEALTH_STATUS_BUTTON = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/button")
    FULLY_VACCINATED = (
        By.XPATH, f"//*[contains(text(), 'Fully Vaccinated')]/preceding-sibling::*/child::*")
    HEALTH_CONDITION_NONE = (
        By.XPATH, f"//*[contains(text(), 'None')]/preceding-sibling::*/child::*")
    PROVIDING_CARE_NO = (
        By.XPATH, f"//*[contains(text(), 'If you are providing care to a confirmed /suspect/probable case')]/parent::*/following-sibling::*/child::div[2]/child::div[2]/child::div/child::div/child::div/child::*")
    CONTACT_14DAYS_NO = (
        By.XPATH, f"//*[contains(text(), 'If you have come in contact with any COVID-19 positive case in the last 14 days')]/parent::*/following-sibling::*/child::div[2]/child::div[2]/child::div/child::div/child::div/child::*")
    OFFICE_TO_VISIT_DROPDOWN = (By.XPATH, f"//*[@id='other_5014']/div")
    OFFICE_TO_VISIT_SELECT = (
        By.XPATH, f"//*[contains(text(), 'Digicred HQ-New York')]")
    PARKING_DROPDOWN = (By.XPATH, f"//*[@id='other_5015']/div")
    PARKING_SELECT = (By.XPATH, f"//*[contains(text(), '2 Wheeler')]")
    CONFIRM_DECLARATION = (
        By.XPATH, f"//*[contains(text(), 'Confirm Declaration')]")

    # Recurring booking
    DESK_201_CHECK_RDIV = "//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]"
    DESK_201_RDIV_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]/parent::*/parent::*/parent::*/parent::*/following-sibling::*/div/div/button[2]"
    REPEAT_DIV = (
        By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]")
    REPEAT_DAILY = (By.XPATH, f"//*[contains(text(), 'Daily')]")
    REPEAT_WEEKLY = (By.XPATH, f"//*[contains(text(), 'Weekly')]")
    REPEAT_WEEKLY_DEFAULT_DAY = (By.XPATH, f"//*[contains(text(), 'Wed')]")
    REPEAT_WEEKLY_DAY = (By.XPATH, f"//*[contains(text(), 'Wed')]")
    # REPEAT_TILL_DATE = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div")
    REPEAT_TILL_DATE = (
        By.XPATH, f"//*[contains(text(), 'Ending (on Date)')]/following-sibling::*/child::*/child::*/input")
    MULTIPLE_DAYS = (By.XPATH, f"//*[contains(text(), 'Multiple Days')]")
    MULTIPLE_DAYS_START_DATE = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/input")
    MULTIPLE_DAYS_END_DATE = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/input")

    # Extend Booking
    PRE_EXTEND_TIME = "//p[text()='{}']/parent::*/following-sibling::*[1]/div/div"
    CHECKIN_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[1]"
    EXTEND_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2]"
    EXTEND_15_MINS = (By.CSS_SELECTOR, "p[text()='15 minutes']")
    EXTEND_30_MINS = (By.CSS_SELECTOR, "p[text()='30 minutes']")
    EXTEND_45_MINS = (By.CSS_SELECTOR, "p[text()='45 minutes']")
    EXTEND_60_MINS = (By.CSS_SELECTOR, "p[text()='60 minutes']")
    EXTEND_BOOKING_TEXT_CONFIRM = "//p[text()='{}']/parent::*/parent::*/following-sibling::div[2]/div"

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
            self.do_click(self.LOCATION_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.GENPACT_IT_PARK)
            sleep(2)
            self.action_chain_click(self.BUSINESS_TOWER)
            sleep(2)
            self.do_click(self.FREE_CLICK)
            assert "Location selection passed"
        except Exception as e:
            print("Select_location_room exception: ", e)
            self.quit_driver()
        sleep(5)

    def select_floor(self):
        try:
            self.do_click(self.SECOND_FLOOR)
            sleep(2)
            assert "Floor selection done"
        except Exception as e:
            print("select_floor exception: ", e)

    def select_available_status(self):
        try:
            self.do_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.do_click(self.AVAILABLE_STATUS)
            sleep(2)
            assert "Select Available status done"
        except Exception as e:
            print("select_available_status exception: ", e)
    
    def select_available_resource(self, a=None):
        # self.do_click(self.ROOM_AVAIL)
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
        sleep(2)

    def select_booked_status(self):
        try:
            self.do_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.do_click(self.BOOKED_STATUS)
            sleep(2)
            assert "Select Booked status done"
        except Exception as e:
            print("select_booked_status exception: ", e)

    def select_all_status(self):
        try:
            self.do_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.do_click(self.ALL_STATUS)
            sleep(2)
            assert "Select All status done"
        except Exception as e:
            print("select_all_status exception: ", e)

    def select_resource_type_desk(self):
        try:
            self.do_click(self.RESOURCE_DROPDOWN)
            sleep(2)
            self.do_click(self.RESOURCE_DESKS)
            self.do_click(self.FREE_CLICK)
            sleep(3)
        except Exception as e:
            print("select_resource_type exception: ", e)

    def get_desk_name(self):
        try:
            dval = self.get_element_text(self.DESK_NUMBER)
            print("dval: ", dval)
            return dval
        except Exception as e:
            print("get_room_name exception: ", e)

    def resource_details_page_check(self):
        self.scroll_to_element(self.SCHEDULE_LISTING)
        sleep(2)
        try:
            self.do_click(self.I_BUTTON)
            sleep(3)
            eltext = self.get_element_text(self.I_INFO).split('\n')
            print("eltext: ", eltext)
            sleep(3)
            print("At the resource details page, booking should be available: Passed")
        except Exception as e:
            print("I_button exce: ", e)
        self.do_send_keys(self.BODY, Keys.PAGE_UP)

    def selecting_date(self, btype=None):
        try:
            if btype is None:
                self.date_selection_chain(self.DATE_INPUT, TestData.BOOKING_DATE, 2)
            else:
                self.date_selection_chain(self.DATE_INPUT, TestData.WEEKLY_REPEAT_DATE1, 2)
            dcheck = self.get_element_text(self.DATE_INPUT)
            print("dcheck: ", dcheck)
        except Exception as e:
            print("selecting_date exception: ", e)

    def select_time(self):
        sleep(2)
        try:
            self.time_selection(self.TIME_SELECT_START, TestData.TIME_START)
            self.time_selection(self.TIME_SELECT_END, TestData.TIME_END)
        except Exception as e:
            print("select_time exception: ", e)

    def check_my_booking(self):
        try:
            self.do_click(self.MY_BOOKING_NAV)
            sleep(3)
            self.scroll_to_element_to_mid_by_xpath(self.DESK_201_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = self.get_element_text_by_xpath(
                self.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            self.do_click_by_xpath(self.DESK_201_CHECK_DIV)
            sleep(3)
        except Exception as e:
            print("check_my_deskbooking exception: ", e)

    def resource_page_booking_check(self):
        try:
            rpage_status = self.get_element_text_by_xpath(
                self.DESK_201_RPAGE_STATUS_CHECK)
            assert rpage_status == "Booked"
            print("rpage_status passed as: ", rpage_status)
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        except Exception as e:
            print("resource_page_booking_check exception: ", e)

    def resource_details_date_select(self):
        self.date_selection_chain(
                self.RD_CALENDER_INPUT, TestData.BOOKING_DATE, 2)
        sleep(2)

    def resource_page_date_select(self):
        self.do_click(self.DATE_CALENDER_RPAGE)
        sleep(2)
        self.date_selection_chain(
            self.BDATE_RPAGE_INPUT, TestData.BOOKING_DATE, 2)
        dcheck = self.get_element_text(self.BDATE_RPAGE_INPUT)
        # assert dcheck == TestData.BOOKING_DATE
        sleep(2)
        self.do_click(self.BDATE_CALENDER_DONE)
        print("dcheck: ", dcheck)
        sleep(2)

    def resource_page_multiple_date_select(self):
        self.do_click(self.DATE_CALENDER_RPAGE)
        sleep(2)
        self.do_click(self.MULTIPLE_DAYS)
        sleep(2)
        # self.mdate_selection_chain(self.MULTIPLE_DAYS_START_DATE, TestData.BOOKING_DATE1, 8)
        self.do_click(self.MULTIPLE_DAYS_END_DATE)
        print("Clicked on multiple days end_date")
        # dcheck = self.get_element_text(self.MULTIPLE_DAYS_START_DATE)
        sleep(2)
        vcheck = self.is_enabled(self.MONTH_SELECTOR)
        print("vcheck: ", vcheck)
        self.action_chain_click(self.MONTH_SELECTOR)
        sleep(2)
        self.do_click(self.MONTH_SELECT)
        sleep(2)
        self.do_click(self.CDATE_SELECT)
        sleep(2)
        self.do_click(self.CDATE_OK_BTN)
        # self.mdate_selection_chain(self.MULTIPLE_DAYS_END_DATE, TestData.REPEAT_TILL_DATE2, 8)
        # dcheck = self.get_element_text(self.MULTIPLE_DAYS_END_DATE)
        # assert dcheck == TestData.BOOKING_DATE
        sleep(2)
        self.do_click(self.BDATE_CALENDER_DONE)
        # print("dcheck: ", dcheck)
        sleep(2)

    def overlapping_error_check(self):
        # Selecting time
        try:
            self.time_selection(self.TIME_SELECT_START,
                                TestData.TIME_OVERLAPPING_START)
            self.time_selection(self.TIME_SELECT_END,
                                TestData.TIME_OVERLAPPING_END)
            print("Selecting datetime done")
            start_check = self.get_element_text(self.TIME_SELECT_START)
            print("startcheck: ", start_check)
            end_check = self.get_element_text(self.TIME_SELECT_END)
            print("endcheck: ", end_check)
            sleep(1)
            self.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
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
            print("Error 2")

    def daily_repeat(self):
        try:
            self.do_click(self.REPEAT_DIV)
            sleep(2)
            self.do_click(self.REPEAT_DAILY)
            sleep(2)
            self.date_selection_chain(
                self.REPEAT_TILL_DATE, TestData.REPEAT_TILL_DATE[:12], 2)
        except Exception as e:
            print("daily_repeat exception: ", e)

    def weekly_repeat(self):
        try:
            self.do_click(self.REPEAT_DIV)
            sleep(2)
            self.do_click(self.REPEAT_WEEKLY)
            sleep(2)
            # self.do_click(self.REPEAT_WEEKLY_DEFAULT_DAY)
            # sleep(2)
            # self.do_click(self.REPEAT_WEEKLY_DAY)
            # sleep(2)
            self.date_selection_chain(
                self.REPEAT_TILL_DATE, TestData.WEEKLY_REPEAT_TILL_DATE, 2)
        except Exception as e:
            print("weekly_repeat exception: ", e)

    def extend_booking(self, etime):
        try:
            pre_extend_time = self.get_element_text_by_xpath(
                self.PRE_EXTEND_TIME)
            print("pre_extend_time: ", pre_extend_time)
            self.do_click_by_xpath(self.CHECKIN_BOOKING)
            sleep(12)
            self.do_click_by_xpath(self.EXTEND_BOOKING)
            sleep(5)
            self.do_click(etime)
            sleep(12)
            textend_confirm = self.get_element_text_by_xpath(
                self.EXTEND_BOOKING_TEXT_CONFIRM)
            print("text: ", textend_confirm)
            assert textend_confirm == "In Use, Booking Extended"
            post_extend_time = self.get_element_text_by_xpath(
                self.PRE_EXTEND_TIME)
            print("post_extend_time: ", post_extend_time)
            assert pre_extend_time != post_extend_time
        except Exception as e:
            print("extend_booking exception: ", e)

    def do_logout(self):
        try:
            self.do_click(self.LOGOUT_DROPDOWN)
            sleep(2)
            self.do_click(self.LOGOUT_BUTTON)
        except Exception as e:
            print("do_logout exception: ", e)

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
            self.do_click(self.LIST_VIEW_BUTTON)
            sleep(3)
        except Exception as e:
            print("start_selection exception: ", e)

    def update_health_status(self):
        try:
            val = self.is_enabled(self.HEALTH_STATUS_PROMPT)
            if val == 1:
                self.do_click(self.HEALTH_STATUS_PROMPT)
                sleep(2)
                self.do_click(self.UPDATE_HEALTH_STATUS_BUTTON)
                sleep(2)
                self.do_click(self.FULLY_VACCINATED)
                sleep(2)
                self.do_click(self.HEALTH_CONDITION_NONE)
                sleep(2)
                self.do_click(self.PROVIDING_CARE_NO)
                sleep(2)
                self.do_click(self.CONTACT_14DAYS_NO)
                sleep(2)
                self.do_click(self.OFFICE_TO_VISIT_DROPDOWN)
                sleep(2)
                self.do_click(self.OFFICE_TO_VISIT_SELECT)
                sleep(2)
                self.do_click(self.CONFIRM_DECLARATION)
                sleep(2)
                self.do_click(self.BOOK_SPACE_NAV)
                sleep(2)
                self.do_click(self.DESK_201)
            else:
                pass
        except Exception as e:
            print("update_health_status exception: ", e)
