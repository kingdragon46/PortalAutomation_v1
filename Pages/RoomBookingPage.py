import sys
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
    MORE_APPS = (By.XPATH, "//*[contains(text(), 'More Apps')]")
    BOOKING_NAV = (
        By.XPATH, "//*[@class='navigation-AppName-1_BPN'][text()='Booking']")
    BOOK_SPACE_NAV = (By.XPATH, "//*[contains(text(), 'Book space')]")

    # Location
    # LOCATION_DROPDOWN = (
    #     By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[1]/div/div")
    LOCATION_DROPDOWN = (
        By.XPATH, "//p[text()= 'Locations']/following-sibling::*/div")
    GENPACT_IT_PARK = (
        By.XPATH, f"//div[contains(text(), '{TestData.LOC_1}')]/parent::*/parent::*/parent::*/preceding-sibling::*[2]/span/child::*")
    BUSINESS_TOWER = (By.XPATH, f"//div[contains(text(), '{TestData.LOC_2}')]")
    FREE_CLICK = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/p")
    FIRST_FLOOR = (By.ID, "0-floor")
    SECOND_FLOOR = (By.ID, "1-floor")
    FLOOR_ARROW = (By.XPATH, "//h5[text()='Bussiness Tower']/../child::*[2]")

    # Status
    # BookingStatusFilter_STATUS_DROPDOWN = (
    #     By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div")
    BookingStatusFilter_STATUS_DROPDOWN = (By.XPATH, "//*[text()='Status']/following-sibling::*/child::*")
    BookingStatusFilter_AVAILABLE_STATUS = (By.CSS_SELECTOR, "span[title='Available']")
    BookingStatusFilter_BOOKED_STATUS = (By.CSS_SELECTOR, "span[title='Booked']")
    BookingStatusFilter_ASSIGNED_STATUS = (By.CSS_SELECTOR, "span[title='Assigned']")
    BookingStatusFilter_INACTIVE_STATUS = (By.CSS_SELECTOR, "span[title='Inactive']")
    BookingStatusFilter_ALL_STATUS = (By.CSS_SELECTOR, "span[title='All']")
    LIST_VIEW_BUTTON = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]")

    RESOURCE_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div")
    RESOURCE_ROOM = (By.CSS_SELECTOR, "span[title='Rooms']")
    # Room
    ROOM = "//*[@title='{}']/parent::*/parent::*/following-sibling::*[5]/button"

    # Modal selectors
    BookResource_Modal_BOOKING_AGENDA = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input")
    BookResource_Modal_ATTENDEE_DETAILS = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div/div/div[1]")
    BookResource_Modal_CONFIRM_BOOKING = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[6]/button[2]")
    BookResource_Modal_EDIT_DETAILS = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[7]/div[2]/p")
    BookResource_Modal_EDIT_DETAILS_SEARCH_BOX = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[8]/div[1]/div")
    BookResource_Modal_START_DATE = (
        By.CSS_SELECTOR, "input[placeholder= 'Select Start Date']")
    BookResource_Modal_START_DATE_X = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[3]/div[2]/div/span/span")
    BookResource_Modal_END_DATE = (
        By.CSS_SELECTOR, "input[placeholder= 'Select End Date']")
    BookResource_Modal_CONTACT_EMAIL = (
        By.XPATH, "//*[contains(text(), 'New Member')]/parent::*/child::*/following-sibling::*/input")
    BookResource_Modal_CONTACT_RIGHT_TICK = (
        By.XPATH, "//*[contains(text(), 'New Member')]/parent::*/child::*[4]/div")
    BookResource_Modal_BOOKING_CONFIRM_BUTTON = (
        By.XPATH, "//*[contains(text(), 'Confirm Booking')]")
    BookResource_Modal_LAST_DATE_VALIDITY = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div[2]/div/div[2]/div/div/div/input")

    BOOKING_SUCCESSFULL = (By.XPATH, "//*[contains(text(),'Booking created successfully')]")
    BOOKING_MODAL_GO_BACK = (By.XPATH, "//div/button[1]")
    # BOOKING_MODAL_GO_BACK = (
    #     By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[1]/div/child::*")

    # After Booking
    ROOM_AFTER_BOOKING_TITLE = "//div[@title='{}']"
    ROOM_RPAGE_STATUS_CHECK = "//*[@title='{}']/parent::*/parent::td/following-sibling::*[1]/div/div"

    # Resource Details
    ResourceDetails_RD_CALENDER_INPUT = (
        By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/input")
    ResourceDetails_SCHEDULE_LISTING = (
        By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[3]/div/div/div[2]")
    ResourceDetails_I_BUTTON = (By.XPATH, "//*[@class='rbc-event-content']/span")
    ResourceDetails_I_INFO = (By.CLASS_NAME, "ant-popover-content")
    ResourceDetails_I_INFO2 = (By.XPATH, "/html/body/div[7]/div/div/div")
    ResourceDetails_RD_TIME_CHECK = (By.CLASS_NAME, "rbc-event-label")
    BOOK_THIS_SPACE = (
        By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[4]/div/button")
    ResourceDetails_BOOKING_HOSTNAME = (
        By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[1]")
    ResourceDetails_BOOKING_HOSTEMAIL = (
        By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[2]")
    ResourceDetails_BOOKING_START = (
        By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[3]")
    ResourceDetails_BOOKING_END = (
        By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[4]")

    # My Bookings
    MY_BOOKING_NAV = (By.XPATH, "//*[@id='sub-nav']/div[2]")
    MyBookings_ROOM_CHECK_DIV = "(//p[text()='{}']/parent::*/parent::div)"
    MyBookings_ROOM_CHECK_DIV_LAST = "(//p[text()='{}']/parent::*/parent::div)[last()]"
    MyBookings_ROOM_SCHEDULE_CHECK = "//p[text()='{}']/parent::*/following-sibling::*[1]"
    MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = "(//p[text()='{}']/parent::*/following-sibling::*[2])"
    MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2])"
    MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON_LAST = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2])[last()]"
    MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = "(//p[text()='{}']/parent::*/following-sibling::*[2]/div/button)"
    MyBookings_MAIN_CARDS_CONATINER = (By.ID, "mainBookingCardsContainer")
    MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = "(//p[text()='{}']/parent::*/parent::*/preceding-sibling::*/child::*[2]/child::*/child::*/*[@class='MuiSvgIcon-root'])"
    MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_BUTTON = (
        By.XPATH, "//*[text()='Cancel All']")
    MyBookings_LAST_DATE_INPUT = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[1]/div/div[3]/input")
    FREE_CLICK_MB = (
        By.XPATH, "//p[text()='Status']")
    MyBookings_MAIN_CARDS_CONATINER = (By.XPATH, "//*[@id='mainBookingCardsContainer']")
    MyBookings_REFRESH_BOOKINGS = (By.XPATH, "//*[@class='ant-tooltip-open']")
    MyBookings_FREE_CLICK_2 = (By.XPATH, "//*[@id='meeting-room']/div[2]")
    MyBookings_MY_SHORTCUTS_H3 = (By.XPATH, "//h3[text()='My Shortcut']")

    # Overlapping error
    GEN_ERROR_MSG = (By.XPATH, "//*[contains(text(), 'Booking Error:')]")
    BK_OVERLAPPING_ERROR_MSG = (
        By.XPATH, "//span[contains(text(), 'Booking Error: Booking Exists')]")
    BK_OVERLAPPING_ERROR_MSG_1 = (
        By.XPATH, "//*[contains(text(), 'Error in extending Booking')]")
    BK_OVERLAPPING_ERROR_MSG_2 = (
        By.XPATH, "//*[contains(text(), 'Error in extending Booking')]")

    # Recurring
    RecurringBookings_ROOM_CHECK_RDIV = "(//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')])"
    RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = "//p[text()='{}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]/parent::*/parent::*/parent::*/parent::*/following-sibling::*/div/div/button[2]"
    RecurringBookings_REPEAT_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div[1]/div/div/div/div[1]")
    RecurringBookings_REPEAT_DAILY = (By.XPATH, "//*[contains(text(), 'Daily')]")
    RecurringBookings_REPEAT_WEEKLY = (By.XPATH, "//*[contains(text(), 'Weekly')]")
    RecurringBookings_REPEAT_TILL_DATE = (
        By.XPATH, "//*[contains(text(), 'Ending (on Date)')]/following-sibling::*/child::*/child::*")
    RecurringBookings_REPEAT_FREQUENCY = (By.XPATH, "//*[contains(text(), 'Every')]/child::*")
    RecurringBookings_MULTIPLE_DAYS = (By.XPATH, "//*[contains(text(), 'Daily')]")
    RecurringBookings_MULTIPLE_DAYS_START_DATE = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/input")
    RecurringBookings_MULTIPLE_DAYS_END_DATE = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/input")

    # Extend Booking
    MyBookings_PRE_EXTEND_TIME = "//p[text()='{}']/parent::*/following-sibling::*[1]/div/div"
    MyBookings_CHECKIN_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[1]"
    MyBookings_EXTEND_BOOKING = "//p[text()='{}']/parent::*/following-sibling::*[2]/div/div/button[2]"
    MyBookings_EXTEND_15_MINS = (By.CSS_SELECTOR, "p[text()='15 minutes']")
    MyBookings_EXTEND_30_MINS = (By.CSS_SELECTOR, "p[text()='30 minutes']")
    MyBookings_EXTEND_45_MINS = (By.CSS_SELECTOR, "p[text()='45 minutes']")
    MyBookings_EXTEND_60_MINS = (By.CSS_SELECTOR, "p[text()='60 minutes']")
    MyBookings_EXTEND_BOOKING_TEXT_CONFIRM = "//p[text()='{}']/parent::*/parent::*/following-sibling::div[2]/div"

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
    BS_D_MULTIPLE_DAYS = (By.XPATH, "//p[text()='Multiple Days']")
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
            self.action_chain_click(self.FREE_CLICK)
            assert "Location selection passed"
        except Exception as e:
            print(f"Select_location_room {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/select_location/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        # sleep(5)

    def select_resource_type(self):
        sleep(2)
        try:
            self.action_chain_click(self.RESOURCE_DROPDOWN)
            sleep(1)
            self.action_chain_click(self.RESOURCE_ROOM)
            self.action_chain_click(self.FREE_CLICK)
            sleep(1)
        except Exception as e:
            print(f"select_resource_type {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/select_resource_type/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_floor(self, fl=None):
        try:
            if fl:
                fl_visibilty = self.is_visible(self.SECOND_FLOOR)
                if fl_visibilty == False:
                    self.action_chain_click(self.FLOOR_ARROW)
                self.action_chain_click(self.SECOND_FLOOR)
            else:
                fl_visibilty = self.is_visible(self.FIRST_FLOOR)
                if fl_visibilty == False:
                    self.action_chain_click(self.FLOOR_ARROW)
                self.action_chain_click(self.FIRST_FLOOR)
            
            sleep(1)
            assert "Floor selection done"
        except Exception as e:
            print(f"select_floor {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/select_floor/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_available_status(self):
        try:
            self.action_chain_click(self.BookingStatusFilter_STATUS_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.BookingStatusFilter_AVAILABLE_STATUS)
            sleep(2)
            assert "Select Available status done"
        except Exception as e:
            print(f"select_available_status exception: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/select_available_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)
    
    def select_available_resource(self, a=None):
        # self.action_chain_click(self.ROOM_AVAIL)
        try:
            if a is None:
                a = 2
            for i in range(a, 15):
                elemnt = self.get_element(
                    (By.XPATH, self.ROOM_AVAIL_NAME+str([i])))
                title = self.get_element_text_by_xpath(
                    self.ROOM_AVAIL_NAME+str([i]))
                title1 = elemnt.get_attribute("title")
                print("title1: ", title1)
                if title1 == TestData.ROOM_W_ISSUE:
                    pass
                elif title1 == TestData.ROOM_W_ISSUE_2:
                    pass
                else:
                    print("Booking: ", self.ROOM_AVAIL+str([i]))
                    self.do_click_by_xpath(self.ROOM_AVAIL+str([i]))
                    break
        except Exception as e:
            print(f"select_available_resource exception: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/select_available_resource/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_days_end(self):
        try:
            self.action_chain_click(self.BS_DATE_DIV)
            self.action_chain_click(self.BS_D_MULTIPLE_DAYS)
            self.action_chain_click(self.BS_DENDDATE)
            print(f"End date: {self.TDATA_ENDDATE}")
            for i in range(2):
                self.action_chain_click(self.CAL_NEXT_MONTH)
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
            self.take_screenshot(f"RoomBooking/select_days_end/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_tag(self):
        try:
            self.action_chain_click(self.TAG_DROPDOWN)
            sleep(3)
            self.action_chain_click(self.TAG_SELECT)
            sleep(3)
            self.action_chain_click(self.FREE_CLICK)
            sleep(2)
        except Exception as e:
            print(f"select_tag: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/select_tag/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def BookResource_Modal_CONFIRM_BOOKING(self):
        try:
            self.action_chain_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
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
                self.action_chain_click(self.BOOKING_MODAL_GO_BACK)
                sleep(2)
            else:
                pass
        except Exception as e:
            print(f"BookResource_Modal_CONFIRM_BOOKING exception: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/BookResource_Modal_CONFIRM_BOOKING/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def booking_successfull(self):
        check = self.is_visible(self.BOOKING_SUCCESSFULL)
        if check == True:
            print("Booking should be created successfully: Passed")
        else:
            print("Booking Failed")


    def get_room_name(self):
        try:
            rval = self.get_element_text(self.ROOM_NUMBER)
            print("rval: ", rval)
            return rval
        except Exception as e:
            print(f"get_room_name: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/get_room_name/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def select_BookingStatusFilter_BOOKED_STATUS(self):
        sleep(3)
        try:
            self.action_chain_click(self.BookingStatusFilter_STATUS_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.BookingStatusFilter_BOOKED_STATUS)
            sleep(2)
            print("Select Booked status done")
        except Exception as e:
            print(f"select_BookingStatusFilter_BOOKED_STATUS exception: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/select_BookingStatusFilter_BOOKED_STATUS/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def select_BookingStatusFilter_ALL_STATUS(self):
        sleep(5)
        try:
            self.action_chain_click(self.BookingStatusFilter_STATUS_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.BookingStatusFilter_ALL_STATUS)
            sleep(2)
            print("Select All status done")
        except Exception as e:
            print(f"select_BookingStatusFilter_ALL_STATUS exception: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/select_BookingStatusFilter_ALL_STATUS/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def enter_agenda(self):
        try:
            self.host_selection(self.BookResource_Modal_BOOKING_AGENDA, TestData.ROOM_AGENDA)
        except Exception as e:
            print(f"enter_agenda: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/enter_agenda/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def new_contact_guest(self, contact_name, BookResource_Modal_CONTACT_EMAIL):
        try:
            self.host_selection(self.BookResource_Modal_ATTENDEE_DETAILS, contact_name)
            # element = self.get_element(self.BookResource_Modal_CONTACT_EMAIL)
            self.do_send_keys(self.BookResource_Modal_CONTACT_EMAIL, BookResource_Modal_CONTACT_EMAIL)
            self.action_chain_click(self.BookResource_Modal_CONTACT_RIGHT_TICK)
            sleep(2)
        except Exception as e:
            print(f"new_contact_guest: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/new_contact_guest/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def enter_datetime(self):
        try:
            # self.action_chain_click(self.BookResource_Modal_START_DATE)
            # self.action_chain_click(self.BookResource_Modal_START_DATE_X)
            self.date_selection_chain(
                self.BookResource_Modal_START_DATE, TestData.ROOM_BookResource_Modal_START_DATE, 18)
            # self.action_chain_click(self.BookResource_Modal_END_DATE)
            self.date_selection_chain(
                self.BookResource_Modal_END_DATE, TestData.ROOM_BookResource_Modal_END_DATE, 18)
        except Exception as e:
            print(f"enter_datetime: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/enter_datetime/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def enter_datetime_weekly(self):
        try:
            self.action_chain_click(self.BookResource_Modal_START_DATE)
            self.action_chain_click(self.BookResource_Modal_START_DATE_X)
            self.date_selection_chain(
                self.BookResource_Modal_START_DATE, TestData.ROOM_WBookResource_Modal_START_DATE, 18)
            self.action_chain_click(self.BookResource_Modal_END_DATE)
            self.date_selection_chain(
                self.BookResource_Modal_END_DATE, TestData.ROOM_WBookResource_Modal_END_DATE, 18)
        except Exception as e:
            print(f"enter_datetime: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/enter_datetime_weekly/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    def resource_page_booking_check(self):
        try:
            rpage_status = self.get_element_text_by_xpath(
                self.ROOM_RPAGE_STATUS_CHECK)
            assert rpage_status == "Booked"
            print("rpage_status passed as: ", rpage_status)
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        except Exception as e:
            print(f"resource_page_booking_check: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/resource_page_booking_check/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def resource_details_page_check(self):
        self.scroll_to_element(self.ResourceDetails_SCHEDULE_LISTING)
        sleep(2)
        try:
            self.action_chain_click(self.ResourceDetails_I_BUTTON)
            sleep(3)
            eltext = self.get_element_text(self.ResourceDetails_I_INFO).split('\n')
            print("eltext: ", eltext)
            sleep(3)
            print("At the resource details page, booking should be available: Passed")
        except Exception as e:
            print(f"resource_details_page_check:{e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/resource_details_page_check/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)
        self.do_send_keys(self.BODY, Keys.PAGE_UP)

    def check_my_booking(self):
        try:
            self.action_chain_click(self.MY_BOOKING_NAV)
            sleep(3)
            self.scroll_to_element_by_xpath(self.MyBookings_ROOM_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = self.get_element_text_by_xpath(
                self.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            # assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            # self.do_click_by_xpath(self.MyBookings_ROOM_CHECK_DIV)
            sleep(3)
        except Exception as e:
            print(f"check_my_roombooking: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/check_my_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def daily_repeat(self):
        try:
            self.action_chain_click(self.RecurringBookings_REPEAT_DROPDOWN)
            sleep(3)
            self.action_chain_click(self.RecurringBookings_REPEAT_DAILY)
            sleep(2)
            # self.date_selection_chain(self.RecurringBookings_REPEAT_FREQUENCY, TestData.RecurringBookings_REPEAT_FREQUENCY, 2)
            sleep(2)
            self.date_selection_chain(
                self.RecurringBookings_REPEAT_TILL_DATE, TestData.REPEAT_TILL_DATE[:11], 2)
        except Exception as e:
            print(f"daily_repeat: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/daily_repeat/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def daily_repeat2(self):
        try:
            self.action_chain_click(self.RecurringBookings_RecurringBookings_REPEAT_DROPDOWN)
            sleep(3)
            self.action_chain_click(self.RecurringBookings_REPEAT_DAILY)
            sleep(2)
            # self.date_selection_chain(self.RecurringBookings_REPEAT_FREQUENCY, TestData.RecurringBookings_REPEAT_FREQUENCY, 2)
            sleep(2)
            self.date_selection_chain(
                self.RecurringBookings_REPEAT_TILL_DATE, TestData.REPEAT_TILL_DATE3, 2)
        except Exception as e:
            print(f"daily_repeat2: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/daily_repeat2/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def weekly_repeat(self):
        try:
            self.action_chain_click(self.RecurringBookings_RecurringBookings_REPEAT_DROPDOWN)
            sleep(3)
            self.action_chain_click(self.RecurringBookings_REPEAT_WEEKLY)
            sleep(2)
            self.date_selection_chain(
                self.RecurringBookings_REPEAT_TILL_DATE, TestData.weekly_repeat_TILL_DATE, 2)
            sleep(2)
            # self.date_selection_chain(self.RecurringBookings_REPEAT_FREQUENCY, TestData.RecurringBookings_REPEAT_FREQUENCY, 2)
        except Exception as e:
            print(f"weekly_repeat: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/weekly_repeat/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def cancel_booking(self):
        try:
            self.scroll_to_element_by_xpath(self.MyBookings_ROOM_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = self.get_element_text_by_xpath(
                self.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            # assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            self.do_click_by_xpath(self.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(4)
            url = self.current_url()
            if 'ndl' in url:
                print("url: ", url)
                self.action_chain_click(self.MyBookings_MY_SHORTCUTS_H3)
            else:
                self.action_chain_click(self.MyBookings_FREE_CLICK_2)
            self.action_chain_sendkeys_1(self.BODY, Keys.HOME)
            self.action_chain_click(self.MyBookings_REFRESH_BOOKINGS)
        except Exception as e:
            print(f"cancel_booking: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/cancel_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def cancel_last_booking(self):
        try:
            self.scroll_to_element_by_xpath(self.MyBookings_ROOM_CHECK_DIV_LAST)
            sleep(3)
            print("In My booking page, the created booking should be visible with two options i.e Cancel booking: Passed")
            self.do_click_by_xpath(
                self.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON_LAST)
            sleep(20)
        except Exception as e:
            print(f"cancel_last_booking: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/cancel_last_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def change_date_format(self, string):
        string1 = f'{string[3:6]} {string[:2]} {string[7:11]}'
        return string1

    def cancel_some_bookings(self, crange):
        try:
            for i in range(1, crange):
                sleep(2)
                a = 1
                print(
                    f"i: {i} \n xpath: {self.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON+str([a])}")
                self.scroll_to_element_by_xpath(
                    f'{self.MyBookings_ROOM_CHECK_DIV+str([a])}')
                sleep(3)
                # Meeting Options
                meeting_options = self.get_element_text_by_xpath(
                    self.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK+str([a])).split('\n')
                std_meeting_options = ['Check in', '', 'Cancel Booking']
                # assert meeting_options == std_meeting_options
                print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
                if i == 1:
                    print("in i=1")
                    self.scroll_to_element_by_xpath(
                        self.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON)
                    self.do_click_by_xpath(
                        self.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON)
                else:
                    print("in i!=1")
                    self.scroll_to_element_to_mid_by_xpath(
                        f'{self.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON+str([a])}')
                    self.do_click_by_xpath(
                        f'{self.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON+str([a])}')
                sleep(4)
                ele = self.is_visible(self.VRS_LOADER)
                print("vrs loadr: ", ele)
                url = self.current_url()
                if 'ndl' in url:
                    print("url: ", url)
                    self.action_chain_click(self.MyBookings_MY_SHORTCUTS_H3)
                else:
                    self.action_chain_click(self.MyBookings_FREE_CLICK_2)
                self.action_chain_sendkeys_1(self.BODY, Keys.HOME)
                self.action_chain_click(self.MyBookings_REFRESH_BOOKINGS)
        except Exception as e:
            print(f"cancel_some_bookings: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/cancel_some_bookings/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def MyBookings_EXTEND_booking(self, etime):
        try:
            MyBookings_PRE_MyBookings_EXTEND_TIME = self.get_element_text_by_xpath(
                self.MyBookings_PRE_EXTEND_TIME)
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
            assert tMyBookings_EXTEND_confirm == "In Use, Booking Extended"
            post_MyBookings_EXTEND_time = self.get_element_text_by_xpath(
                self.MyBookings_PRE_EXTEND_TIME)
            print("post_MyBookings_EXTEND_time: ", post_MyBookings_EXTEND_time)
            assert MyBookings_PRE_MyBookings_EXTEND_TIME != post_MyBookings_EXTEND_time
        except Exception as e:
            print(f"MyBookings_EXTEND_booking: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/MyBookings_EXTEND_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def do_logout(self):
        try:
            self.action_chain_click(self.LOGOUT_DROPDOWN)
            sleep(2)
            self.action_chain_click(self.LOGOUT_BUTTON)
        except Exception as e:
            print(f"do_logout: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/do_logout/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    def start_selection(self, fl=None):
        fl = None
        try:
            sleep(1)
            print("Selecting Location")
            self.select_location()
            print("Selecting Floor")
            if fl:
                self.select_floor(fl)
            else:
                self.select_floor()
            # Checking available resources
            self.select_available_status()
            # Selecting resource type
            self.select_resource_type()
            # Clicking on list view
            self.action_chain_click(self.LIST_VIEW_BUTTON)
            sleep(3)
        except Exception as e:
            print(f"start_selection exception: {e} \n{traceback.format_exc()}")
            self.take_screenshot(f"RoomBooking/start_selection/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # sys.exit(3)

    #
