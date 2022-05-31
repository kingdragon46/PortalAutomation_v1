import traceback
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
    ROOM_NUMBER = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[5]/div[3]")
    # ROOM_AVAIL = (By.XPATH, "//div[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button")
    ROOM_AVAIL = "(//div[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button)"
    ROOM_AVAIL_NAME = "(//div[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button)"

    # ---------------
    # BOOKING_NAV = (By.XPATH, "//h3[text()='Booking']")
    BOOKING_NAV = (
        By.XPATH, "//*[@id='navigation']/div/div/div/div[2]/child::*[3]")
    BOOK_SPACE_NAV = (By.XPATH, "//*[contains(text(), 'Book space')]")
    LOCATION_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[1]/div/div")
    GENPACT_IT_PARK = (
        By.XPATH, "//div[contains(text(), 'Genpact IT Park')]/parent::*/parent::*/parent::*/preceding-sibling::*[2]/span/child::*")
    BUSINESS_TOWER = (By.XPATH, "//div[contains(text(), 'Bussiness Tower')]")
    FREE_CLICK = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/p")
    FIRST_FLOOR = (By.ID, "0-floor")
    STATUS_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div")
    AVAILABLE_STATUS = (By.CSS_SELECTOR, "span[title='Available']")
    BOOKED_STATUS = (By.CSS_SELECTOR, "span[title='Booked']")
    ASSIGNED_STATUS = (By.CSS_SELECTOR, "span[title='Assigned']")
    INACTIVE_STATUS = (By.CSS_SELECTOR, "span[title='Inactive']")
    ALL_STATUS = (By.CSS_SELECTOR, "span[title='All']")
    LIST_VIEW_BUTTON = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]")

    RESOURCE_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div")
    RESOURCE_ROOM = (By.CSS_SELECTOR, "span[title='Rooms']")
    # Room
    ROOM_124 = "//*[@title='{}']/parent::*/parent::*/following-sibling::*[5]/button"

    # Modal selectors
    BOOKING_AGENDA = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input")
    ATTENDEE_DETAILS = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div/div/div[1]")
    CONFIRM_BOOKING = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[6]/button[2]")
    EDIT_DETAILS = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[7]/div[2]/p")
    EDIT_DETAILS_SEARCH_BOX = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[8]/div[1]/div")
    START_DATE = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[1]/div[2]/div/input")
    START_DATE_X = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[3]/div[2]/div/span/span")
    END_DATE = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[3]/div[2]/div/input")
    CONTACT_EMAIL = (
        By.XPATH, "//*[contains(text(), 'New Member')]/parent::*/child::*/following-sibling::*/input")
    CONTACT_RIGHT_TICK = (
        By.XPATH, "//*[contains(text(), 'New Member')]/parent::*/child::*[4]/div")
    BOOKING_CONFIRM_BUTTON = (
        By.XPATH, "//*[contains(text(), 'Confirm Booking')]")
    LAST_DATE_VALIDITY = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div[2]/div/div[2]/div/div/div/input")

    # BOOKING_MODAL_GO_BACK = (By.XPATH, "//span[contains(text(),'Go Back')]")
    BOOKING_MODAL_GO_BACK = (By.XPATH, "//div/button[1]")
    # BOOKING_MODAL_GO_BACK = (
    #     By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[1]/div/child::*")

    # After Booking
    ROOM_124_AFTER_BOOKING_TITLE = "//div[@title='{}']"
    ROOM_124_RPAGE_STATUS_CHECK = "//*[@title='{}']/parent::*/parent::td/following-sibling::*[1]/div/div"

    # Resource Details
    RD_CALENDER_INPUT = (
        By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/input")
    SCHEDULE_LISTING = (
        By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[3]/div/div/div[2]")
    I_BUTTON = (By.XPATH, "//*[@class='rbc-event-content']/span")
    I_INFO = (By.CLASS_NAME, "ant-popover-content")
    I_INFO2 = (By.XPATH, "/html/body/div[7]/div/div/div")
    RD_TIME_CHECK = (By.CLASS_NAME, "rbc-event-label")
    BOOK_THIS_SPACE = (
        By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[4]/div/button")
    BOOKING_HOSTNAME = (
        By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[1]")
    BOOKING_HOSTEMAIL = (
        By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[2]")
    BOOKING_START = (
        By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[3]")
    BOOKING_END = (
        By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[4]")

    # My Bookings
    MY_BOOKING_NAV = (By.XPATH, "//*[@id='sub-nav']/div[2]")
    ROOM_124_CHECK_DIV = "(//p[text()='{}']/parent::*/parent::div)"
    ROOM_124_CHECK_DIV_LAST = "(//p[text()='{}']/parent::*/parent::div)[last()]"
    ROOM_124_SCHEDULE_CHECK = "//p[text()='{}']/parent::*/following-sibling::*[1]"
    ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = "(//p[text()='{}']/parent::*/following-sibling::*[2])"
    ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2])"
    ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON_LAST = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2])[last()]"
    ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/button)"
    MAIN_CARDS_CONATINER = (By.ID, "mainBookingCardsContainer")
    ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = "//p[text()='{}']/parent::*/parent::*/preceding-sibling::*/child::*[2]/child::*/child::*/*[@class='MuiSvgIcon-root']"
    ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON = (
        By.XPATH, "//*[text()='Cancel All']")
    LAST_DATE_INPUT = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[1]/div/div[3]/input")
    FREE_CLICK_MB = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div[2]/div[1]/div/div[1]")
    MAIN_CARDS_CONTAINER = (By.XPATH, "//*[@id='mainBookingCardsContainer']")
    REFRESH_BOOKINGS = (By.XPATH, "//*[@class='ant-tooltip-open']")
    MY_SHORTCUTS_H3 = (By.XPATH, "//h3[text()='My Shortcut']")

    # Overlapping error
    GEN_ERROR_MSG = (By.XPATH, "//*[contains(text(), 'Booking Error:')]")
    BK_OVERLAPPING_ERROR_MSG = (
        By.XPATH, "//span[contains(text(), 'Booking Error: Booking Exists')]")
    BK_OVERLAPPING_ERROR_MSG_1 = (
        By.XPATH, "//*[contains(text(), 'Error in extending Booking')]")
    BK_OVERLAPPING_ERROR_MSG_2 = (
        By.XPATH, "//*[contains(text(), 'Error in extending Booking')]")

    # Recurring
    ROOM_124_CHECK_RDIV = "(//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')])"
    ROOM_124_RDIV_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]/parent::*/parent::*/parent::*/parent::*/following-sibling::*/div/div/button[2]"
    REPEAT_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div[1]/div/div/div/div[1]")
    REPEAT_DAILY = (By.XPATH, "//*[contains(text(), 'Daily')]")
    REPEAT_WEEKLY = (By.XPATH, "//*[contains(text(), 'Weekly')]")
    REPEAT_TILL_DATE = (
        By.XPATH, "//*[contains(text(), 'Ending (on Date)')]/following-sibling::*/child::*/child::*")
    REPEAT_FREQUENCY = (By.XPATH, "//*[contains(text(), 'Every')]/child::*")
    MULTIPLE_DAYS = (By.XPATH, "//*[contains(text(), 'Daily')]")
    MULTIPLE_DAYS_START_DATE = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/input")
    MULTIPLE_DAYS_END_DATE = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/input")

    # Extend Booking
    PRE_EXTEND_TIME = "//p[text()='{}']/parent::*/following-sibling::*[1]/div/div"
    CHECKIN_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[1]"
    EXTEND_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2]"
    EXTEND_15_MINS = (By.CSS_SELECTOR, "p[text()='15 minutes']")
    EXTEND_30_MINS = (By.CSS_SELECTOR, "p[text()='30 minutes']")
    EXTEND_45_MINS = (By.CSS_SELECTOR, "p[text()='45 minutes']")
    EXTEND_60_MINS = (By.CSS_SELECTOR, "p[text()='60 minutes']")
    EXTEND_BOOKING_TEXT_CONFIRM = "//p[text()='{}']/parent::*/parent::*/following-sibling::div[2]/div"

    # Logout
    LOGOUT_DROPDOWN = (
        By.XPATH, "//*[@id='navigation']/div/div/div/div[3]/div/div[2]/div/div[2]/div")
    LOGOUT_BUTTON = (By.XPATH, "//*[text()='Logout']")

    # Tags
    TAG_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[2]/div/div")
    TAG_SELECT = (
        By.XPATH, f"//*[@title='{TestData.TAG}']/preceding-sibling::*[1]")

    # Pagination Check
    ROOOMS_CLOSE = (
        By.XPATH, "//span[@title='Rooms']/child::*[2]/child::*/child::*")
    TOTAL_ITEMS = (By.XPATH, "//*[@class='ant-pagination-total-text'][last()]")
    PAGE_PREV = (
        By.XPATH, "//*[@class='ant-pagination-total-text']/following-sibling::*[1]")
    PAGES_NUMBERING = "//*[@class='ant-pagination-total-text']/following-sibling::*[{}]"
    FIRST_PAGE_LI = (
        By.XPATH, "//*[@class='ant-pagination-total-text']/following-sibling::*[2]")
    NEXT_PREV = (
        By.XPATH, "//*[@class='ant-pagination-total-text']/following-sibling::*[last()]/*/parent::*/preceding-sibling::*[1]")
    LAST_PAGE_LI = (
        By.XPATH, "//*[@class='ant-pagination-total-text']/following-sibling::*[last()]/*/parent::*/preceding-sibling::*[2]")

    NUM_OF_TR = (By.XPATH, "//tbody/tr")

    VRS_LOADER = (By.XPATH, "//*[@class='vrs-loader-logo']/child::*")


    # Book Space Date Selectors
    BS_DATE_DIV = (By.XPATH, "//input[@placeholder='Today']")
    BS_DMULTIPLE_DAYS = (By.XPATH, "//p[text()='Multiple Days']")
    BS_DENDDATE = (By.XPATH, "//input[@placeholder='End date']")
    BS_DONE = (By.XPATH, "//button/span[text()='Done']")
    TDATA_ENDDATE = (By.XPATH, f"//*[@title='{TestData.BS_CAL_ENDDATE}']")
    CAL_NEXT_MONTH = (By.CLASS_NAME, "ant-picker-next-icon")
    CAL_OK_BUTTON = (By.XPATH, "//button/span[text()='Ok']")

    # <===================================== Functions =======================================>

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for Bookings Page"""

    """selecting location"""

    def select_location(self):
        sleep(5)
        try:
            self.action_chain_click(self.LOCATION_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.GENPACT_IT_PARK)
            sleep(2)
            self.action_chain_click(self.BUSINESS_TOWER)
            sleep(2)
            self.do_click(self.FREE_CLICK)
            assert "Location selection passed"
        except Exception as e:
            print("Select_location_room exception: ", e)
        # sleep(5)

    def select_resource_type(self):
        try:
            self.do_click(self.RESOURCE_DROPDOWN)
            sleep(1)
            self.do_click(self.RESOURCE_ROOM)
            self.do_click(self.FREE_CLICK)
            sleep(1)
        except Exception as e:
            print("select_resource_type exception: ", e)

    def select_floor(self):
        try:
            self.do_click(self.FIRST_FLOOR)
            sleep(1)
            assert "Floor selection done"
        except Exception as e:
            print("select_floor exception: ", e)

    def select_available_status(self):
        try:
            self.action_chain_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.do_click(self.AVAILABLE_STATUS)
            sleep(2)
            assert "Select Available status done"
        except Exception as e:
            print(f"select_available_status exception: e \n{traceback.format_exc()}")
            self.take_screenshot(f"select_available_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_available_resource(self, a=None):
        # self.do_click(self.ROOM_AVAIL)
        for i in range(1, 6):
            title = self.get_element_text_by_xpath(
                self.ROOM_AVAIL_NAME+str([i]))
            if title not in TestData.ROOM_W_ISSUE:
                if a is None:
                    print("Booking: ", self.ROOM_AVAIL+str([i]))
                    self.do_click_by_xpath(self.ROOM_AVAIL+str([i]))
                else:
                    self.do_click_by_xpath(self.ROOM_AVAIL_NAME+str([a]))
                break
            else:
                pass

    def select_days_end(self):
        try:
            self.do_click(self.BS_DATE_DIV)
            self.action_chain_click(self.BS_DMULTIPLE_DAYS)
            self.action_chain_click(self.BS_DENDDATE)
            print(f"End date: {self.TDATA_ENDDATE}")
            for i in range(2):
                d_isvisible = self.is_visible(self.TDATA_ENDDATE)
                print(f"{i}. visibility: {d_isvisible}")
                if d_isvisible == True:
                    self.do_click(self.TDATA_ENDDATE)
                    break
                else:
                    self.do_click(self.CAL_NEXT_MONTH)
            self.action_chain_click(self.CAL_OK_BUTTON)
            sleep(1)
            self.action_chain_click(self.BS_DONE)
            sleep(4)
        except Exception as e:
            print(f"select_days_end exception: {e}")

    def select_tag(self):
        try:
            self.do_click(self.TAG_DROPDOWN)
            sleep(3)
            self.do_click(self.TAG_SELECT)
            sleep(3)
            self.do_click(self.FREE_CLICK)
            sleep(2)
        except Exception as e:
            print("select_tag exception: ", e)

    def confirm_booking(self):
        self.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        enabled_check = self.is_enabled(
            self.GEN_ERROR_MSG)
        print("enabled_check: ", enabled_check)
        if enabled_check == 1:
            error_msg = self.get_element_text(
                self.GEN_ERROR_MSG)
            print("error-msg: ", error_msg)
            sleep(6)
            enabled_check_1 = self.is_enabled(
                self.BOOKING_MODAL_GO_BACK)
            print("enabled_check1: ", enabled_check_1)
            self.do_click(self.BOOKING_MODAL_GO_BACK)
            sleep(2)
        else:
            pass

    def get_room_name(self):
        try:
            rval = self.get_element_text(self.ROOM_NUMBER)
            print("rval: ", rval)
            return rval
        except Exception as e:
            print("get_room_name exception: ", e)

    def select_booked_status(self):
        sleep(3)
        try:
            self.action_chain_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.do_click(self.BOOKED_STATUS)
            sleep(2)
            assert "Select Booked status done"
        except Exception as e:
            print(f"select_booked_status exception: e \n{traceback.format_exc()}")
            self.take_screenshot(f"select_booked_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_all_status(self):
        sleep(5)
        try:
            self.action_chain_click(self.STATUS_DROPDOWN)
            sleep(2)
            self.do_click(self.ALL_STATUS)
            sleep(2)
            assert "Select All status done"
        except Exception as e:
            print(f"select_all_status exception: e \n{traceback.format_exc()}")
            self.take_screenshot(f"select_all_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

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
            # self.do_click(self.START_DATE)
            # self.action_chain_click(self.START_DATE_X)
            self.date_selection_chain(
                self.START_DATE, TestData.ROOM_START_DATE, 18)
            # self.do_click(self.END_DATE)
            self.date_selection_chain(
                self.END_DATE, TestData.ROOM_END_DATE, 18)
        except Exception as e:
            print("enter_datetime exception: ", e)

    def enter_datetime_weekly(self):
        try:
            self.do_click(self.START_DATE)
            self.action_chain_click(self.START_DATE_X)
            self.date_selection_chain(
                self.START_DATE, TestData.ROOM_WSTART_DATE, 18)
            self.do_click(self.END_DATE)
            self.date_selection_chain(
                self.END_DATE, TestData.ROOM_WEND_DATE, 18)
        except Exception as e:
            print("enter_datetime exception: ", e)

    def resource_page_booking_check(self):
        try:
            rpage_status = self.get_element_text_by_xpath(
                self.ROOM_124_RPAGE_STATUS_CHECK)
            assert rpage_status == "Booked"
            print("rpage_status passed as: ", rpage_status)
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        except Exception as e:
            print("resource_page_booking_check exception: ", e)
            self.take_screenshot(f"resource_page_booking_check/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

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
            self.take_screenshot(f"resource_details_page_check/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        self.do_send_keys(self.BODY, Keys.PAGE_UP)

    def check_my_booking(self):
        try:
            self.do_click(self.MY_BOOKING_NAV)
            sleep(3)
            self.scroll_to_element_by_xpath(self.ROOM_124_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = self.get_element_text_by_xpath(
                self.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            self.do_click_by_xpath(self.ROOM_124_CHECK_DIV)
            sleep(3)
        except Exception as e:
            print("check_my_roombooking exception: ", e)

    def daily_repeat(self):
        try:
            self.do_click(self.REPEAT_DROPDOWN)
            sleep(3)
            self.do_click(self.REPEAT_DAILY)
            sleep(2)
            # self.date_selection_chain(self.REPEAT_FREQUENCY, TestData.REPEAT_FREQUENCY, 2)
            sleep(2)
            self.date_selection_chain(
                self.REPEAT_TILL_DATE, TestData.REPEAT_TILL_DATE[:11], 2)
        except Exception as e:
            print("daily_repeat exception: ", e)

    def daily_repeat2(self):
        try:
            self.do_click(self.REPEAT_DROPDOWN)
            sleep(3)
            self.do_click(self.REPEAT_DAILY)
            sleep(2)
            # self.date_selection_chain(self.REPEAT_FREQUENCY, TestData.REPEAT_FREQUENCY, 2)
            sleep(2)
            self.date_selection_chain(
                self.REPEAT_TILL_DATE, TestData.REPEAT_TILL_DATE3, 2)
        except Exception as e:
            print("daily_repeat2 exception: ", e)

    def weekly_repeat(self):
        try:
            self.do_click(self.REPEAT_DROPDOWN)
            sleep(3)
            self.do_click(self.REPEAT_WEEKLY)
            sleep(2)
            self.date_selection_chain(
                self.REPEAT_TILL_DATE, TestData.WEEKLY_REPEAT_TILL_DATE, 2)
            sleep(2)
            # self.date_selection_chain(self.REPEAT_FREQUENCY, TestData.REPEAT_FREQUENCY, 2)
        except Exception as e:
            print("weekly_repeat exception: ", e)

    def cancel_booking(self):
        try:
            self.scroll_to_element_by_xpath(self.ROOM_124_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = self.get_element_text_by_xpath(
                self.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            # assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            self.do_click_by_xpath(self.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(4)
            self.do_click(self.MY_SHORTCUTS_H3)
            self.action_chain_sendkeys_1(self.BODY, Keys.HOME)
            self.do_click(self.REFRESH_BOOKINGS)
        except Exception as e:
            print("cancel_booking exception: ", e)

    def cancel_last_booking(self):
        try:
            self.scroll_to_element_by_xpath(self.ROOM_124_CHECK_DIV_LAST)
            sleep(3)
            print("In My booking page, the created booking should be visible with two options i.e Cancel booking: Passed")
            self.do_click_by_xpath(
                self.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON_LAST)
            sleep(20)
        except Exception as e:
            print("cancel_last_booking exception: ", e)

    def change_date_format(self, string):
        string1 = f'{string[3:6]} {string[:2]} {string[7:11]}'
        return string1

    def cancel_some_bookings(self, crange):
        try:
            for i in range(1, crange):
                sleep(2)
                a = 1
                print(
                    f"i: {i} \n xpath: {self.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON+str([a])}")
                self.scroll_to_element_by_xpath(
                    f'{self.ROOM_124_CHECK_DIV+str([a])}')
                sleep(3)
                # Meeting Options
                meeting_options = self.get_element_text_by_xpath(
                    self.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK+str([a])).split('\n')
                std_meeting_options = ['Check in', '', 'Cancel Booking']
                # assert meeting_options == std_meeting_options
                print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
                if i == 1:
                    print("in i=1")
                    self.scroll_to_element_by_xpath(
                        self.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
                    self.do_click_by_xpath(
                        self.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
                else:
                    print("in i!=1")
                    self.scroll_to_element_to_mid_by_xpath(
                        f'{self.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON+str([a])}')
                    self.do_click_by_xpath(
                        f'{self.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON+str([a])}')
                sleep(4)
                ele = self.is_visible(self.VRS_LOADER)
                print("vrs loadr: ", ele)
                # while True:
                #     if ele == True:
                #         sleep(2)
                #     else:
                #         break
                self.do_click(self.MY_SHORTCUTS_H3)
                self.action_chain_sendkeys_1(self.BODY, Keys.HOME)
                self.do_click(self.REFRESH_BOOKINGS)
        except Exception as e:
            print("cancel_some_bookings exception: ", e)

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
            sleep(1)
            print("Selecting Location")
            self.select_location()
            print("Selecting Floor")
            self.select_floor()
            # Checking available resources
            self.select_available_status()
            # Selecting resource type
            self.select_resource_type()
            # Clicking on list view
            self.do_click(self.LIST_VIEW_BUTTON)
            sleep(3)
        except Exception as e:
            print(f"start_selection exception: e \n{traceback.format_exc()}")
            self.take_screenshot(f"start_selection/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    #
