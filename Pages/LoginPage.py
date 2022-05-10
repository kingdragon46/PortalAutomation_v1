from Pages.BasePage import BasePage
from Pages.deskBookingsPage import deskBookingsPage
from Pages.RoomBookingPage import RoomBookingsPage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(BasePage):

    '''By locators - OR'''
    USERNAME = (By.XPATH,"//*[@id='login']/div/div/div[2]/div[1]/div[2]/form/div[2]/div[2]/div/div/input")
    PASSWORD = (By.XPATH,"//*[@id='login']/div/div/div[2]/div[1]/div[2]/form/div[3]/div[2]/div/div/input")
    LOGIN_BUTTON = (By.XPATH,"//*[@id='login']/div/div/div[2]/div[1]/div[2]/form/div[4]/div/div/div/button")
    FORGOT_PASSWORD = (By.XPATH,"//*[@id='login']/div/div/div[2]/div[1]/div[2]/form/div[5]")

    '''Domain select'''
    ENTER_DOMAIN = (By.XPATH, "//*[@id='login']/div/div/div[2]/div[1]/div/div[2]/div[2]/input")
    CONTINUE = (By.XPATH, "//*[contains(text(), 'Continue')]")

    # <<=========================================== Functions ==============================================================>>

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions"""

    """this is used to login to website"""
    def do_login(self, username, password):
        self.do_send_keys(self.ENTER_DOMAIN, TestData.DOMAIN)
        self.do_click(self.CONTINUE)
        sleep(10)
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        sleep(10)
        return deskBookingsPage(self.driver)
    
    def do_rlogin(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        sleep(10)
        return RoomBookingsPage(self.driver)