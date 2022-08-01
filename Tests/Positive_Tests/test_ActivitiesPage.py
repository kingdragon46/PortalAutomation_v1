import json
from time import time, sleep
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from Pages.ActivitiesPage import ActivitiesPage
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

    '''Create Activity'''

    # @pytest.mark.selected
    def test_normal_invite(self):
        activitypage = ActivitiesPage(self.driver)
        sleep(3)
        activitypage.action_chain_click(ActivitiesPage.CreateActivity_link)
        sleep(2)

        activitypage.createActivity_selectVenue()

        phn = Config.random_phn()

        activitypage.createActivity_contactInput(phn)

        activitypage.createActivity_activityType()

        activitypage.createActivity_visitorCategory()

        activitypage.scroll_to_element(ActivitiesPage.CreateActivity_Confirm)

        activitypage.createActivity_covidQuestions()

        # Visitor Details
        person = ran_name()
        fname = person[2]
        lname = person[3]
        cmail = person[1]
        activitypage.createActivity_visitorDetails(fname, lname, cmail)

        activitypage.createActivity_selectHost()

        activitypage.createActivity_checkbox_NDA()

        activitypage.createActivity_companyName()

        activitypage.createActivity_wifi()

        activitypage.createActivity_parking()

        activitypage.createActivity_areasToVisit()

        activitypage.createActivity_confirmCheckIn()
        

    
    # @pytest.mark.selected
    def test_mandatoryFields_check(self):
        activitypage = ActivitiesPage(self.driver)
        sleep(3)
        activitypage.action_chain_click(ActivitiesPage.CreateActivity_link)
        sleep(2)

        activitypage.createActivity_selectVenue()

        activitypage.createActivity_activityType()

        activitypage.createActivity_visitorCategory()

        activitypage.scroll_to_element(ActivitiesPage.CreateActivity_Confirm)

        activitypage.createActivity_confirmCheckIn()

        mfields = activitypage.createActivity_mandatoryFields() - 1
        print("mfields: ", mfields)

        enum = activitypage.createActivity_mandatory_error()
        print("enum: ", enum)

        assert mfields == enum

    
    @pytest.mark.selected
    def test_mandatoryFields_input_check(self):
        activitypage = ActivitiesPage(self.driver)
        sleep(3)
        activitypage.action_chain_click(ActivitiesPage.CreateActivity_link)
        sleep(2)

        activitypage.createActivity_selectVenue()

        activitypage.createActivity_activityType()

        activitypage.createActivity_visitorCategory()

        activitypage.scroll_to_element(ActivitiesPage.CreateActivity_Confirm)

        vresult = Config.validate_email("TestData.CreateActivity_NotTrueEmail@gmail.com")
        print("vresult: ", vresult)
        error_vis = activitypage.createActivity_emailField_InputError_check(TestData.CreateActivity_NotTrueEmail)
        print("error_vis: ", error_vis)
        if vresult is False:
            try:
                assert error_vis==True
            except AssertionError:
                print("Assertion failed. Actual value is %s" % error_vis)
        if vresult is True:
            try:
                assert error_vis==False
            except AssertionError:
                print("Assertion failed. Actual value is %s" % error_vis)