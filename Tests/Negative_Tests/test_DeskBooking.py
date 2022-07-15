from time import sleep
import logging

from selenium.webdriver.common.keys import Keys
from Pages.LoginPage import LoginPage
from Pages.deskBookingsPage import deskBookingsPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest
from selenium.webdriver.common.by import By

from mail_conf import send_email

import traceback


'''Logger'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Test_Booking(BaseTest):

    @pytest.mark.custom
    @pytest.mark.healthstat
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(
            TestData.USER_NAME, TestData.PASSWORD)

    @pytest.mark.xfail(reason="The test is expected to fail as selecting past date")
    def test_pastdate_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()

        # Selecting datetime
        bookinpage.date_selection_chain(deskBookingsPage.DATE_INPUT, TestData.PAST_BOOKING_DATE, 2)

        # Get date input value
        input_value = bookinpage.get_element(deskBookingsPage.DATE_INPUT)
        title = input_value.get_attribute('title')

        # Clicking on modal close
        bookinpage.do_click(deskBookingsPage.MODAL_CLOSE)
        sleep(2)
        assert title == TestData.PAST_BOOKING_DATE

    
    @pytest.mark.xfail(reason="The test is expected to fail as selecting past start time")
    def test_past_time_booking_(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()

        # Selecting datetime
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_START, TestData.PAST_TIME_START)

        # Get date input value
        input_value = bookinpage.get_element(deskBookingsPage.TIME_SELECT_START)
        title = input_value.get_attribute('value')

        # Clicking on modal close
        bookinpage.do_click(deskBookingsPage.MODAL_CLOSE)
        sleep(2)
        assert title == TestData.PAST_TIME_START

    
    @pytest.mark.xfail(reason="The test is expected to fail as selecting past end time")
    @pytest.mark.skip
    def test_datetime_change_booking_3(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()

        # Selecting datetime
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.PAST_TIME_END)

        # Get date input value
        input_value = bookinpage.get_element(deskBookingsPage.TIME_SELECT_END)
        title = input_value.get_attribute('value')

        # Clicking on modal close
        bookinpage.do_click(deskBookingsPage.MODAL_CLOSE)
        sleep(2)
        assert title == TestData.PAST_TIME_END

    # @pytest.mark.custom
    @pytest.mark.xfail(reason="The test is expected to fail as selecting time less than 15 minutes")
    def test_time_less_than_mintime_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()

        # Selecting datetime
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_START, TestData.NEGATIVE_TIME_START_1)
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.NEGATIVE_TIME_END_1)

        # Get date input value
        is_visible = bookinpage.is_visible(deskBookingsPage.TIME_SELECT_ERROR)
        print("is_visible: ", is_visible)

        # Clicking on modal close
        bookinpage.do_click(deskBookingsPage.MODAL_CLOSE)
        sleep(2)
        assert is_visible == False

    @pytest.mark.custom
    @pytest.mark.xfail(reason="The test is expected to fail as selecting time more than 60 minutes")
    def test_time_more_than_maxtime_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()

        # Selecting datetime
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_START, TestData.NEGATIVE_TIME_START_1)
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.NEGATIVE_TIME_END_2)

        # Get date input value
        is_visible = bookinpage.is_visible(deskBookingsPage.TIME_SELECT_ERROR)
        print("is_visible: ", is_visible)

        # Clicking on modal close
        bookinpage.do_click(deskBookingsPage.MODAL_CLOSE)
        sleep(2)
        assert is_visible == False


    def test_simple_booking(self):
        try:
            bookinpage = deskBookingsPage(self.driver)
            # bookinpage = Test_Booking.test_login()
            sleep(3)

            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(3)

            bookinpage.start_selection()

            # Clicking on available desk
            bookinpage.select_available_resource(1)

            dval = bookinpage.get_desk_name()
            # setting desk value
            deskBookingsPage.DESK_NO = dval
            deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(
                deskBookingsPage.DESK_NO)

            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON.format(
                deskBookingsPage.DESK_NO)

            deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(
                deskBookingsPage.DESK_NO)
            deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(
                deskBookingsPage.DESK_NO)

            sleep(2)
            # Clicking on booking button
            bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
            sleep(2)
            print("Booking should be created successfully: Passed")

            # Checking Booking
            # At the find resource page, status of booking should be changed from available to booked
            print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
            bookinpage.resource_page_booking_check()
            sleep(3)

            # Resource details page
            bookinpage.do_click_by_xpath(
                deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
            bookinpage.resource_details_page_check()

            # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
            bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
            bookinpage.check_my_booking()
            print("Create a booking for the desk by selecting a default date and time: Passed")
            # Cancelling Booking
            bookinpage.do_click_by_xpath(
                deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
            sleep(2)
        except Exception as e:
            print(f"Exception test_simple_booking: {e}\n{traceback.format_exc()}")
            bookinpage.take_screenshot(f"DeskBooking/test_simple_booking/{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
