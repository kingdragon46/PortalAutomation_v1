from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import traceback


class HealthStatusPage(BasePage):
    # Health Status
    HS_HEALTH_STATUS_MSG = 'You cannot book the desk since your health status is "Not Filled", Please fill your health status under "My Bookings"'
    HS_HEALTH_STATUS_PROMPT = (
        By.XPATH, "//*[contains(text(), 'Update Health Status')]")
    HS_UPDATE_HEALTH_STATUS_BUTTON = (
        By.XPATH, "//*[text()='Health status']/../following-sibling::*//button")
    HS_WS_UPDATE_HEALTH_STATUS_BUTTON = (
        By.XPATH, "//*[contains(@class,'work-status-health-declaration')]//button")
    HS_FULLY_VACCINATED = (
        By.XPATH, "//*[contains(text(), 'Fully Vaccinated')]/preceding-sibling::*/child::*")
    HS_HEALTH_CONDITION_NONE = (
        By.XPATH, "//*[contains(text(), 'None')]/preceding-sibling::*/child::*")
    HS_PROVIDING_CARE_NO = (
        By.XPATH, "//*[contains(text(), 'If you are providing care to a confirmed /suspect/probable case')]/parent::*/following-sibling::*/child::div[2]/child::div[2]/child::div/child::div/child::div/child::*")
    HS_CONTACT_14DAYS_NO = (
        By.XPATH, "//*[contains(text(), 'If you have come in contact with any COVID-19 positive case in the last 14 days')]/parent::*/following-sibling::*/child::div[2]/child::div[2]/child::div/child::div/child::div/child::*")
    HS_OFFICE_TO_VISIT_DROPDOWN = (By.XPATH, "//*[@id='other_5014']/div")
    HS_OFFICE_TO_VISIT_SELECT = (
        By.XPATH, "//*[contains(text(), 'Digicred HQ-New York')]")
    HS_PARKING_DROPDOWN = (By.XPATH, "//*[@id='other_5015']/div")
    HS_PARKING_SELECT = (By.XPATH, "//*[contains(text(), '2 Wheeler')]")
    HS_CONFIRM_DECLARATION = (
        By.XPATH, "//*[contains(text(), 'Confirm Declaration')]")
    HS_Q1_1_OPTIONS = "(//*[@class='workflow-health']//*[@class='meeting-room-padding-cd0a98b0f8d88ac043f27d7a806873ed'][1]//*[@class='next_btn'])"
    HS_Q2_1_OPTIONS = "(//*[@class='workflow-health']//*[@class='meeting-room-padding-cd0a98b0f8d88ac043f27d7a806873ed'][2]//*[@class='next_btn'])"
    HS_Q3_1_OPTIONS = "(//*[@class='workflow-health']//*[@class='meeting-room-padding-cd0a98b0f8d88ac043f27d7a806873ed'][3]//*[@class='next_btn'])"
    HS_Q4_1_OPTIONS = "(//*[@class='workflow-health']//*[@class='meeting-room-padding-cd0a98b0f8d88ac043f27d7a806873ed'][4]//*[@class='next_btn'])"
    
    HS_Q1_OPTIONS = "(//*[@class='work-status-padding-cd0a98b0f8d88ac043f27d7a806873ed'][1]//*[@class='next_btn'])"
    HS_Q2_OPTIONS = "(//*[@class='work-status-padding-cd0a98b0f8d88ac043f27d7a806873ed'][2]//*[@class='next_btn'])"
    HS_Q3_OPTIONS = "(//*[@class='work-status-padding-cd0a98b0f8d88ac043f27d7a806873ed'][3]//*[@class='next_btn'])"
    HS_Q4_OPTIONS = "(//*[@class='work-status-padding-cd0a98b0f8d88ac043f27d7a806873ed'][4]//*[@class='next_btn'])"
    HS_ERROR_MSG = (By.XPATH, "//*[@class='ant-message-custom-content ant-message-error']//span[text()='Please fill all required data !']")
    HS_Refresh_Div = (By.XPATH, "(//*[@src='/apps/meeting-room/static/media/button-refresh-arrow.ed68bee1.svg'])")
    HS_Refresh_Div_2 = (By.XPATH, "(//*[@src='/apps/work-status/static/media/button-refresh-arrow.ed68bee1.svg'])[2]")


    # <<=========================================================== Functions ======================================================>>

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for Health status Page"""

    
    def negative_test_health_status(self, test_type=None):
        try:
            val = self.is_visible(self.HS_WS_UPDATE_HEALTH_STATUS_BUTTON)
            print("val: ", val)
            if val == True:
                self.action_chain_click(self.HS_WS_UPDATE_HEALTH_STATUS_BUTTON)
                sleep(5)
                if test_type == 1 or None:
                    pass
                elif test_type == 2:
                    print("Case 2")
                    self.action_chain_click((By.XPATH, f"{self.HS_Q1_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q2_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q3_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q4_OPTIONS}[1]"))
                    sleep(2)
                elif test_type == 3:
                    print("Case 3")
                    self.action_chain_click((By.XPATH, f"{self.HS_Q1_OPTIONS}[2]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q2_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q3_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q4_OPTIONS}[1]"))
                    sleep(2)
                elif test_type == 4:
                    print("Case 4")
                    url = self.current_url()
                    if 'ndl' in url:
                        print("url: ", url)
                        self.action_chain_click((By.XPATH, f"{self.HS_Q1_OPTIONS}[4]"))
                        sleep(2)
                        self.action_chain_click((By.XPATH, f"{self.HS_Q4_OPTIONS}[1]"))
                    else:
                        self.action_chain_click((By.XPATH, f"{self.HS_Q1_OPTIONS}[1]"))
                        sleep(2)
                        self.action_chain_click((By.XPATH, f"{self.HS_Q4_OPTIONS}[3]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q2_OPTIONS}[2]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q3_OPTIONS}[1]"))
                    sleep(2)
                elif test_type == 5:
                    print("Case 5")
                    self.action_chain_click((By.XPATH, f"{self.HS_Q1_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q2_OPTIONS}[2]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q3_OPTIONS}[2]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q4_OPTIONS}[2]"))
                    sleep(2)
                elif test_type == 6:
                    print("Case 6")
                    self.action_chain_click((By.XPATH, f"{self.HS_Q1_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q2_OPTIONS}[2]"))
                    sleep(2)
                elif test_type == 7:
                    print("Case 7")
                    self.action_chain_click((By.XPATH, f"{self.HS_Q3_OPTIONS}[2]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q4_OPTIONS}[2]"))
                    sleep(2)
                elif test_type == 8:
                    print("Case 8")
                    self.action_chain_click((By.XPATH, f"{self.HS_Q1_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q4_OPTIONS}[2]"))
                elif test_type == 9:
                    print("Case 9")
                    self.action_chain_click((By.XPATH, f"{self.HS_Q2_OPTIONS}[1]"))
                    sleep(2)
                    self.action_chain_click((By.XPATH, f"{self.HS_Q3_OPTIONS}[2]"))
                    sleep(2)
                cd_visible = self.is_visible(self.HS_CONFIRM_DECLARATION)
                print("confirm btn: ", cd_visible)
                sleep(2)
                self.action_chain_click(self.HS_CONFIRM_DECLARATION)
                sleep(2)
            else:
                pass
        except Exception as e:
            print(f"update_health_status exception: {e}\n{traceback.format_exc()}")
            self.take_screenshot(f"deskBooking/update_health_status/Ex_{TestData.CDATE[:10]}/{TestData.CDATE[1:]}.png")

            