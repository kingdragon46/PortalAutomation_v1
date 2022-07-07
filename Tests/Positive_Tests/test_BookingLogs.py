import json
from time import time, sleep
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from Pages.LoginPage import LoginPage
from Pages.RoomBookingPage import RoomBookingsPage
from Pages.BookingLogsPage import BookingLogsPage
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
    def test_login_booking(self):
        print("Start time: ", self.start_time)
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(
                    TestData.USER_NAME, TestData.PASSWORD)
        # sleep(3)

    """Room Booking"""

    @pytest.mark.pnr
    # @pytest.mark.login
    @pytest.mark.selected
    def test_simple_booking_logs(self):
        try:
            # obj = self.test_login_MyBookings_ROOM_booking()
            bookinpage = BookingLogsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.BOOKING_LOGS_URL)
            sleep(3)
            
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.test_selector_click()
            # Clicking on available room

            # Getting logs
            # p_log = bookinpage.p_log()
            # responses = [bookinpage.process_log(log) for log in p_log]
            # with open("b_logs_11.json", "a", encoding="utf-8") as f:
            #     f.write("{")
            #     f.write(json.dumps(responses)+",")
            #     f.write("}")

            ele = bookinpage.get_element(BookingLogsPage.BookingLog_DATA_TABLE_ROW_1)
            key = ele.get_attribute("data-row-key")
            print("data-key: ", key)

            sleep(2)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(5)
            bookinpage.start_selection()
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
            RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
            RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)

            '''Booking Modal'''

            # Attendee Details
            # New Member
            NEW_CONTACT_1 = (ran_name())[0]
            NEW_CONTACT_1_EMAIL = Config.name_to_mail(NEW_CONTACT_1)
            bookinpage.new_contact_guest(
                NEW_CONTACT_1, NEW_CONTACT_1_EMAIL)
            NEW_CONTACT_2 = (ran_name())[0]
            NEW_CONTACT_2_EMAIL = Config.name_to_mail(NEW_CONTACT_2)
            bookinpage.new_contact_guest(
                NEW_CONTACT_2, NEW_CONTACT_2_EMAIL)
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

            # loader invisibilty check
            loader = bookinpage.is_visible(RoomBookingsPage.VRS_LOADER)
            print("loader: ", loader)

            ele2 = bookinpage.get_element(RoomBookingsPage.BookResource_Modal_START_DATE)
            ele2_text = ele2.get_attribute('title')
            print("bl_BookResource_Modal_START_DATE: ", ele2_text)
            d_formatted = Config.tr_date_format(ele2_text)
            print("bl_time2: ", d_formatted)

            # Clicking on booking button
            bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
            bookinpage.take_screenshot(f"RoomBooking/test_simple_booking/{TestData.CDATE[:10]}/pr{TestData.CDATE[11:]}.png")
            
            bookinpage.driver_get_url(TestData.BOOKING_LOGS_URL)
            sleep(8)

            print('Starting selection')
            bookinpage.resource_selection(2)

            bookinpage.verify_booking_status_filter(3)
            
            sleep(5)
            # bookinpage.date_selection(2, 30)

            # bookinpage.guest_host_selection(1, TestData.DEFAULT_HOSTNAME)

            # Getting data-key
            ele = bookinpage.get_element(BookingLogsPage.BookingLog_DATA_TABLE_ROW_1)
            key = ele.get_attribute("data-row-key")
            print("data-key: ", key)
            # Verifying matrix
            print("Verifying Booking Logs Data Matrix: Passed")
            # Selecting tr element
            BookingLogsPage.BookingLog_BookingDetailsPage_BOOKED_I_BUTTON = BookingLogsPage.BookingLog_BookingDetailsPage_BOOKED_I_BUTTON.format(rval, d_formatted)
            print("Xpath selector: ", BookingLogsPage.BookingLog_BookingDetailsPage_BOOKED_I_BUTTON)
            bookinpage.action_chain_click((By.XPATH, BookingLogsPage.BookingLog_BookingDetailsPage_BOOKED_I_BUTTON))
            bookinpage.booking_details_data_verification()
            sleep(2)
        except Exception as e:
            print(f"Exception test_simple_booking: {e}")
            bookinpage.take_screenshot(f"BookingLogs/test_simple_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")


    # @pytest.mark.login
    def test_recurring_booking_logs(self):
        try:
            # obj = self.test_login_MyBookings_ROOM_booking()
            bookinpage = BookingLogsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.BOOKING_LOGS_URL)
            sleep(3)
            
            # bookinpage.driver_implicitly_wait(6)
            bookinpage.test_selector_click()
            # Clicking on available room

            # Getting logs
            # p_log = bookinpage.p_log()
            # responses = [bookinpage.process_log(log) for log in p_log]
            # with open("b_logs_11.json", "a", encoding="utf-8") as f:
            #     f.write("{")
            #     f.write(json.dumps(responses)+",")
            #     f.write("}")

            ele = bookinpage.get_element(BookingLogsPage.BookingLog_DATA_TABLE_ROW_1)
            key = ele.get_attribute("data-row-key")
            print("data-key: ", key)

            sleep(2)
            bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
            sleep(5)
            bookinpage.start_selection()
            bookinpage.select_available_resource()
            # bookinpage.driver_implicitly_wait(4)

            # Getting and assigning room number to selectors
            rval = bookinpage.get_room_name()
            RoomBookingsPage.ROOM = RoomBookingsPage.ROOM.format(rval)
            RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE = RoomBookingsPage.ROOM_AFTER_BOOKING_TITLE.format(rval)
            RoomBookingsPage.MyBookings_ROOM_CHECK_DIV = RoomBookingsPage.MyBookings_ROOM_CHECK_DIV.format(rval)
            RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_BUTTONS_CHECK.format(rval)
            RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK = RoomBookingsPage.ROOM_RPAGE_STATUS_CHECK.format(rval)
            RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON = RoomBookingsPage.MyBookings_ROOM_MEETING_OPTIONS_CANCEL_BUTTON.format(rval)

            '''Booking Modal'''

            # Attendee Details
            # New Member
            NEW_CONTACT_1 = (ran_name())[0]
            NEW_CONTACT_1_EMAIL = Config.name_to_mail(NEW_CONTACT_1)
            bookinpage.new_contact_guest(
                NEW_CONTACT_1, NEW_CONTACT_1_EMAIL)
            NEW_CONTACT_2 = (ran_name())[0]
            NEW_CONTACT_2_EMAIL = Config.name_to_mail(NEW_CONTACT_2)
            bookinpage.new_contact_guest(
                NEW_CONTACT_2, NEW_CONTACT_2_EMAIL)
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

            # loader invisibilty check
            loader = bookinpage.is_visible(RoomBookingsPage.VRS_LOADER)
            print("loader: ", loader)

            # Daily repeat
            # Repeating meeting
            bookinpage.daily_repeat()

            ele2 = bookinpage.get_element(RoomBookingsPage.BookResource_Modal_START_DATE)
            ele2_text = ele2.get_attribute('title')
            print("bl_BookResource_Modal_START_DATE: ", ele2_text)
            d_formatted = Config.tr_date_format(ele2_text)
            print("bl_time2: ", d_formatted)

            # Clicking on booking button
            bookinpage.do_click(RoomBookingsPage.BookResource_Modal_BOOKING_CONFIRM_BUTTON)
            bookinpage.take_screenshot(f"RoomBooking/test_simple_booking/{TestData.CDATE[:10]}/pr{TestData.CDATE[11:]}.png")

            bookinpage.driver_get_url(TestData.BOOKING_LOGS_URL)
            sleep(8)

            print('Starting selection')
            bookinpage.resource_selection(2)

            bookinpage.verify_booking_status_filter(3)
            
            sleep(5)
            bookinpage.date_selection(2)

            # bookinpage.guest_host_selection(1, TestData.DEFAULT_HOSTNAME)

            # Getting data-key
            ele = bookinpage.get_element(BookingLogsPage.BookingLog_DATA_TABLE_ROW_1)
            key = ele.get_attribute("data-row-key")
            print("data-key: ", key)

            # Selecting tr element
            BookingLogsPage.BookingLog_BookingDetailsPage_BOOKED_I_BUTTON = BookingLogsPage.BookingLog_BookingDetailsPage_BOOKED_I_BUTTON.format(rval, d_formatted)
            BookingLogsPage.BookingLog_BOOKED_TR_PLUS_ICON = BookingLogsPage.BookingLog_BOOKED_TR_PLUS_ICON.format(rval, d_formatted)
            print("Xpath selector: ", BookingLogsPage.BookingLog_BookingDetailsPage_BOOKED_I_BUTTON)
            bookinpage.action_chain_click((By.XPATH, BookingLogsPage.BookingLog_BOOKED_TR_PLUS_ICON))
            sleep(4)
            bookinpage.action_chain_click((By.XPATH, BookingLogsPage.BookingLog_BookingDetailsPage_BOOKED_I_BUTTON))
            bookinpage.booking_details_data_verification(1)
            sleep(2)
        except Exception as e:
            print(f"Exception test_simple_booking: {e}")
            bookinpage.take_screenshot(f"RoomBooking/test_simple_booking/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")

    @pytest.mark.login
    def test_download_report(self):
        try:
            bookinpage = BookingLogsPage(self.driver)
            sleep(3)
            bookinpage.driver_get_url(TestData.BOOKING_LOGS_URL)
            sleep(8)

            # bookinpage.test_selector_click()
            # print('Starting selection')
            # bookinpage.resource_selection(2)

            # bookinpage.verify_booking_status_filter(3)

            # print("BookingLog_Data Matrix verification: Passed")

            # bookinpage.date_selection(2)
            # sleep(5)
            bookinpage.download_report()
            sleep(10)
            # # Getting data-key
            # ele = bookinpage.get_element(BookingLogsPage.BookingLog_DATA_TABLE_ROW_1)
            # key = ele.get_attribute("data-row-key")
            # print("data-key: ", key)

            # # Selecting tr element
            # BookingLogsPage.BL_BD_TR_I_BUTTON = BookingLogsPage.BL_BD_TR_I_BUTTON.format(key)
            # bookinpage.action_chain_click((By.XPATH, BookingLogsPage.BL_BD_TR_I_BUTTON))
            # sleep(2)
            # bookinpage.booking_details_data_verification()
            # sleep(5)
        except Exception as e:
            print(f"Exception test_download_report: {e}")
            bookinpage.take_screenshot(f"BookingLogs/test_download_report/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[11:]}.png")
