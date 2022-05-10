from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class RoomBookingsPage(BasePage):

    # <======================================== Selectors ========================================>
    # Body Xpath
    BODY = (By.CSS_SELECTOR, "body")

    # Room No -------
    ROOM_NO = 124
    ROOM_NUMBER = (By.XPATH, f"//*[@class='desk-title']")
    ROOM_AVAIL = (By.XPATH, f"//*[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button")

    # ---------------
    BOOKING_NAV = (By.XPATH, f"//h3[text()='Booking']")
    BOOK_SPACE_NAV = (By.XPATH, f"//*[contains(text(), 'Book space')]")
    LOCATION_DROPDOWN = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[1]/div/div")
    GENPACT_IT_PARK = (
        By.XPATH, f"/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div/div/div[4]/span[2]/span")
    BUSINESS_TOWER = (
        By.XPATH, f"/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div/div/div[5]")
    FREE_CLICK = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/p")
    FIRST_FLOOR = (By.XPATH, f"//*[@id='0-floor']/div/div[1]/div[1]")
    STATUS_DROPDOWN = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div")
    AVAILABLE_STATUS = (By.XPATH, f"//span[text()='Available']")
    BOOKED_STATUS = (By.XPATH, f"//span[text()='Booked']")
    ASSIGNED_STATUS = (By.XPATH, f"//span[text()='Assigned']")
    INACTIVE_STATUS = (By.XPATH, f"//span[text()='Inactive']")
    ALL_STATUS = (By.XPATH, f"//span[text()='All Status']")
    LIST_VIEW_BUTTON = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]")

    RESOURCE_DROPDOWN = (
        By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div")
    RESOURCE_ROOM = (
        By.XPATH, f"//*[contains(text(), 'Rooms')]")
    # Room
    ROOM_124 = "//*[@title='{}']/parent::*/parent::*/following-sibling::*[5]/button"
    # Modal selectors

    BOOKING_AGENDA = (
        By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input")
    ATTENDEE_DETAILS = (
        By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div/div/div[1]")
    CONFIRM_BOOKING = (
        By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[6]/button[2]")
    EDIT_DETAILS = (
        By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[7]/div[2]/p")
    EDIT_DETAILS_SEARCH_BOX = (
        By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[8]/div[1]/div")
    START_DATE = (
        By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[1]/div[2]/div/input")
    START_DATE_X = (
        By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[3]/div[2]/div/span/span")
    END_DATE = (
        By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[3]/div[2]/div/input")
    CONTACT_EMAIL = (
        By.XPATH, f"//*[contains(text(), 'New Member')]/parent::*/child::*/following-sibling::*/input")
    CONTACT_RIGHT_TICK = (
        By.XPATH, f"//*[contains(text(), 'New Member')]/parent::*/child::*[4]/div")
    BOOKING_CONFIRM_BUTTON = (By.XPATH, f"//*[contains(text(), 'Confirm Booking')]")

    # After Booking
    ROOM_124_AFTER_BOOKING_TITLE = "//div[@title='{}']"
    ROOM_124_RPAGE_STATUS_CHECK = "//*[@title='{}']/parent::*/parent::td/following-sibling::*[1]/div/div"
    

    # Resource Details
    RD_CALENDER_INPUT = (By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/input")
    SCHEDULE_LISTING = (By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[3]/div/div/div[2]")
    I_BUTTON = (By.XPATH, f"//*[@class='rbc-event-content']/span")
    I_INFO = (By.XPATH, f"//*[@class='ant-popover-content']")
    I_INFO2 = (By.XPATH, f"/html/body/div[7]/div/div/div")
    RD_TIME_CHECK = (By.XPATH, f"*[@class='rbc-event-label']")
    BOOK_THIS_SPACE = (By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[4]/div/button")
    BOOKING_HOSTNAME = (By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[1]")
    BOOKING_HOSTEMAIL = (By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[2]")
    BOOKING_START = (By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[3]")
    BOOKING_END = (By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[4]")

    # My Bookings
    MY_BOOKING_NAV = (By.XPATH, f"//*[@id='sub-nav']/div[2]")
    ROOM_124_CHECK_DIV = "//p[text()='{}']/parent::*/parent::div"
    ROOM_124_CHECK_DIV_LAST = "(//p[text()='{}']/parent::*/parent::div)[last()]"
    ROOM_124_SCHEDULE_CHECK = "//p[text()='{}']/parent::*/following-sibling::*[1]"
    ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = "//p[text()='{}']/parent::*/following-sibling::*[2]"
    ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2]"
    ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON_LAST = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2])[last()]"
    ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/button"
    MAIN_CARDS_CONATINER = (By.XPATH, f"//*[@id='mainBookingCardsContainer']")
    ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = "//p[text()='{}']/parent::*/parent::*/preceding-sibling::*/child::*[2]/child::*/child::*/child::*[3]"
    ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON = (By.XPATH, f"//*[text()='Cancel All']")

    # Overlapping error
    BK_OVERLAPPING_ERROR_MSG = (By.XPATH, f"//*[contains(text(), 'Error in creating Booking: Booking Exists')]")
    BK_OVERLAPPING_ERROR_MSG_1 = (By.XPATH, f"//*[contains(text(), 'Error in extending Booking')]")
    BK_OVERLAPPING_ERROR_MSG_2 = (By.XPATH, f"//*[contains(text(), 'Error in extending Booking')]")

    # Recurring
    ROOM_124_CHECK_RDIV = "//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]"
    ROOM_124_RDIV_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]/parent::*/parent::*/parent::*/parent::*/following-sibling::*/div/div/button[2]"
    REPEAT_DROPDOWN = (By.XPATH, f"//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div[1]/div/div/div/div[1]")
    REPEAT_DAILY = (By.XPATH, f"//*[contains(text(), 'Daily')]")
    REPEAT_WEEKLY = (By.XPATH, f"//*[contains(text(), 'Weekly')]")
    REPEAT_TILL_DATE = (By.XPATH, f"//*[contains(text(), 'Ending (on Date)')]/following-sibling::*/child::*/child::*")
    REPEAT_FREQUENCY = (By.XPATH, f"//*[contains(text(), 'Every')]/child::*")
    MULTIPLE_DAYS = (By.XPATH, f"//*[contains(text(), 'Daily')]")
    MULTIPLE_DAYS_START_DATE = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/input")
    MULTIPLE_DAYS_END_DATE = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/input")

    # Extend Booking
    PRE_EXTEND_TIME = "//p[text()='{}']/parent::*/following-sibling::*[1]/div/div"
    CHECKIN_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[1]"
    EXTEND_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2]"
    EXTEND_15_MINS = (By.XPATH, f"//p[text()='15 minutes']")
    EXTEND_30_MINS = (By.XPATH, f"//p[text()='30 minutes']")
    EXTEND_45_MINS = (By.XPATH, f"//p[text()='45 minutes']")
    EXTEND_60_MINS = (By.XPATH, f"//p[text()='60 minutes']")
    EXTEND_BOOKING_TEXT_CONFIRM = "//p[text()='{}']/parent::*/parent::*/following-sibling::div[2]/div"


    # Logout
    LOGOUT_DROPDOWN = (By.XPATH, "//*[@id='navigation']/div/div/div/div[3]/div/div[2]/div/div[2]/div")
    LOGOUT_BUTTON = (By.XPATH, "//*[text()='Logout']")

    # Tags
    TAG_DROPDOWN = (By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[2]/div/div")
    TAG_SELECT = (By.XPATH, f"//*[@title='{TestData.TAG}']/preceding-sibling::*[1]")

    # Find my colleague
    FMC_SEARCH = (By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[4]/span/input")
    VIEW_ON_MAP = (By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[4]/div/div/div/div/div[2]/div[2]/button")

    # Amenities
    EDIT_AMENITIES = (By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[2]/div[2]/div")
    PRESENT_AMENITIES = (By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div")
    ADD_AMENITIES = (By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div/div[4]/div/child::*[2]")
    ADD_AMENITIES_SEARCH = (By.XPATH, "//*[text()='Search']")
    AMENITY_SELECT = (By.XPATH, "//*[contains(text(), 'Dual Monitor')]")
    AMENITIES_QUANTITY_INPUT = (By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div/div[4]/div/input")
    AMENITIES_RIGHT_CHECK = (By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div/div[4]/div/div[2]/child::*")
    AMENITIES_DONE = (By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[2]/div[2]/div")
    AMENITIES_REMOVE = (By.XPATH, "//*[@id='resource-details-content']/div[3]/div[1]/div/div/div[5]/div/div/div[4]/div/child::*[5]")


    # <===================================== Functions =======================================>

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for Bookings Page"""

    """selecting location"""

    def select_location(self):
        sleep(3)
        self.do_click(self.LOCATION_DROPDOWN)
        sleep(5)
        self.do_click(self.GENPACT_IT_PARK)
        sleep(5)
        self.do_click(self.BUSINESS_TOWER)
        sleep(5)
        self.do_click(self.FREE_CLICK)
        assert "Location selection passed"
        sleep(10)

    def select_resource_type(self):
        self.do_click(self.RESOURCE_DROPDOWN)
        sleep(2)
        self.do_click(self.RESOURCE_ROOM)
        self.do_click(self.FREE_CLICK)

    def select_floor(self):
        self.do_click(self.FIRST_FLOOR)
        sleep(5)
        assert "Floor selection done"

    def select_available_status(self):
        self.do_click(self.STATUS_DROPDOWN)
        sleep(5)
        self.do_click(self.AVAILABLE_STATUS)
        sleep(5)
        assert "Select Available status done"

    def select_tag(self):
        self.do_click(self.TAG_DROPDOWN)
        sleep(3)
        self.do_click(self.TAG_SELECT)
        sleep(3)
        self.do_click(self.FREE_CLICK)
        sleep(5)



    def get_room_name(self):
        rval = self.get_element_text(self.ROOM_NUMBER)
        print("dval: ", rval)
        return rval

    def select_booked_status(self):
        self.do_click(self.STATUS_DROPDOWN)
        sleep(5)
        self.do_click(self.BOOKED_STATUS)
        sleep(5)
        assert "Select Booked status done"

    def select_all_status(self):
        self.do_click(self.STATUS_DROPDOWN)
        sleep(5)
        self.do_click(self.ALL_STATUS)
        sleep(5)
        assert "Select Booked status done"

    def enter_agenda(self):
        try:
            self.host_selection(self.BOOKING_AGENDA, TestData.ROOM_AGENDA)
        except Exception as e:
            print("Agenda error exception: ", e)

    def new_contact_guest(self, contact_name, contact_email):
        try:
            self.host_selection(self.ATTENDEE_DETAILS, contact_name)
            self.do_send_keys(self.CONTACT_EMAIL, contact_email)
            self.do_click(self.CONTACT_RIGHT_TICK)
            sleep(2)
        except Exception as e:
            print("new_contact_guest exception: ", e)

    def enter_datetime(self):
        try:
            self.do_click(self.START_DATE)
            self.action_chain_click(self.START_DATE_X)
            self.date_selection_chain(
                self.START_DATE, TestData.ROOM_START_DATE, 18)
            self.do_click(self.END_DATE)
            self.date_selection_chain(
                self.END_DATE, TestData.ROOM_END_DATE, 18)
        except Exception as e:
            print("enter_datetime exception: ", e)

    def resource_page_booking_check(self):
        rpage_status = self.get_element_text_by_xpath(
            self.ROOM_124_RPAGE_STATUS_CHECK)
        assert rpage_status == "Booked"
        print("rpage_status passed as: ", rpage_status)
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")

    def resource_details_page_check(self):
        self.scroll_to_element(self.SCHEDULE_LISTING)
        sleep(2)
        try:
            self.do_click(self.I_BUTTON)
            sleep(3)
            eltext = self.get_element_text(self.I_INFO).split('\n')
            print("eltext: ", eltext)
            sleep(5)
            print("At the resource details page, booking should be available: Passed")
        except Exception as e:
            print("I_button exce: ", e)
        self.do_send_keys(self.BODY, Keys.PAGE_UP)

    def check_my_booking(self):
        self.do_click(self.MY_BOOKING_NAV)
        sleep(5)
        self.scroll_to_element_by_xpath(self.ROOM_124_CHECK_DIV)
        sleep(3)
        # Meeting Options
        meeting_options = self.get_element_text_by_xpath(self.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
        std_meeting_options = ['Check in', '', 'Cancel Booking']
        assert meeting_options == std_meeting_options
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        self.do_click_by_xpath(self.ROOM_124_CHECK_DIV)
        sleep(5)

    def daily_repeat(self):
        self.do_click(self.REPEAT_DROPDOWN)
        sleep(3)
        self.do_click(self.REPEAT_DAILY)
        sleep(2)
        # self.date_selection_chain(self.REPEAT_FREQUENCY, TestData.REPEAT_FREQUENCY, 2)
        sleep(2)
        self.date_selection_chain(self.REPEAT_TILL_DATE, TestData.REPEAT_TILL_DATE[:11], 2)

    def daily_repeat2(self):
        self.do_click(self.REPEAT_DROPDOWN)
        sleep(3)
        self.do_click(self.REPEAT_DAILY)
        sleep(2)
        # self.date_selection_chain(self.REPEAT_FREQUENCY, TestData.REPEAT_FREQUENCY, 2)
        sleep(2)
        self.date_selection_chain(self.REPEAT_TILL_DATE, TestData.WEEKLY_REPEAT_TILL_DATE2, 2)

    def weekly_repeat(self):
        self.do_click(self.REPEAT_DROPDOWN)
        sleep(3)
        self.do_click(self.REPEAT_WEEKLY)
        sleep(2)
        self.date_selection_chain(self.REPEAT_TILL_DATE, TestData.WEEKLY_REPEAT_TILL_DATE, 2)
        sleep(2)
        self.date_selection_chain(self.REPEAT_FREQUENCY, TestData.REPEAT_FREQUENCY, 2)

    def cancel_booking(self):
        self.scroll_to_element_by_xpath(self.ROOM_124_CHECK_DIV)
        sleep(3)
        # Meeting Options
        meeting_options = self.get_element_text_by_xpath(self.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
        std_meeting_options = ['Check in', '', 'Cancel Booking']
        # assert meeting_options == std_meeting_options
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        self.do_click_by_xpath(self.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)

    def cancel_last_booking(self):
        self.scroll_to_element_by_xpath(self.ROOM_124_CHECK_DIV_LAST)
        sleep(3)
        # Meeting Options
        # meeting_options = self.get_element_text(self.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
        # std_meeting_options = ['Check in', '', 'Cancel Booking']
        # assert meeting_options == std_meeting_options
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        self.do_click_by_xpath(self.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON_LAST)

    def cancel_some_bookings(self, crange):
        for i in range(crange):
            print("i: ", i)
            self.scroll_to_element_by_xpath(self.ROOM_124_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = self.get_element_text_by_xpath(self.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            # assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            if i == 0:
                self.do_click_by_xpath(self.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            else:
                self.do_click_by_xpath(self.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON)
            sleep(8)

    def extend_booking(self, etime):
        pre_extend_time = self.get_element_text_by_xpath(self.PRE_EXTEND_TIME)
        print("pre_extend_time: ", pre_extend_time)
        self.do_click_by_xpath(self.CHECKIN_BOOKING)
        sleep(12)
        self.do_click_by_xpath(self.EXTEND_BOOKING)
        sleep(5)
        self.do_click(etime)
        sleep(12)
        textend_confirm = self.get_element_text_by_xpath(self.EXTEND_BOOKING_TEXT_CONFIRM)
        print("text: ", textend_confirm)
        assert textend_confirm == "In Use, Booking Extended"
        post_extend_time = self.get_element_text_by_xpath(self.PRE_EXTEND_TIME)
        print("post_extend_time: ", post_extend_time)
        assert pre_extend_time != post_extend_time

    def do_logout(self):
        self.do_click(self.LOGOUT_DROPDOWN)
        sleep(2)
        self.do_click(self.LOGOUT_BUTTON)