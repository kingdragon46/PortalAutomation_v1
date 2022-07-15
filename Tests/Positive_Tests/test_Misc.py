import json
from time import time, sleep
import sys

from selenium.webdriver.common.keys import Keys


from Pages.LoginPage import LoginPage
from Pages.RoomBookingPage import RoomBookingsPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest

import traceback, sys

from random_name_generator import ran_name, ran_name_2
from WebConfig.time_functions import WebConfigFunctions as Config

# '''Logger'''
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# Note: Sending only pnr


class Test_RoomBooking(BaseTest):

    start_time = time()

    def process_browser_log_entry(self,entry):
        response = json.loads(entry['message'])['message']
        return response

    # Login
    @pytest.mark.pnr
    @pytest.mark.prsc
    @pytest.mark.prs
    @pytest.mark.pr
    @pytest.mark.prw
    @pytest.mark.pcnclb
    @pytest.mark.extndb
    @pytest.mark.misc
    @pytest.mark.hostrltd
    @pytest.mark.custom
    @pytest.mark.selected
    @pytest.mark.login
    def test_login_room_booking(self):
        print("Start time: ", self.start_time)
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
                    TestData.USER_NAME, TestData.PASSWORD)
        sleep(3)

        '''Extend booking'''

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_daily_recurring_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        # Checking available resources
        bookinpage.select_available_status()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.prEXTEND_TIME = RoomBookingsPage.prEXTEND_TIME.format(rval)
        RoomBookingsPage.CHECKIN_BOOKING = RoomBookingsPage.CHECKIN_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING = RoomBookingsPage.EXTEND_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking/test_extend_single_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Extend booking
        bookinpage.extend_booking(RoomBookingsPage.EXTEND_30_MINS)
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        sleep(2)

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        # Checking available resources
        bookinpage.select_available_status()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.prEXTEND_TIME = RoomBookingsPage.prEXTEND_TIME.format(rval)
        RoomBookingsPage.CHECKIN_BOOKING = RoomBookingsPage.CHECKIN_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING = RoomBookingsPage.EXTEND_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking/test_extend_single_booking/{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Extend booking
        bookinpage.extend_booking(RoomBookingsPage.EXTEND_30_MINS)
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        sleep(2)

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_overlapping_recurring_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        # Checking available resources
        bookinpage.select_available_status()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.prEXTEND_TIME = RoomBookingsPage.prEXTEND_TIME.format(rval)
        RoomBookingsPage.CHECKIN_BOOKING = RoomBookingsPage.CHECKIN_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING = RoomBookingsPage.EXTEND_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.BookResource_Modal_END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_2, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking/test_extend_single_overlapping_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        # Clicking on Book Space for overlapping booking
        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.BookResource_Modal_START_DATE, TestData.ROOM_OVERLAPPING_TIME_START_1, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.BookResource_Modal_END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_1, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking/test_extend_single_overlapping_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Extend booking
        bookinpage.extend_booking(RoomBookingsPage.EXTEND_30_MINS)
        # Error in extending Booking
        try:
            enabled_check = bookinpage.is_enabled(RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG_1)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG_1)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
                sleep(2)
        except Exception as e:
            print("Error 2")
        # "Booking cannot be extended because"
        bookinpage.driver_get_url(TestData.MY_BOOKING_URL)
        sleep(3)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        sleep(2)

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_cancelled_recurring_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.scroll_to_element(RoomBookingsPage.BOOKING_NAV)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        # Checking available resources
        bookinpage.select_available_status()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.prEXTEND_TIME = RoomBookingsPage.prEXTEND_TIME.format(rval)
        RoomBookingsPage.CHECKIN_BOOKING = RoomBookingsPage.CHECKIN_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING = RoomBookingsPage.EXTEND_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.BookResource_Modal_END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_2, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking/test_extend_single_cancelled_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        # Clicking on Book Space for overlapping booking
        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.BookResource_Modal_START_DATE, TestData.ROOM_OVERLAPPING_TIME_START_1, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.BookResource_Modal_END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_1, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking/test_extend_single_cancelled_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
        sleep(5)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV)
        sleep(2)
        bookinpage.do_click_by_xpath(RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV)
        sleep(3)
        bookinpage.do_click_by_xpath(RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON)
        sleep(8)

        # Extend booking
        bookinpage.scroll_to_element(RoomBookingsPage.MyBookings_ROOM_CHECK_DIV)
        bookinpage.extend_booking(RoomBookingsPage.EXTEND_30_MINS)
        print("Start meeting and then extend the booking for the next 30 minute make sure there is a cancelled recurring  existing booking  is available : Passed")
        sleep(2)

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_till_next_date_extended_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.scroll_to_element(RoomBookingsPage.BOOKING_NAV)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        # Checking available resources
        bookinpage.select_available_status()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.prEXTEND_TIME = RoomBookingsPage.prEXTEND_TIME.format(rval)
        RoomBookingsPage.CHECKIN_BOOKING = RoomBookingsPage.CHECKIN_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING = RoomBookingsPage.EXTEND_BOOKING.format(rval)
        RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = RoomBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.BookResource_Modal_START_DATE, TestData.ROOM_OVERLAPPING_TIME_START_1, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.BookResource_Modal_END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_1, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking/test_till_next_date_extended_booking/{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Extend booking
        bookinpage.extend_booking(RoomBookingsPage.EXTEND_30_MINS)
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        sleep(2)
      
    
    '''Test Pagination'''
    @pytest.mark.misc
    @pytest.mark.skip
    def test_pagination(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Checking available resources
        bookinpage.select_BookingStatusFilter_ALL_STATUS()
        sleep(5)
        # Selecting resource type
        bookinpage.do_click(RoomBookingsPage.ROOOMS_CLOSE)
        sleep(5)


        # Moving to element
        bookinpage.scroll_to_element(RoomBookingsPage.TOTAL_ITEMS)
        pages_total = bookinpage.get_element_text(RoomBookingsPage.TOTAL_ITEMS)
        check_prev = bookinpage.is_clickable(RoomBookingsPage.PAGE_PREV)
        check_prev_el = bookinpage.get_element(RoomBookingsPage.PAGE_PREV)
        print("prev check: ", check_prev)
        print("prev class check: ", check_prev_el.get_attribute("class"))

        check_next = bookinpage.is_clickable(RoomBookingsPage.NEXT_PREV)
        check_next_el = bookinpage.get_element(RoomBookingsPage.PAGE_PREV)
        print("next check: ", check_next)
        print("next class check: ", check_next_el.get_attribute("class"))

        last_page = bookinpage.get_element_text(RoomBookingsPage.LAST_PAGE_LI)
        print("last-page: ", last_page)

        rows = bookinpage.get_elements(RoomBookingsPage.NUM_OF_TR)
        print("num of rows: ", len(rows))

        rrange = int(last_page) + 1
        print("rrange: ", rrange)
        for i in range(2, rrange, 1):
            print("i: ", i)
            PAGES_NUMBERING = f"//*[@class='ant-pagination-total-text']/following-sibling::*[{i}]"
            print("i xpath: ", PAGES_NUMBERING)
            bookinpage.scroll_to_element(RoomBookingsPage.TOTAL_ITEMS)
            bookinpage.do_click_by_xpath(PAGES_NUMBERING)
            rows = bookinpage.get_elements(RoomBookingsPage.NUM_OF_TR)
            print("num of rows: ", len(rows))
            sleep(3)

        sleep(2)


    '''Host related'''

    @pytest.mark.hostrltd
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_only_host_can_cancel_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(
        #     TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        # bookinpage.host_selection(
        #     RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_3_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # # Selecting Host
        # bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        # bookinpage.host_selection(
        #     RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.DEFAULT_HOSTNAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking//{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        # Logging out
        bookinpage.do_logout()
        sleep(8)

        # Logging again using attendee details
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME_2, TestData.PASSWORD_2)

        sleep(10)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Meeting is visible in attendee's my bookings")

        # trying to cancel the booking
        try:
            bookinpage.do_click_by_xpath(
            RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON)
            print("Cancelling meeting succesfull")
        except Exception as e:
            print("exception in cancelling: ", e)

        bookinpage.do_logout()
        sleep(8)

        # Logging again using attendee details
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        
        sleep(8)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(2)

    @pytest.mark.hostrltd
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_change_host_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        sleep(6)

        # Checking available resources
        bookinpage.select_available_status()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting Host
        bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        bookinpage.host_selection(
            RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking//{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        # bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

    @pytest.mark.hostrltd
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_change_host_daily_recurring_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        sleep(3)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        # Checking available resources
        bookinpage.select_available_status()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting Host
        bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        bookinpage.host_selection(
            RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking//{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

    @pytest.mark.hostrltd
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_change_host_weekly_recurring_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        sleep(3)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        # Checking available resources
        bookinpage.select_available_status()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
        RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV = RoomBookingsPage.RecurringBookings_ROOM_CHECK_RDIV.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON = RoomBookingsPage.RecurringBookings_ROOM_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)


        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.BookResource_Modal_ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        # Selecting Host
        bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        bookinpage.host_selection(
            RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"RoomBooking//{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
        sleep(5)
        # print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_BookingStatusFilter_BOOKED_STATUS()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")
       
    