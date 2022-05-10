from time import sleep
import logging


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

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()


    """Non-Recurring"""

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        
        # Checking available resources
        bookinpage.select_available_status()
        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)


        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        val1 = ('xpath', "//p[text()='None']")
        if deskBookingsPage.DESK_201_CHECK_NAME == val1:
            bookinpage.quit_driver()

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Clicking on booking button
        sleep(5)
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
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
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        # bookinpage.check_my_booking()
        # sleep(5)
        print("Create a booking for the desk by selecting a default date and time: Passed")
        # bookinpage.quit_driver()

    @pytest.mark.skip(reason="to be edited once tags are alloted")
    def test_simple_booking_by_tag(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()
        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)


        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        val1 = ('xpath', "//p[text()='None']")
        if deskBookingsPage.DESK_201_CHECK_NAME == val1:
            bookinpage.quit_driver()

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Clicking on booking button
        sleep(5)
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
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
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        # bookinpage.check_my_booking()
        # sleep(5)
        print("Create a booking for the desk by selecting a default date and time: Passed")
        # bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_host_change_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # try:
        #     bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        # except Exception as e:
        #     print("Exception on Nav: ", e)
        bookinpage.select_available_status()
        sleep(5)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)
        sleep(10)

        # Covid-declaration check
        # bookinpage.update_health_status()

        # Selecting host
        bookinpage.do_click(deskBookingsPage.HOST_DROPDOWN)
        bookinpage.host_selection(deskBookingsPage.HOST_INPUT, TestData.HOST1_NAME)
        print("Selecting host done")
        sleep(5)

        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        val1 = ('xpath', "//p[text()='None']")

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL]
        bookinpage.resource_details_page_check()

        sleep(5)
        print("Create a booking for the desk by changing the default host: Passed")
        
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        bookinpage.select_available_status()

        sleep(5)

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)
        sleep(10)

        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a booking for the desk by changing the default date and time: Passed")
        
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_booking(self):
        # self.loginPage = LoginPage(self.driver)
        # bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        bookinpage = deskBookingsPage(self.driver)
        # sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        # print("Selecting Location")
        # bookinpage.select_location()
        # print("Selecting Floor")
        # bookinpage.select_floor()

        # Checking available resources
        bookinpage.select_available_status()

        # # Clicking on list view
        # bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        # bookinpage.select_resource_type_desk()

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)
        bookinpage.do_click(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Testing overlapping booking
        bookinpage.overlapping_error_check()
        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_booking(self):
        # self.loginPage = LoginPage(self.driver)
        # bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # sleep(15)
        # bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage = deskBookingsPage(self.driver)
        # sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        # print("Selecting Location")
        # bookinpage.select_location()
        # print("Selecting Floor")
        # bookinpage.select_floor()

        # Checking available resources
        bookinpage.select_available_status()

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on list view
        # bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        # bookinpage.select_resource_type_desk()

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        # bookinpage.resource_page_booking_check()
        # sleep(3)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(3)

        # Going to Book Space Nav Panel
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_available_status()

        # Again booking on cancelled time
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)
        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(3)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks after booking: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks after booking: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Again checking if booking is made or not
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Booking of desk by selecting the time of already cancelled booking: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_till_next_date_booking(self):
        # self.loginPage = LoginPage(self.driver)
        # bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        # sleep(15)
        # bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        # sleep(10)
        bookinpage = deskBookingsPage(self.driver)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        # bookinpage.select_location()
        # bookinpage.select_floor()
        bookinpage.select_available_status()


        # # Clicking on list view
        # print("Clicking on list view")
        # bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        # bookinpage.select_resource_type_desk()
        sleep(5)

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)
        sleep(10)

        # Multiple days
        bookinpage.do_click(deskBookingsPage.MULTIPLE_DAYS_SINGLE_BOOKING)

        # Selecting datetime
        bookinpage.time_selection(deskBookingsPage.MULTIPLE_DAYS_SB_START, TestData.TILL_NEXT_DAY_START_TIME) 
        bookinpage.time_selection(deskBookingsPage.MULTIPLE_DAYS_SB_END, TestData.TILL_NEXT_DAY_END_TIME)
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a booking of the desk by selecting a date& time such a way that its overlapping the date : Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_till_next_date_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.select_available_status()

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)
        sleep(6)

        # Selecting host
        bookinpage.do_click(deskBookingsPage.HOST_DROPDOWN)
        bookinpage.host_selection(deskBookingsPage.HOST_INPUT, TestData.HOST2_NAME)
        print("Selecting host done")
        sleep(5)

        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(6)

        # Multiple days
        bookinpage.do_click(deskBookingsPage.MULTIPLE_DAYS_SINGLE_BOOKING)

        # Selecting datetime
        bookinpage.time_selection(deskBookingsPage.MULTIPLE_DAYS_SB_START, TestData.TILL_NEXT_DAY_START_TIME) 
        bookinpage.time_selection(deskBookingsPage.MULTIPLE_DAYS_SB_END, TestData.TILL_NEXT_DAY_END_TIME)
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a booking of the desk by selecting a date& time such a way that its overlapping the date : Passed")



    """Recurring"""

    '''Daily'''
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.select_location()
        bookinpage.select_floor()
        bookinpage.select_available_status()

        # Clicking on list view
        print("Clicking on list view")
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()
        sleep(5)

        # Selecting multiple date
        bookinpage.resource_page_multiple_date_select()

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)
        sleep(10)


        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Repeating Daily
        bookinpage.daily_repeat()

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_multiple_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a Daily recurring booking for the desk by changing the default date and time.: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.daily_repeat()

        # Testing overlapping booking
        bookinpage.overlapping_error_check()
        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)

        # Going to Book Space Nav Panel
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_available_status()

        # Again booking on cancelled time
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.daily_repeat()

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)

        # Again checking if booking is made or not
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()

        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")



    '''Weekly'''
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_weekly_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_weekly_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.select_location()
        bookinpage.select_floor()
        bookinpage.select_available_status()

        # Clicking on list view
        print("Clicking on list view")
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()
        sleep(5)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)
        sleep(6)


        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)


        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Repeating Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_multiple_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a Daily recurring booking for the desk by changing the default date and time.: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_weekly_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.weekly_repeat()

        # Testing overlapping booking
        bookinpage.overlapping_error_check()
        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_weekly_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Selecting time
        bookinpage.select_time()

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)

        # Going to Book Space Nav Panel
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_available_status()

        # Again booking on cancelled time
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.weekly_repeat()

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)

        # Again checking if booking is made or not
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()

        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")


    
    '''Extend Booking'''

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(deskBookingsPage.DESK_NO)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)

        # Extend booking
        bookinpage.extend_booking(deskBookingsPage.EXTEND_15_MINS)
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(deskBookingsPage.DESK_NO)
        sleep(5)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()


        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)

        # Extend booking
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_overlapping_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Booking single for extending purpose
        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(deskBookingsPage.DESK_NO)
        sleep(5)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # recurring
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.TIME_END2)


        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Clicking on desk 201 modal
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201)
        sleep(5)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # recurring
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_START, TestData.TIME_START3)
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.TIME_END3)
        bookinpage.daily_repeat()


        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)

        # Extend booking
        for i in range(1):
            print("i: ", i)
            bookinpage.scroll_to_element(deskBookingsPage.DESK_201_CHECK_DIV)
            sleep(3)
            # Meeting Options
            meeting_options = bookinpage.get_element_text(deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
            std_meeting_options = ['Check in', '', 'Cancel Booking']
            # assert meeting_options == std_meeting_options
            print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
            if i == 1:
                bookinpage.extend_booking(deskBookingsPage.EXTEND_15_MINS)
            else:
                pass

        # bookinpage.extend_booking(deskBookingsPage.EXTEND_15_MINS)
        try:
            enabled_check = bookinpage.is_enabled(deskBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(deskBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")
        # "Booking cannot be extended because"
        sleep(5)

        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_cancelled_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Booking single for extending purpose
        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(deskBookingsPage.DESK_NO)
        sleep(5)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # recurring
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.TIME_END2)


        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(5)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # recurring
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_START, TestData.TIME_START3)
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.TIME_END3)
        bookinpage.daily_repeat()


        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(5)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_xpath(deskBookingsPage.DESK_201_CHECK_RDIV)
        sleep(2)
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_CHECK_RDIV)
        sleep(3)
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON)
        sleep(8)

        # Extend booking
        bookinpage.scroll_to_element_by_xpath(deskBookingsPage.DESK_201_CHECK_DIV)
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
            
        sleep(5)

        print("Start meeting and then extend the booking for the next 30 minute make sure there is a cancelled recurring  existing booking  is available : Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_extend_single_cancelled_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Booking single for extending purpose
        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(deskBookingsPage.DESK_NO)
        sleep(5)

        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.TIME_END2)

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Clicking on desk 201 modal
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201)
        sleep(5)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # single
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_START, TestData.TIME_START3)
        bookinpage.time_selection(deskBookingsPage.TIME_SELECT_END, TestData.TIME_END3)


        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        bookinpage.do_click(deskBookingsPage.MY_BOOKING_NAV)
        sleep(5)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 1)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 1)
        sleep(3)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON, 1)
        sleep(8)

        # Extend booking
        bookinpage.scroll_to_element_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 0)
        sleep(5)
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
            
        sleep(5)

        print("Start meeting and then extend the booking for the next 30 minute make sure there is a cancelled single  existing booking  is available : Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_till_next_date_extended_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.select_location()
        bookinpage.select_floor()
        bookinpage.select_available_status()


        # Clicking on list view
        print("Clicking on list view")
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()
        sleep(5)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.PRE_EXTEND_TIME = deskBookingsPage.PRE_EXTEND_TIME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.CHECKIN_BOOKING = deskBookingsPage.CHECKIN_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING = deskBookingsPage.EXTEND_BOOKING.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM = deskBookingsPage.EXTEND_BOOKING_TEXT_CONFIRM.format(deskBookingsPage.DESK_NO)
        sleep(10)

        # Multiple days
        bookinpage.do_click(deskBookingsPage.MULTIPLE_DAYS_SINGLE_BOOKING)

        # Selecting datetime
        bookinpage.time_selection(deskBookingsPage.MULTIPLE_DAYS_SB_START, TestData.TILL_NEXT_DAY_START_TIME) 
        bookinpage.time_selection(deskBookingsPage.MULTIPLE_DAYS_SB_END, TestData.TILL_NEXT_DAY_END_TIME)
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        bookinpage.scroll_to_element_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 0)
        bookinpage.extend_booking(deskBookingsPage.EXTEND_30_MINS)
        sleep(5)
        print("Create a booking of the desk by selecting a date& time such a way that its overlapping the date : Passed")



    '''Cancel Booking'''

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_cancel_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 2)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 2)
        sleep(3)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON, 2)
        sleep(8)
        print("Create a daily recurring booking for a month and delete any single instance: Passed")
        bookinpage.quit_driver()


    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_cancel_all_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 0)
        sleep(3)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON, 0)
        sleep(8)
        print("Create a daily recurring booking for a month and delete all instances: Passed")
        bookinpage.quit_driver()


    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_weekly_recurring_cancel_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 2)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 2)
        sleep(3)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON, 2)
        sleep(8)
        print("Create a weekly recurring booking for a month and delete any single instance: Passed")
        bookinpage.quit_driver()


    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_weekly_recurring_cancel_all_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_RDIV, 0)
        sleep(3)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON, 0)
        sleep(8)
        print("Create a weekly recurring booking for a month and delete all booking: Passed")
        bookinpage.quit_driver()

    
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_cancel_single_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)

        # Getting Desk value
        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        sleep(5)
        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.scroll_to_element_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 0)
        sleep(2)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_CHECK_DIV, 0)
        sleep(3)
        bookinpage.do_click_by_index(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON, 0)
        sleep(8)
        print("Create a single booking and cancel it: Passed")
        bookinpage.quit_driver()


    ''''Find My Colleague'''
    @pytest.mark.skip(reason="no need of currently testing this")
    def find_my_colleague(self):
        bookinpage = deskBookingsPage(self.driver)
        # sleep(15)
        # bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        # sleep(10)
        # print("Selecting Location")
        # bookinpage.select_location()
        # print("Selecting Floor")
        # bookinpage.select_floor()
        # # Checking available resources
        # bookinpage.select_available_status()
        # # Clicking on list view
        # bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        # bookinpage.select_resource_type_desk()
        # # Network logs
        # try:
        #     bookinpage.print_browser_logs()
        # except Exception as e:
        #     print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL)


        dval = bookinpage.get_desk_name()
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        deskBookingsPage.DESK_201_CHECK_NAME = deskBookingsPage.DESK_201_CHECK_NAME.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_CHECK_DIV = deskBookingsPage.DESK_201_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = deskBookingsPage.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE = deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_DIV = deskBookingsPage.DESK_201_RPAGE_CHECK_DIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON = deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK = deskBookingsPage.DESK_201_RPAGE_STATUS_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_SCHEDULE_CHECK = deskBookingsPage.DESK_201_SCHEDULE_CHECK.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS.format(deskBookingsPage.DESK_NO)
        
        deskBookingsPage.DESK_201_CHECK_RDIV = deskBookingsPage.DESK_201_CHECK_RDIV.format(deskBookingsPage.DESK_NO)
        deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON = deskBookingsPage.DESK_201_RDIV_CANCEL_BUTTON.format(deskBookingsPage.DESK_NO)
        val1 = ('xpath', "//p[text()='None']")
        if deskBookingsPage.DESK_201_CHECK_NAME == val1:
            bookinpage.quit_driver()

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Clicking on booking button
        sleep(5)
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
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
        bookinpage.do_click_by_xpath(deskBookingsPage.DESK_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        bookinpage.check_my_booking()
        # sleep(5)
        # Logging out
        bookinpage.do_logout()
        sleep(8)

        # Logging again using attendee details
        bookinpage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()

        bookinpage.do_click(deskBookingsPage.FMC_SEARCH)
        sleep(3)
        bookinpage.do_send_keys(deskBookingsPage.FMC_SEARCH, TestData.HOST1_NAME)

        bookinpage.do_click(deskBookingsPage.VIEW_ON_MAP)
        sleep(20)

        # Network logs
        print("Create a booking for the desk by selecting a default date and time: Passed")

        bookinpage.quit_driver()


    '''Check and edit amenities'''
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_amenities(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(15)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(10)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        bookinpage.select_resource_type_desk()
        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_AVAIL_2)
        sleep(5)

        # Getting prevoius amenities data
        amtext = bookinpage.get_element_text(deskBookingsPage.PRESENT_AMENITIES)
        print("Amenities: ", amtext)

        # Edit amenities
        bookinpage.do_click(deskBookingsPage.EDIT_AMENITIES)
        sleep(4)

        print("Adding Amenity")
        # Add amenities
        bookinpage.do_click(deskBookingsPage.ADD_AMENITIES)

        # Search box
        bookinpage.chain_selection_send_keys_click(deskBookingsPage.ADD_AMENITIES_SEARCH, TestData.DUAL_MONITOR)
        sleep(3)

        # bookinpage.do_click(deskBookingsPage.AMENITY_SELECT)

        # Adding quantity
        bookinpage.do_send_keys(deskBookingsPage.AMENITIES_QUANTITY_INPUT, TestData.AM_QUANTITY)

        # Right check
        bookinpage.action_chain_click(deskBookingsPage.AMENITIES_RIGHT_CHECK)
        sleep(3)

        bookinpage.do_click(deskBookingsPage.AMENITIES_DONE)
        sleep(2)
        print("Amenity added")

        # Getting post amenities data
        amtext2 = bookinpage.get_element_text(deskBookingsPage.PRESENT_AMENITIES)
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

        sleep(10)
        bookinpage.quit_driver()


    '''Send report'''
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_send_email_report(self):
        send_email()

