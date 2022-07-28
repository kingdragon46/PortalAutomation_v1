import json
from time import time, sleep
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from Pages.InvitesPage import InvitesPage
from Pages.LoginPage import LoginPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest

import traceback
import sys

from random_name_generator import ran_name, ran_name_2
from WebConfig.time_functions import WebConfigFunctions as Config


class Test_InvitesPage(BaseTest):

    # Login
    @pytest.mark.selected
    @pytest.mark.singleInvite
    @pytest.mark.invitesList
    @pytest.mark.bulkInvite
    @pytest.mark.login
    def test_login_booking(self):
        self.loginPage = LoginPage(self.driver)
        loginPage = self.loginPage.do_rlogin(
            TestData.USER_NAME, TestData.PASSWORD)

    '''Single Visitor'''

    @pytest.mark.singleInvite
    def test_normal_invite(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)

        invitepage.singleInvite_StartsAt()

        invitepage.singleInvite_EndsAt()

        invitepage.singleInvite_hostName()

        invitepage.singleInvite_Agenda()

        # FirstName
        person = ran_name()
        fname = person[2]
        invitepage.singleInvite_firstName(fname)

        # lastName
        lname = person[3]
        invitepage.singleInvite_lastName(lname)
        # Email
        cmail = person[1]
        invitepage.singleInvite_Contact(cmail)

        invitepage.singleInvite_visitorCategory()

        invitepage.singleInvite_escortName()

        invitepage.singleInvite_sendInvite()

    @pytest.mark.singleInvite
    def test_mandatory_fields_error(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)

        invitepage.singleInvite_visitorCategory()

        invitepage.singleInvite_sendInvite()

        No_of_mandatory_fields = invitepage.singleInvite_get_no_of_mandate_fields() - \
            TestData.MandatoryFields_to_skip

        No_of_error = invitepage.singleInvite_mandatory_error_check()

        assert No_of_mandatory_fields == No_of_error

    @pytest.mark.singleInvite
    def test_mandatory_pastDated_invite(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)

        invitepage.singleInvite_StartsAt_time()

        invitepage.action_chain_click(InvitesPage.InviteDetails_heading)

        count_error = invitepage.singleInvite_pastDate_error_check()
        assert count_error == 1

    @pytest.mark.singleInvite
    def test_namefieldInput_datatype(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)

        fname = "123"
        lname = "456"

        invitepage.singleInvite_firstName(fname)
        invitepage.singleInvite_lastName(lname)

        error = invitepage.singleInvite_datatype_error_check()

        assert error == 2

    '''Invites List'''

    @pytest.mark.invitesList
    def test_invitesList_selectVenue(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)
        invitepage.action_chain_click(InvitesPage.InvitesList_link)

        invitepage.invitesList_venue_select()

        invitepage.invitesList_verify_TableData()
        sleep(2)

    @pytest.mark.invitesList
    def test_invitesList_selectDates(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)
        invitepage.action_chain_click(InvitesPage.InvitesList_link)

        invitepage.invitesList_venue_select()

        invitepage.invitesList_StartsAt(-5)

        invitepage.invitesList_EndsAt()

        invitepage.invitesList_verify_TableData()
        sleep(2)

    @pytest.mark.invitesList
    def test_invitesList_selectHost(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)
        invitepage.action_chain_click(InvitesPage.InvitesList_link)

        invitepage.invitesList_venue_select()

        invitepage.invitesList_StartsAt(-5)

        invitepage.invitesList_EndsAt()

        invitepage.invitesList_select_host_dropdown()
        sleep(2)

        invitepage.invitesList_verify_TableData(1)
        sleep(2)

    @pytest.mark.selected
    @pytest.mark.invitesList
    def test_invitesList_selectGuest(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)
        invitepage.action_chain_click(InvitesPage.InvitesList_link)

        invitepage.invitesList_venue_select()

        invitepage.invitesList_StartsAt(-5)

        invitepage.invitesList_EndsAt()

        invitepage.invitesList_select_guest_dropdown()
        sleep(2)

        invitepage.invitesList_verify_TableData(1, 1)
        sleep(2)

    @pytest.mark.invitesList
    def test_invitesList_selectStatus(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)
        invitepage.action_chain_click(InvitesPage.InvitesList_link)

        invitepage.invitesList_venue_select()

        invitepage.invitesList_StartsAt(-5)

        invitepage.invitesList_EndsAt()

        invitepage.action_chain_click(
            InvitesPage.InvitesList_VisitorInvites_header)

        invitepage.action_chain_click(InvitesPage.InvitesList_MoreFilters)

        invitepage.invitesList_currentStatus_selector()

        invitepage.invitesList_verify_TableData()
        sleep(2)

    '''Bulk Invites'''

    @pytest.mark.bulkInvite
    def test_bulkInvite_add_member(self):
        invitepage = InvitesPage(self.driver)
        sleep(3)
        invitepage.action_chain_click(InvitesPage.Invites_Link)
        sleep(2)
        invitepage.action_chain_click(InvitesPage.MultipleVisitors_link)
        sleep(3)
        invitepage.bulkInvite_visitor_category_select()

        invitepage.bulkInvite_add_rows(TestData.BulkInvite_Rows)

        for i in range(TestData.BulkInvite_Rows):
            print("i: ", i)
        # Table Data
            person = ran_name()
            fname = person[2]
            lname = person[3]
            cmail = person[1]
            sdate = Config.bulk_invite_dateFormat(i, i+5)
            edate = Config.bulk_invite_dateFormat(i, i+15)
            invitepage.bulkInvite_add_data_to_table(fname, lname, cmail, sdate, edate, TestData.Single_invite_agenda, i)
            # invitepage.scroll_horizontally_left(InvitesPage.BulkInvite_TableDiv)
            
        sleep(3)
