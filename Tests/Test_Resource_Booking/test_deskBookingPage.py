from time import sleep
import logging

from selenium.webdriver.common.keys import Keys
from Pages.LoginPage import LoginPage
from Pages.deskBookingsPage import deskBookingsPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest

from mail_conf import send_email


'''Logger'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Test_Booking(BaseTest):

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
    # @pytest.mark.dependency()
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(
            TestData.USER_NAME, TestData.PASSWORD)
        sleep(3)
        return bookinpage

    """Non-Recurring"""

    @pytest.mark.pnr
    # @pytest.mark.dependency(depends=["test_login"])
    def test_simple_booking(self):
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
        bookinpage.select_booked_status()
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

    @pytest.mark.hostrltd
    def test_host_change_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()
        sleep(2)

        # Covid-declaration check
        # bookinpage.update_health_status()

        # Selecting host
        bookinpage.do_click(deskBookingsPage.HOST_DROPDOWN)
        bookinpage.host_selection(
            deskBookingsPage.HOST_INPUT, TestData.HOST1_NAME)
        print("Selecting host done")
        sleep(2)

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
        val1 = ('xpath', "//p[text()='None']")

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(2)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL]
        bookinpage.resource_details_page_check()

        sleep(2)
        print("Create a booking for the desk by changing the default host: Passed")

    @pytest.mark.pnr
    # @pytest.mark.dependency(depends=["test_login"])
    def test_datetime_change_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource(2)

        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Getting Desk value
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

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(3)

        # Checking Booking
        bookinpage.select_booked_status()

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(3)

        bookinpage.date_selection_chain(
            deskBookingsPage.RD_CALENDER_INPUT, TestData.BOOKING_DATE, 2)
        bookinpage.resource_details_page_check()
        sleep(3)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by changing the default date and time: Passed")
        # Cancelling Booking
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)

    @pytest.mark.pnr
    # @pytest.mark.dependency(depends=["test_login"])
    def test_overlapping_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Clicking on available desk modal
        bookinpage.select_available_resource(3)

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
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
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(
            deskBookingsPage.DESK_NO)

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(3)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()

        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)
        sleep(2)

        # Testing overlapping booking
        bookinpage.overlapping_error_check()

        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")
        sleep(2)

        # Cancelling Booking
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        bookinpage.scroll_to_element_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)

    @pytest.mark.pnr
    # @pytest.mark.dependency(depends=["test_login"])
    def test_already_cancelled_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource(4)

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
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

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(3)

        # Going to Book Space Nav Panel
        bookinpage.scroll_to_element(deskBookingsPage.BOOK_SPACE_NAV)
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_all_status()

        # Again booking on cancelled time
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Selecting time
        bookinpage.select_time()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(3)

        # Again checking if booking is made or not
        bookinpage.action_chain_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        print("Booking of desk by selecting the time of already cancelled booking: Passed")
        sleep(2)

    # @pytest.mark.pnr
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_till_next_date_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()
        sleep(2)

        # Multiple days
        bookinpage.do_click(deskBookingsPage.MULTIPLE_DAYS_SINGLE_BOOKING)

        # Selecting datetime
        bookinpage.date_selection_chain(
            deskBookingsPage.MULTIPLE_DAYS_SB_START, TestData.TILL_NEXT_DAY_START_TIME)
        bookinpage.date_selection_chain(
            deskBookingsPage.MULTIPLE_DAYS_SB_END, TestData.TILL_NEXT_DAY_END_TIME)
        bookinpage.date_selection_chain(
            deskBookingsPage.MULTIPLE_DAYS_SB_START, TestData.TILL_NEXT_DAY_START_TIME)
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(
            deskBookingsPage.MULTIPLE_DAYS_SB_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(
            deskBookingsPage.MULTIPLE_DAYS_SB_END)
        print("startcheck: ", end_check)

        # Getting Desk value
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

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(2)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        # bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL,
                     TestData.TILL_NEXT_DAY_START_TIME, TestData.TILL_NEXT_DAY_END_TIME]
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)
        print("Create a booking of the desk by selecting a date& time such a way that its overlapping the date : Passed")

    # @pytest.mark.pnr
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_overlapping_till_next_date_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()
        sleep(2)

        # Selecting host
        bookinpage.do_click(deskBookingsPage.HOST_DROPDOWN)
        bookinpage.host_selection(
            deskBookingsPage.HOST_INPUT, TestData.HOST2_NAME)
        print("Selecting host done")
        sleep(2)

        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(2)

        # Multiple days
        bookinpage.do_click(deskBookingsPage.MULTIPLE_DAYS_SINGLE_BOOKING)

        # Selecting datetime
        bookinpage.time_selection(
            deskBookingsPage.MULTIPLE_DAYS_SB_START, TestData.TILL_NEXT_DAY_START_TIME)
        bookinpage.time_selection(
            deskBookingsPage.MULTIPLE_DAYS_SB_END, TestData.TILL_NEXT_DAY_END_TIME)
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Getting Desk value
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

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(2)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME,
                     TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(2)
        print("Create a booking of the desk by selecting a date& time such a way that its overlapping the date : Passed")

    """Recurring"""

    '''Daily'''
    @pytest.mark.pr
    def test_simple_daily_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Getting Desk value
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

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        bookinpage.resource_details_page_check()

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        # Cancelling Booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")

    @pytest.mark.pr
    def test_datetime_change_daily_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()

        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Repeating Daily
        bookinpage.daily_repeat()

        # Getting Desk value
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

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(2)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_all_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_multiple_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        bookinpage.resource_details_date_select()
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        # Cancelling Booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        print("Create a Daily recurring booking for the desk by changing the default date and time.: Passed")

    @pytest.mark.pr
    def test_overlapping_daily_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
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

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.daily_repeat()

        # Testing overlapping booking
        bookinpage.overlapping_error_check()

        # Cancelling Booking
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        bookinpage.scroll_to_element_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")
        sleep(2)

    @pytest.mark.pr
    def test_already_cancelled_daily_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
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

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)

        # Going to Book Space Nav Panel
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_all_status()

        # Again booking on cancelled time
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.daily_repeat()

        # Selecting time
        bookinpage.select_time()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(4)
        # Again checking if booking is made or not
        bookinpage.check_my_booking()

        # Cancelling Booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")
        sleep(2)

    '''Weekly'''
    # @pytest.mark.prw

    def test_simple_weekly_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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

        # Repeat Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        bookinpage.resource_details_page_check()

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        # Cancelling Booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")

    @pytest.mark.prw
    def test_datetime_change_weekly_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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

        # Selecting datetime
        bookinpage.selecting_date(1)
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Repeating Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(2)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_all_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_multiple_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        bookinpage.resource_details_date_select()
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        # Cancelling Booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        print("Create a Daily recurring booking for the desk by changing the default date and time.: Passed")

    @pytest.mark.prw
    def test_overlapping_weekly_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
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

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.weekly_repeat()

        # Testing overlapping booking
        bookinpage.overlapping_error_check()
        sleep(2)
        # Cancelling Booking
        bookinpage.scroll_to_element_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")

    @pytest.mark.prw
    def test_already_cancelled_weekly_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
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

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(4)
        print("Booking should be created successfully: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)

        # Going to Book Space Nav Panel
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_all_status()

        # Again booking on cancelled time
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.weekly_repeat()

        # Selecting time
        bookinpage.select_time()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(4)

        # Again checking if booking is made or not
        bookinpage.check_my_booking()

        # Cancelling Booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")

    '''Extend Booking'''
    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_daily_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Network logs

        # Get total desks value

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(
            deskBookingsPage.DESK_NO)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        sleep(2)

        # Extend booking
        bookinpage.extend_booking(deskBookingsPage.EXTEND_15_MINS)
        sleep(2)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Network logs

        # Get total desks value

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(
            deskBookingsPage.DESK_NO)
        sleep(2)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        sleep(2)

        # Extend booking
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
        sleep(2)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_overlapping_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Network logs

        # Get total desks value

        # Booking single for extending purpose
        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(
            deskBookingsPage.DESK_NO)
        sleep(2)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # recurring
        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_END, TestData.TIME_END2)

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Clicking on available desk
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201)
        sleep(2)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # recurring
        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_START, TestData.TIME_START3)
        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_END, TestData.TIME_END3)
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        sleep(2)

        # Extend booking
        for i in range(1):
            print("i: ", i)
            bookinpage.scroll_to_element(deskBookingsPage.DESK_201_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = bookinpage.get_element_text(
                deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            # assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            if i == 1:
                bookinpage.extend_booking(deskBookingsPage.EXTEND_15_MINS)
            else:
                pass

        # bookinpage.extend_booking(deskBookingsPage.EXTEND_15_MINS)
        try:
            enabled_check = bookinpage.is_enabled(
                deskBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(
                    deskBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")
        # "Booking cannot be extended because"
        sleep(2)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_cancelled_recurring_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Network logs

        # Get total desks value

        # Booking single for extending purpose
        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(
            deskBookingsPage.DESK_NO)
        sleep(2)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # recurring
        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_END, TestData.TIME_END2)

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Clicking on available desk
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(2)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # recurring
        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_START, TestData.TIME_START3)
        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_END, TestData.TIME_END3)
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(2)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_xpath(
            deskBookingsPage.DESK_201_CHECK_RDIV)
        sleep(2)
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_CHECK_RDIV)
        sleep(3)
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON)
        sleep(2)

        # Extend booking
        bookinpage.scroll_to_element_by_xpath(
            deskBookingsPage.DESK_201_CHECK_DIV)
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)

        sleep(2)

        print("Start meeting and then extend the booking for the next 30 minute make sure there is a cancelled recurring  existing booking  is available : Passed")

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_extend_single_cancelled_single_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Network logs

        # Get total desks value

        # Booking single for extending purpose
        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(
            deskBookingsPage.DESK_NO)
        sleep(2)

        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_END, TestData.TIME_END2)

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Clicking on available desk
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201)
        sleep(2)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # single
        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_START, TestData.TIME_START3)
        bookinpage.time_selection(
            deskBookingsPage.TIME_SELECT_END, TestData.TIME_END3)

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(2)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_CHECK_DIV, 1)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 1)
        sleep(3)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON, 1)
        sleep(2)

        # Extend booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_CHECK_DIV, 0)
        sleep(2)
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)

        sleep(2)

        print("Start meeting and then extend the booking for the next 30 minute make sure there is a cancelled single  existing booking  is available : Passed")

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.extndb
    def test_till_next_date_extended_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(
            deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(
            deskBookingsPage.DESK_NO)
        sleep(2)

        # Multiple days
        bookinpage.do_click(deskBookingsPage.MULTIPLE_DAYS_SINGLE_BOOKING)

        # Selecting datetime
        bookinpage.time_selection(
            deskBookingsPage.MULTIPLE_DAYS_SB_START, TestData.TILL_NEXT_DAY_START_TIME)
        bookinpage.time_selection(
            deskBookingsPage.MULTIPLE_DAYS_SB_END, TestData.TILL_NEXT_DAY_END_TIME)
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(
            deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(2)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME,
                     TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(2)
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_CHECK_DIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 0)
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
        sleep(2)
        print("Create a booking of the desk by selecting a date& time such a way that its overlapping the date : Passed")

    '''Cancel Booking'''

    @pytest.mark.pcnclb
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_simple_daily_recurring_cancel_single_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        sleep(2)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON, 2)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON, 2)
        sleep(15)

        bookinpage.action_chain_sendkeys_1(
            deskBookingsPage.MAIN_CARDS_CONTAINER, Keys.HOME)
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        print("Create a daily recurring booking for a month and delete any single instance: Passed")

    @pytest.mark.pcnclb
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_simple_daily_recurring_cancel_all_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)


        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        sleep(2)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_CHECK_RDIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 0)
        sleep(3)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(15)
        print(
            "Create a daily recurring booking for a month and delete all instances: Passed")
        
    @pytest.mark.pcnclb
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_simple_weekly_recurring_cancel_single_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)


        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        sleep(2)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON, 2)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_MEETING_OPTIONS_FOLLOWING_CANCEL_BUTTON, 2)
        sleep(15)
        print("Create a weekly recurring booking for a month and delete any single instance: Passed")
        bookinpage.action_chain_sendkeys_1(
            deskBookingsPage.MAIN_CARDS_CONTAINER, Keys.HOME)
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)

    @pytest.mark.pcnclb
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_simple_weekly_recurring_cancel_all_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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


        # Repeat Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)


        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        sleep(2)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(
            deskBookingsPage.DESK_201_CHECK_RDIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 0)
        sleep(3)
        bookinpage.do_click_by_index(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON)
        sleep(2)
        print(
            "Create a weekly recurring booking for a month and delete all booking: Passed")

    @pytest.mark.pcnclb
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_simple_cancel_single_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

        # Getting Desk value
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


        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)


        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        sleep(2)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_CHECK_DIV)
        sleep(3)
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)
        print("Create a single booking and cancel it: Passed")

    ''''Find My Colleague'''
    @pytest.mark.misc
    def find_my_colleague(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Clicking on available desk
        bookinpage.select_available_resource()

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
        val1 = ('xpath', "//p[text()='None']")
        # Clicking on booking button
        sleep(2)
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        print("Desk_no_confirm: ", deskBookingsPage.DESK_NO)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        print("Xpath: ", deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        bookinpage.check_my_booking()
        # sleep(2)
        # Logging out
        bookinpage.do_logout()
        sleep(2)

        # Logging again using attendee details
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()

        bookinpage.do_click(deskBookingsPage.FMC_SEARCH)
        sleep(3)
        bookinpage.do_send_keys(
            deskBookingsPage.FMC_SEARCH, TestData.HOST1_NAME)

        bookinpage.do_click(deskBookingsPage.VIEW_ON_MAP)
        sleep(20)

        # Network logs
        print("Create a booking for the desk by selecting a default date and time: Passed")

    '''Select by tag'''

    @pytest.mark.misc
    def test_simple_booking_by_tag(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()

        # Network logs

        # Get total desks value

        # Clicking on available desk
        bookinpage.select_available_resource()

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
        val1 = ('xpath', "//p[text()='None']")
        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Clicking on booking button
        sleep(2)
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(2)
        print("Booking should be created successfully: Passed")

        print("Desk_no_confirm: ", deskBookingsPage.DESK_NO)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        # bookinpage.resource_page_booking_check()
        sleep(3)

        print("Xpath: ", deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        # Resource details page
        bookinpage.do_click_by_xpath(
            deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(2)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(2)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(2)
        # bookinpage.check_my_booking()
        # sleep(2)
        print("Create a booking for the desk by selecting a default date and time: Passed")

    '''Check and edit amenities'''
    @pytest.mark.misc
    def test_amenities(self):
        bookinpage = deskBookingsPage(self.driver)
        sleep(3)

        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)

        bookinpage.start_selection()
        # Network logs

        # Get total desks value

        # Clicking on available desk
        bookinpage.select_available_resource(1)
        sleep(2)

        # Getting prevoius amenities data
        amtext = bookinpage.get_element_text(
            deskBookingsPage.PRESENT_AMENITIES)
        print("Amenities: ", amtext)

        # Edit amenities
        bookinpage.do_click(deskBookingsPage.EDIT_AMENITIES)
        sleep(4)

        print("Adding Amenity")
        # Add amenities
        bookinpage.do_click(deskBookingsPage.ADD_AMENITIES)

        # Search box
        bookinpage.chain_selection_send_keys_click(
            deskBookingsPage.ADD_AMENITIES_SEARCH, TestData.DUAL_MONITOR)
        sleep(3)

        # bookinpage.do_click(deskBookingsPage.AMENITY_SELECT)

        # Adding quantity
        bookinpage.do_send_keys(
            deskBookingsPage.AMENITIES_QUANTITY_INPUT, TestData.AM_QUANTITY)

        # Right check
        bookinpage.action_chain_click(deskBookingsPage.AMENITIES_RIGHT_CHECK)
        sleep(3)

        bookinpage.do_click(deskBookingsPage.AMENITIES_DONE)
        sleep(2)
        print("Amenity added")

        # Getting post amenities data
        amtext2 = bookinpage.get_element_text(
            deskBookingsPage.PRESENT_AMENITIES)
        print("Amenities2: ", amtext2)

        assert amtext != amtext2

        # Removing Amenity
        print("Removing Amenity")
        # Edit amenities
        bookinpage.do_click(deskBookingsPage.EDIT_AMENITIES)
        sleep(4)

        bookinpage.do_click(deskBookingsPage.AMENITIES_REMOVE)
        sleep(4)

        bookinpage.do_click(deskBookingsPage.AMENITIES_DONE)
        print("Amenity Removed")

        sleep(2)

    '''Send report'''

    def test_send_email_report(self):
        print("Sending report in mail....")
        send_email()


sleep(2)
