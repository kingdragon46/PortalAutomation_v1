from time import sleep
from time import time
import logging
import sys
import os

from selenium.webdriver.common.keys import Keys


from Pages.LoginPage import LoginPage
from Pages.deskBookingsPage import deskBookingsPage
from Pages.RoomBookingPage import RoomBookingsPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest
from datetime import datetime

from mail_conf import send_email

import traceback

# '''Logger'''
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# Note: Sending only pnr


class Test_RoomBooking(BaseTest):

    start_time = time()

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
    def test_login_room_booking(self):
        print("Start time: ", self.start_time)
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
                    TestData.USER_NAME, TestData.PASSWORD)
        

    """Room Booking"""

    @pytest.mark.pnr
    # @pytest.mark.custom
    def test_simple_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()
            # Clicking on available room

            bookinpage.take_screenshot(f"test_simple_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            bookinpage.select_available_resource()
            bookinpage.take_screenshot(f"test_simple_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)

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

            # loader invisibilty check
            loader = bookinpage.is_visible(RoomBookingsPage.VRS_LOADER)
            print("loader: ", loader)

            # Clicking on booking button
            # bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            bookinpage.take_screenshot(f"test_simple_booking/{TestData.CDATE[:10]}/pre_{TestData.CDATE[1:]}.png")
            sleep(5)
            bookinpage.take_screenshot(f"test_simple_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("Booking should be created successfully: Passed")
            print("Room_no_confirm: ", RoomBookingsPage.ROOM_124)
            # loader visibilty check
            # loader1 = bookinpage.is_visible(RoomBookingsPage.VRS_LOADER)
            # print("loader1: ", loader1)
            sleep(2)

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            bookinpage.take_screenshot(f"test_simple_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()
            sleep(3)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            bookinpage.check_my_booking()
            print("Create a booking for the desk by selecting a default date and time: Passed")
            # Cancelling Booking
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(1)
            loader2 = bookinpage.is_visible(RoomBookingsPage.VRS_LOADER)
            print("loader2: ", loader2)
            sleep(2)
        except Exception as e:
            print(f"Exception test_simple_booking: {e}")
            bookinpage.take_screenshot(f"test_simple_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.pnr
    # @pytest.mark.custom
    def test_datetime_change_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)

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

            # Selecting datetime0]}
            bookinpage.enter_datetime()

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            bookinpage.take_screenshot(f"test_datetime_change_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(5)
            
            bookinpage.take_screenshot(f"test_datetime_change_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("Booking should be created successfully: Passed")

            bookinpage.select_all_status()

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            sleep(3)

            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            sleep(3)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            bookinpage.check_my_booking()
            print("Create a booking for the desk by selecting a default date and time: Passed")
            # Cancelling Booking
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(2)
        except Exception as e:
            bookinpage.take_screenshot(f"test_datetime_change_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print(f"Exception test_datetime_change_booking: {e}\n{traceback.format_exc()}")

    @pytest.mark.pnr
    def test_overlapping_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            # Agenda
            bookinpage.enter_agenda()

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            bookinpage.take_screenshot(f"test_overlapping_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)

            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.resource_details_page_check()

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            bookinpage.check_my_booking()
            print("Create a booking for the desk by selecting a default date and time: Passed")

            # Clicking on Book Space for overlapping booking
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            sleep(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            bookinpage.take_screenshot(f"test_overlapping_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(1)

            enabled_check = bookinpage.is_visible(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == True:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
            
            bookinpage.driver_get_url(TestData.MY_BOOKING_URL)
            sleep(3)

            # Cancelling Booking
            # bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_CHECK_DIV)

            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(2)
        except Exception as e:
            bookinpage.take_screenshot(f"test_overlapping_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print(f"Exception test_overlapping_booking: {e}\n{traceback.format_exc()}")

    @pytest.mark.pnr
    def test_already_cancelled_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            bookinpage.take_screenshot(f"test_already_cancelled_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(5)
            
            bookinpage.take_screenshot(f"test_already_cancelled_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(3)
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()
            sleep(3)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            bookinpage.resource_details_page_check()

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            bookinpage.check_my_booking()
            bookinpage.do_click_by_xpath(
                RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            print("Create a booking for the desk by selecting a default date and time: Passed")
            sleep(5)
            bookinpage.scroll_to_element(RoomBookingsPage.BOOK_SPACE_NAV)

            # Clicking on Book Space for overlapping booking
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            sleep(3)

            # Checking available resources
            bookinpage.select_available_status()

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_already_cancelled_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(3)

            # Cancelling Booking
            bookinpage.action_chain_click(RoomBookingsPage.MY_BOOKING_NAV)
            sleep(2)
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_CHECK_DIV)
            sleep(2)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            print("Create a booking of room by selecting the time of already cancelled booking: Passed")
            sleep(2)
        except Exception as e:
            bookinpage.take_screenshot(f"test_already_cancelled_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print(f"Exception test_simple_booking: {e}\n{traceback.format_exc()}")


    '''Recurring Bookings Daily'''

    @pytest.mark.pr
    def test_simple_daily_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_simple_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(3)
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            sleep(2)
            bookinpage.resource_details_page_check()

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            sleep(2)
            bookinpage.check_my_booking()
            # Cancelling Booking
            bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
            sleep(2)
            bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
            print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")
        except Exception as e:
            print(f"Exception test_simple_daily_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_simple_daily_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.pr
    def test_datetime_change_daily_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_datetime_change_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(3)
            print("Booking should be created successfully: Passed")

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            bookinpage.check_my_booking()
            # Cancelling Booking
            bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 0)
            sleep(2)
            bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 0)
            sleep(3)
            bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")
        except Exception as e:
            print(f"Exception test_datetime_change_daily_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_datetime_change_daily_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.pr
    def test_overlapping_daily_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

            '''Booking Modal'''

            # Attendee Details
            # New Member
            bookinpage.new_contact_guest(
                TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
            # Is drafted = False
            bookinpage.host_selection(
                RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
            # Is Member = True
            bookinpage.host_selection(
                RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
            # Agenda
            bookinpage.enter_agenda()

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(3)
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()
            # bookinpage.driver_implicitly_wait(3)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            print("Create a booking for the desk by selecting a default date and time: Passed")

            # Clicking on Book Space for overlapping booking
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            # bookinpage.driver_implicitly_wait(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)

            enabled_check = bookinpage.is_visible(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", bool(enabled_check))
            if enabled_check == True:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
            
            # bookinpage.driver_implicitly_wait(3)
            bookinpage.driver_get_url(TestData.MY_BOOKING_URL)
            sleep(2)
            # Cancelling Booking
            # bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(3)
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            # bookinpage.driver_implicitly_wait(2)
            # Cancelling Booking
            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_overlapping_daily_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_overlapping_daily_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.pr
    def test_already_cancelled_daily_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_already_cancelled_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(3)
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()
            # bookinpage.driver_implicitly_wait(3)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            sleep(8)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            bookinpage.do_click_by_xpath(
                RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            print("Create a booking for the desk by selecting a default date and time: Passed")
            sleep(10)

            bookinpage.scroll_to_element(RoomBookingsPage.BOOK_SPACE_NAV)

            # Clicking on Book Space for overlapping booking
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            # Checking available resources
            bookinpage.select_available_status()
            # bookinpage.driver_implicitly_wait(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_already_cancelled_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("Create a booking of room by selecting the time of already cancelled booking: Passed")

            sleep(2)
            bookinpage.check_my_booking()
            # Cancelling Booking
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(1)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_already_cancelled_daily_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_already_cancelled_daily_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
 

    '''Recurring bookings Weekly'''
    @pytest.mark.prw
    def test_simple_weekly_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_simple_weekly_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()
            # bookinpage.driver_implicitly_wait(5)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            sleep(3)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

            # Cancelling Booking
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_simple_weekly_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_simple_weekly_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.prw
    def test_datetime_change_weekly_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.enter_datetime_weekly()

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_datetime_change_weekly_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            # Checking available resources
            bookinpage.select_all_status()
            # bookinpage.driver_implicitly_wait(5)

            # Resource details page
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(2)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(4)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_WSTART_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            print("Create a daily recurring booking for the desk by selecting a default date and time: Passed") 

            # Cancelling Booking
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_datetime_change_weekly_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_datetime_change_weekly_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.prw
    def test_overlapping_weekly_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_weekly_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()
            # bookinpage.driver_implicitly_wait(3)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            print("Create a booking for the desk by selecting a default date and time: Passed")

            # Clicking on Book Space for overlapping booking
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            # bookinpage.driver_implicitly_wait(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            # bookinpage.driver_implicitly_wait(2)
            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_weekly_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

            enabled_check = bookinpage.is_enabled(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')

            # bookinpage.driver_implicitly_wait(2)
            bookinpage.driver_get_url(TestData.MY_BOOKING_URL)
            sleep(2)

            # Cancelling Booking
            bookinpage.action_chain_click(RoomBookingsPage.MY_BOOKING_NAV)
            sleep(3)
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            # bookinpage.driver_implicitly_wait(3)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            print("Create a booking of room by selecting the time of already cancelled booking: Passed")
            sleep(2)
        except Exception as e:
            print(f"Exception test_overlapping_weekly_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_overlapping_weekly_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.prw
    def test_already_cancelled_weekly_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_already_cancelled_weekly_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            bookinpage.select_booked_status()
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()
            # bookinpage.driver_implicitly_wait(3)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            bookinpage.do_click_by_xpath(
                RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            print("Create a booking for the desk by selecting a default date and time: Passed")
            sleep(5)


            # Clicking on Book Space for overlapping booking
            bookinpage.scroll_to_element(RoomBookingsPage.BOOK_SPACE_NAV)
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            # Checking available resources
            bookinpage.select_available_status()
            # bookinpage.driver_implicitly_wait(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_already_cancelled_weekly_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("Create a booking of room by selecting the time of already cancelled booking: Passed")
            sleep(2)

            bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(4)
            # Cancelling Booking
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_already_cancelled_weekly_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_already_cancelled_weekly_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")


    '''Recurring + Single'''

    @pytest.mark.prs
    def test_overlapping_single_daily_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            # sleep(2)
            
            bookinpage.take_screenshot(f"test_overlapping_single_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            bookinpage.select_all_status()
            # bookinpage.driver_implicitly_wait(2)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            print("Create a booking for the desk by selecting a default date and time: Passed")

            # Clicking on Book Space for overlapping booking
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            # bookinpage.driver_implicitly_wait(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_single_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

            enabled_check = bookinpage.is_enabled(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')

            bookinpage.driver_get_url(TestData.MY_BOOKING_URL)
            sleep(3)
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(2)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_overlapping_single_daily_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_overlapping_single_daily_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
  
    @pytest.mark.prs
    def test_overlapping_daily_recurring_single_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            # bookinpage.enter_datetime()

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_daily_recurring_single_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            bookinpage.select_all_status()
            # bookinpage.driver_implicitly_wait(3)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)
            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            print("Create a booking for the desk by selecting a default date and time: Passed")

            # Clicking on Book Space for overlapping booking
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            # bookinpage.driver_implicitly_wait(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_daily_recurring_single_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

            enabled_check = bookinpage.is_enabled(
                RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')

            bookinpage.driver_get_url(TestData.MY_BOOKING_URL)
            sleep(3)
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_overlapping_daily_recurring_single_booking: {e}")
            bookinpage.take_screenshot(f"test_overlapping_daily_recurring_single_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        
    @pytest.mark.prs
    def test_overlapping_future_cancelled_daily_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_future_cancelled_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")


            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)

            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.check_my_booking()
            bookinpage.do_click_by_xpath(
                RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            print("Create a booking for the desk by selecting a default date and time: Passed")
            sleep(20)

            bookinpage.scroll_to_element(RoomBookingsPage.BOOK_SPACE_NAV)
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            sleep(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_future_cancelled_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("Create a daily recurring booking for a month  by selecting a date and time such a way that Its overlapping from a future cancelled single booking: PASSED")
            sleep(2)

            bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(3)
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_overlapping_future_cancelled_daily_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_overlapping_future_cancelled_daily_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")



    '''Recurring+single+Cancelled'''

    @pytest.mark.prsc
    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_overlapping_single_future_daily_recurring_booking_5_cancelled(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            bookinpage.select_days_end()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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

            last_date = bookinpage.get_element(RoomBookingsPage.LAST_DATE_VALIDITY).get_attribute("title")
            last_date2 = bookinpage.change_date_format(last_date)
            print(f'Last date: {last_date2}')

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_single_future_daily_recurring_booking_5_cancelled/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            bookinpage.select_all_status()
            # bookinpage.driver_implicitly_wait(3)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)

            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)

            bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
            bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)
            # bookinpage.driver_implicitly_wait(2)

            bookinpage.cancel_some_bookings(6)
            # print("Create a booking for the desk by selecting a default date and time: Passed")

            sleep(3)
            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            # bookinpage.driver_implicitly_wait(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.enter_datetime()

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_single_future_daily_recurring_booking_5_cancelled/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("Create a daily recurring booking for a month  by selecting a date and time such a way that Its overlapping from a future cancelled single booking: PASSED")
            sleep(5)

            bookinpage.driver_get_url(TestData.MY_BOOKING_URL)
            sleep(2)
            # bookinpage.driver_implicitly_wait(3)
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            # bookinpage.driver_implicitly_wait(2)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(20)
            bookinpage.scroll_to_element_to_mid_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(3)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_overlapping_single_future_daily_recurring_booking_5_cancelled: {e}")
            bookinpage.take_screenshot(f"test_overlapping_single_future_daily_recurring_booking_5_cancelled/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        
    @pytest.mark.prsc
    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_overlapping_daily_future_daily_recurring_booking_5_cancelled(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            bookinpage.select_days_end()

            # Clicking on available room
            bookinpage.select_available_resource()

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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

            last_date = bookinpage.get_element(RoomBookingsPage.LAST_DATE_VALIDITY).get_attribute("title")
            last_date2 = bookinpage.change_date_format(last_date)
            print(f'Last date: {last_date2}')

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_daily_future_daily_recurring_booking_5_cancelled/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            bookinpage.select_all_status()

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)

            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)

            bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
            bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)
            # bookinpage.driver_implicitly_wait(2)

            bookinpage.cancel_some_bookings(6)
            # print("Create a booking for the desk by selecting a default date and time: Passed")
            # bookinpage.driver_implicitly_wait(8)

            bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
            # bookinpage.driver_implicitly_wait(3)

            # Clicking on room 124 booking modal
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_overlapping_daily_future_daily_recurring_booking_5_cancelled/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            print("Create a daily recurring booking for a month  by selecting a date and time such a way that Its overlapping from a future cancelled single booking: PASSED")
            sleep(2)

            bookinpage.driver_get_url(TestData.MY_BOOKING_URL)
            # bookinpage.driver_implicitly_wait(3)
            bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
            bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)
            # bookinpage.driver_implicitly_wait(2)
            for i in range(2):
                print("i: ", i)
                bookinpage.action_chain_sendkeys_1(
                RoomBookingsPage.MAIN_CARDS_CONTAINER, Keys.HOME)
                vcheck = bookinpage.is_visible(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
                if vcheck == True:
                    bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
                    sleep(2)
                    bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
                    sleep(2)
                    bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
                    sleep(4)
                else:
                    break
                bookinpage.do_click(RoomBookingsPage.MY_SHORTCUTS_H3)
                bookinpage.action_chain_sendkeys_1(RoomBookingsPage.BODY, Keys.HOME)
                bookinpage.do_click(RoomBookingsPage.REFRESH_BOOKINGS)
        except Exception as e:
            print(f"Exception test_overlapping_daily_future_daily_recurring_booking_5_cancelled: {e}")
            bookinpage.take_screenshot(f"test_overlapping_daily_future_daily_recurring_booking_5_cancelled/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.prsc
    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_cancelling_first_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()

            bookinpage.select_days_end()

            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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

            last_date = bookinpage.get_element(RoomBookingsPage.LAST_DATE_VALIDITY).get_attribute("title")
            last_date2 = bookinpage.change_date_format(last_date)
            print(f'Last date: {last_date2}')

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_cancelling_first_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(5)
            print("Booking should be created successfully: Passed")

            bookinpage.select_all_status()
            sleep(2)

            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)

            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)

            bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
            bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)
            # bookinpage.driver_implicitly_wait(2)

            bookinpage.cancel_booking()
            print("Create a daily recurring booking for 10 days and cancel the starting day of booking : To make a verify that other future meetings are not getting cancelled: Passed")
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            # bookinpage.driver_implicitly_wait(2)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_cancelling_first_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_cancelling_first_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

    @pytest.mark.prsc
    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_cancelling_last_recurring_booking(self):
        try:
            bookinpage = RoomBookingsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.start_selection()
            
            bookinpage.select_days_end()
            
            # Clicking on available room
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
            RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
            RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
            RoomBookingsPage.ROOM_124_CHECK_DIV_LAST = RoomBookingsPage.ROOM_124_CHECK_DIV_LAST.format(rval)
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON_LAST = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON_LAST.format(rval)

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

            last_date = bookinpage.get_element(RoomBookingsPage.LAST_DATE_VALIDITY).get_attribute("title")
            last_date2 = bookinpage.change_date_format(last_date)
            print(f'Last date: {last_date2}')

            # Clicking on booking button
            bookinpage.action_chain_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(5)
            
            bookinpage.take_screenshot(f"test_cancelling_last_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
            sleep(2)
            print("Booking should be created successfully: Passed")

            bookinpage.select_all_status()
            sleep(2)
            
            # Resource details page
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
            # bookinpage.driver_implicitly_wait(8)

            # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
            bookinpage.date_selection_chain(
                    RoomBookingsPage.RD_CALENDER_INPUT, TestData.ROOM_START_DATE[:11], 2)
            bookinpage.resource_details_page_check()
            # bookinpage.driver_implicitly_wait(5)

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
            # bookinpage.driver_implicitly_wait(5)
            bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)

            bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
            sleep(3)
            bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)
            # bookinpage.driver_implicitly_wait(2)

            bookinpage.cancel_last_booking()
            print("Create a daily recurring booking for 10 days and cancel the last day of booking : To make a verify that other future meetings are not getting cancelled: Passed")
            bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            # bookinpage.driver_implicitly_wait(2)
            bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS)
            sleep(2)
            bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_cancelling_last_recurring_booking: {e}")
            bookinpage.take_screenshot(f"test_cancelling_last_recurring_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")



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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.PRE_EXTEND_TIME = RoomBookingsPage.PRE_EXTEND_TIME.format(rval)
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
        sleep(2)
        
        bookinpage.take_screenshot(f"test_extend_single_daily_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.PRE_EXTEND_TIME = RoomBookingsPage.PRE_EXTEND_TIME.format(rval)
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
        sleep(2)
        
        bookinpage.take_screenshot(f"test_extend_single_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.PRE_EXTEND_TIME = RoomBookingsPage.PRE_EXTEND_TIME.format(rval)
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
        sleep(2)
        
        bookinpage.take_screenshot(f"test_extend_single_overlapping_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
        sleep(2)
        
        bookinpage.take_screenshot(f"test_extend_single_overlapping_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.PRE_EXTEND_TIME = RoomBookingsPage.PRE_EXTEND_TIME.format(rval)
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
        sleep(2)
        
        bookinpage.take_screenshot(f"test_extend_single_cancelled_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        # bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124)

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
        sleep(2)
        
        bookinpage.take_screenshot(f"test_extend_single_cancelled_recurring_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_CHECK_RDIV)
        sleep(2)
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_CHECK_RDIV)
        sleep(3)
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON)
        sleep(8)

        # Extend booking
        bookinpage.scroll_to_element(RoomBookingsPage.ROOM_124_CHECK_DIV)
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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.PRE_EXTEND_TIME = RoomBookingsPage.PRE_EXTEND_TIME.format(rval)
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
        sleep(2)
        
        bookinpage.take_screenshot(f"test_till_next_date_extended_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        

    
    '''Cancel Booking'''
    @pytest.mark.pcnclb
    def test_simple_daily_recurring_cancel_single_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        bookinpage.select_available_resource()

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        last_date = bookinpage.get_element(RoomBookingsPage.LAST_DATE_VALIDITY).get_attribute("title")
        last_date2 = bookinpage.change_date_format(last_date)
        print(f'Last date: {last_date2}')

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"test_simple_daily_recurring_cancel_single_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()

        # # Resource details page
        # bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        # bookinpage.resource_details_page_check()

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
        bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON, 2)

        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON, 2)
        sleep(20)
        bookinpage.action_chain_sendkeys_1(RoomBookingsPage.MAIN_CARDS_CONTAINER, Keys.HOME)
        print("Create a daily recurring booking for a month and delete any single instance: Passed")

        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        
    @pytest.mark.pcnclb
    def test_simple_daily_recurring_cancel_all_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        # bookinpage.driver_implicitly_wait(6)
        bookinpage.start_selection()

        bookinpage.select_available_resource()
        # bookinpage.driver_implicitly_wait(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.daily_repeat()

        last_date = bookinpage.get_element(RoomBookingsPage.LAST_DATE_VALIDITY).get_attribute("title")
        last_date2 = bookinpage.change_date_format(last_date)
        print(f'Last date: {last_date2}')

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"test_simple_daily_recurring_cancel_all_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        # bookinpage.driver_implicitly_wait(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        bookinpage.resource_details_page_check()

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
        bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 0)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_CHECK_RDIV, 0)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        print("Create a daily recurring booking for a month and delete all booking: Passed")
        sleep(2)
        
    @pytest.mark.pcnclb
    def test_simple_weekly_recurring_cancel_single_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on room 124 booking modal
        bookinpage.select_available_resource()

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        last_date2 = bookinpage.change_date_format(TestData.WEEKLY_REPEAT_TILL_DATE)
        print(f'Last date: {last_date2}')

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"test_simple_weekly_recurring_cancel_single_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()

        # # Resource details page
        # bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        # bookinpage.resource_details_page_check()

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
        bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON, 2)

        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON, 2)
        sleep(20)
        bookinpage.action_chain_sendkeys_1(RoomBookingsPage.MAIN_CARDS_CONTAINER, Keys.HOME)
        print("Create a daily recurring booking for a month and delete any single instance: Passed")
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 1)
        sleep(2)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 1)
        sleep(2)
        bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        
    @pytest.mark.pcnclb
    def test_simple_weekly_recurring_cancel_all_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on room 124 booking modal
        bookinpage.select_available_resource()

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Repeating meeting
        bookinpage.weekly_repeat()

        last_date2 = bookinpage.change_date_format(TestData.WEEKLY_REPEAT_TILL_DATE)
        print(f'Last date: {last_date2}')

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"test_simple_weekly_recurring_cancel_all_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.MY_BOOKING_NAV)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")

        bookinpage.date_selection_chain(RoomBookingsPage.LAST_DATE_INPUT, last_date2, 2)
        bookinpage.do_click(RoomBookingsPage.FREE_CLICK_MB)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 1)
        bookinpage.do_click_by_index(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS, 1)
        sleep(2)
        bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        print("Create a daily recurring booking for a month and delete all booking: Passed")
        sleep(2)
        
    @pytest.mark.pcnclb
    def test_simple_cancel_single_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on room 124 booking modal
        bookinpage.select_available_resource()

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(
            TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(
            RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        
        bookinpage.take_screenshot(f"test_simple_cancel_single_booking/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("Create a daily recurring booking for the desk by selecting a default date and time: Passed")


        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
        print("Create a single booking and cancel it: Passed")
        sleep(2)
        



    '''Tags Testing'''
    @pytest.mark.misc
    def test_tag_booking(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Select tag
        bookinpage.select_tag()

        # Clicking on available room
        bookinpage.select_available_resource()
        sleep(4)

        # Getting and assigning room number to selectors
        rval = bookinpage.get_room_name()
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
        sleep(2)
        
        bookinpage.take_screenshot(f"/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a tag: Passed")


    '''Test Pagination'''
    @pytest.mark.misc
    def test_pagination(self):
        bookinpage = RoomBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Checking available resources
        bookinpage.select_all_status()
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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
        sleep(2)
        
        bookinpage.take_screenshot(f"/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
            RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
        sleep(2)
        
        bookinpage.take_screenshot(f"/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)

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
        sleep(2)
        
        bookinpage.take_screenshot(f"/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
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
        RoomBookingsPage.ROOM_124 = RoomBookingsPage.ROOM_124.format(rval)
        RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_DIV = RoomBookingsPage.ROOM_124_CHECK_DIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_124_RPAGE_STATUS_CHECK.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_CHECK_RDIV = RoomBookingsPage.ROOM_124_CHECK_RDIV.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(rval)
        RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_RDIV_CANCEL_BUTTON.format(rval)
        RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = RoomBookingsPage.ROOM_124_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(rval)


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
        sleep(2)
        
        bookinpage.take_screenshot(f"/{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")
       
    
    end_time = time()

    time_taken = end_time - start_time

    print("Time taken: ", time_taken)

    # '''Send report'''
    # @pytest.mark.email
    # def test_send_email_report(self):
    #     print("Time end: ", self.end_time)
    #     print("Time taken: ", self.time_taken)
    #     print("Sending report in mail....")
    #     send_email()



sleep(5)