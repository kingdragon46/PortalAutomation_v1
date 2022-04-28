from time import sleep
import logging

from selenium.webdriver.common.keys import Keys


from Pages.LoginPage import LoginPage
from Pages.deskBookingsPage import deskBookingsPage
from Pages.RoomBookingPage import RoomBookingsPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest


'''Logger'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Test_RoomBooking(BaseTest):

    """Room Booking"""

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Selecting Host
        # bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        # bookinpage.host_selection(RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting Host
        # bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        # bookinpage.host_selection(RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_change_host_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting Host
        bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        bookinpage.host_selection(
            RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        try:
            enabled_check = bookinpage.is_enabled(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        bookinpage.do_click(
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
        print("Create a booking for the desk by selecting a default date and time: Passed")

        bookinpage.do_send_keys(RoomBookingsPage.BODY, Keys.PAGE_UP)
        sleep(3)

        # Clicking on Book Space for overlapping booking
        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        # Checking available resources
        bookinpage.select_available_status()
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        sleep(10)
        print("Create a booking of room by selecting the time of already cancelled booking: Passed")
        bookinpage.quit_driver()

    # @pytest.mark.skip(reason="no need of currently testing this")
    def test_only_host_can_cancel_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(
        #     TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        # bookinpage.host_selection(
        #     RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_3_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # # Selecting Host
        # bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        # bookinpage.host_selection(
        #     RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.DEFAULT_HOSTNAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Meeting is visible in attendee's my bookings")

        # trying to cancel the booking
        try:
            bookinpage.do_click(
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            print("Cancelling meeting succesfull")
        except Exception as e:
            print("exception in cancelling: ", e)

        sleep(10)
        bookinpage.quit_driver()


    '''Recurring Bookings Daily'''

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        """Booking Modal"""

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_change_host_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

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
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        try:
            enabled_check = bookinpage.is_enabled(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        bookinpage.do_click(
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
        print("Create a booking for the desk by selecting a default date and time: Passed")

        bookinpage.do_send_keys(RoomBookingsPage.BODY, Keys.PAGE_UP)
        sleep(3)

        # Clicking on Book Space for overlapping booking
        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        # Checking available resources
        bookinpage.select_available_status()
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        sleep(10)
        print("Create a booking of room by selecting the time of already cancelled booking: Passed")
        bookinpage.quit_driver()



    '''Recurring bookings Weekly'''

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_change_host_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

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
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        try:
            enabled_check = bookinpage.is_enabled(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        bookinpage.do_click(
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
        print("Create a booking for the desk by selecting a default date and time: Passed")

        bookinpage.do_send_keys(RoomBookingsPage.BODY, Keys.PAGE_UP)
        sleep(3)

        # Clicking on Book Space for overlapping booking
        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        # Checking available resources
        bookinpage.select_available_status()
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        sleep(10)
        print("Create a booking of room by selecting the time of already cancelled booking: Passed")
        bookinpage.quit_driver()



    '''Recurring + Single'''

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_single_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        try:
            enabled_check = bookinpage.is_enabled(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        try:
            enabled_check = bookinpage.is_enabled(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_future_cancelled_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        # print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        # sleep(3)

        # Resource details page
        # bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        # sleep(8)

        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        # bookinpage.resource_details_page_check()
        # sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        bookinpage.do_click(
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
        print("Create a booking for the desk by selecting a default date and time: Passed")
        sleep(5)

        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Create a daily recurring booking for a month  by selecting a date and time such a way that Its overlapping from a future cancelled single booking: PASSED")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_future_cancelled_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        # print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        # sleep(3)

        # Resource details page
        # bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        # sleep(8)

        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        # bookinpage.resource_details_page_check()
        # sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        bookinpage.do_click(
            RoomBookingsPage.DESK_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
        sleep(2)
        bookinpage.do_click(
            RoomBookingsPage.DESK_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        print("Create a booking for the desk by selecting a default date and time: Passed")
        sleep(8)

        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Create a daily recurring booking for a month  by selecting a date and time such a way that Its overlapping from a future cancelled single booking: PASSED")

        sleep(10)
        bookinpage.quit_driver()



    '''Recurring+single+Cancelled'''

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_single_future_daily_recurring_booking_5_cancelled(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        # print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        # sleep(3)

        # Resource details page
        # bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        # sleep(8)

        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        # bookinpage.resource_details_page_check()
        # sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.do_click((RoomBookingsPage.MY_BOOKING_NAV))

        bookinpage.cancel_some_bookings(5)
        # print("Create a booking for the desk by selecting a default date and time: Passed")
        sleep(8)

        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        # bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Create a daily recurring booking for a month  by selecting a date and time such a way that Its overlapping from a future cancelled single booking: PASSED")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_daily_future_daily_recurring_booking_5_cancelled(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        # print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        # sleep(3)

        # Resource details page
        # bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        # sleep(8)

        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        # bookinpage.resource_details_page_check()
        # sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.do_click((RoomBookingsPage.MY_BOOKING_NAV))

        bookinpage.cancel_some_bookings(5)
        # print("Create a booking for the desk by selecting a default date and time: Passed")
        sleep(8)

        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat2()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Create a daily recurring booking for a month  by selecting a date and time such a way that Its overlapping from a future cancelled single booking: PASSED")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_cancelling_first_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        # print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        # sleep(3)

        # Resource details page
        # bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        # sleep(8)

        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        # bookinpage.resource_details_page_check()
        # sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.do_click((RoomBookingsPage.MY_BOOKING_NAV))

        bookinpage.cancel_booking()
        print("Create a daily recurring booking for 10 days and cancel the starting day of booking : To make a verify that other future meetings are not getting cancelled: Passed")
        sleep(8)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_cancelling_last_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.enter_datetime()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        # print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        # sleep(3)

        # Resource details page
        # bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        # sleep(8)

        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        # bookinpage.resource_details_page_check()
        # sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.do_click((RoomBookingsPage.MY_BOOKING_NAV))

        bookinpage.cancel_last_booking()
        print("Create a daily recurring booking for 10 days and cancel the last day of booking : To make a verify that other future meetings are not getting cancelled: Passed")
        sleep(8)
        bookinpage.quit_driver()



    '''Extend booking'''

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        sleep(3)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        sleep(3)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_overlapping_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_2, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START_1, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_1, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
        # Error in extending Booking
        try:
            enabled_check = bookinpage.is_enabled(RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG_1)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG_1)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")
        # "Booking cannot be extended because"
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        sleep(3)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_cancelled_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_2, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START_1, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_1, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.scroll_to_element(RoomBookingsPage.ROOM_124_CHECK_RDIV)
        sleep(2)
        bookinpage.do_click(RoomBookingsPage.ROOM_124_CHECK_RDIV)
        sleep(3)
        bookinpage.do_click(RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON)
        sleep(8)

        # Extend booking
        bookinpage.scroll_to_element(RoomBookingsPage.ROOM_124_CHECK_DIV)
        bookinpage.extend_booking(RoomBookingsPage.EXTEND_30_MINS)
            
        sleep(5)

        print("Start meeting and then extend the booking for the next 30 minute make sure there is a cancelled recurring  existing booking  is available : Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_till_next_date_extended_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START_1, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END_1, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        sleep(3)
        bookinpage.quit_driver()

    
    '''Cancel Booking'''

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_cancel_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 2)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 2)
        sleep(3)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON, 2)
        sleep(8)
        print("Create a daily recurring booking for a month and delete any single instance: Passed")
        bookinpage.quit_driver()
   
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_cancel_all_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 0)
        sleep(3)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON, 0)
        sleep(8)
        print("Create a daily recurring booking for a month and delete all booking: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_weekly_recurring_cancel_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 2)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 2)
        sleep(3)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON, 2)
        sleep(8)
        print("Create a daily recurring booking for a month and delete any single instance: Passed")
        bookinpage.quit_driver()
  
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_weekly_recurring_cancel_all_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 0)
        sleep(3)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON, 0)
        sleep(8)
        print("Create a daily recurring booking for a month and delete all booking: Passed")
        bookinpage.quit_driver()
 
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_cancel_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_CHECK_DIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_CHECK_DIV, 0)
        sleep(3)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON, 0)
        sleep(8)
        print("Create a single booking and cancel it: Passed")
        bookinpage.quit_driver()
