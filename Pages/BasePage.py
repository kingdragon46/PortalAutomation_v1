import json
import pprint
import requests
import urllib3
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

"""This is the parent of all pages"""
"""It contains all the generic methods and utilities for all pages"""

class BasePage:
    time_delay = 40
    # web_drive_cls = WebDriverWait(self.driver, time_delay)

    def __init__(self,driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, self.time_delay).until(EC.element_to_be_clickable(by_locator)).click()

    def is_alert(self):
        try:
            WebDriverWait(self.driver, self.time_delay).until(EC.alert_is_present())
        except Exception as e:
            print(f"is_alert exception: {e}")

    def do_click_by_script(self, by_locator):
        btn = self.driver.find_element(by_locator)
        self.driver.execute_script("arguments[0].click();", btn)

    def do_click_by_xpath(self, by_locator):
        WebDriverWait(self.driver, self.time_delay).until(EC.element_to_be_clickable((By.XPATH, by_locator))).click()

    def do_click_by_index(self, by_locator, index):
        elem = WebDriverWait(self.driver, self.time_delay).until(EC.presence_of_all_elements_located((By.XPATH, by_locator)))
        elem[index].click()

    def do_send_keys(self, by_locator, keys):
        WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator)).send_keys(keys)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element_text_by_xpath(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_enabled_by_index(self, by_locator, index):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_all_elements_located(by_locator))
        return bool(element[index])

    def is_invisible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 40).until(EC.invisibility_of_element_located(by_locator))
            return bool(element)
        except Exception as e:
            print(f"is_invisible exception: {e}")

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except Exception as e:
            print(f"is_visible exception: {e}")

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, self.time_delay).until(EC.title_is(title))
        return self.driver.title

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_elements(self, by_locator):
        elements = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_all_elements_located(by_locator))
        return elements

    def get_present_element(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.presence_of_all_elements_located(by_locator))
        return element.text
    
    def host_selection(self, by_locator, elkeys, ex=None):
        try:
            element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click()
            actions.send_keys(elkeys)
            sleep(2)
            actions.perform()
            sleep(4)
            select_host = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
            actions.move_to_element(select_host)
            if ex is not None:
                for i in range(0, ex):
                    actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.RETURN)
            actions.perform()
            sleep(2)
        except Exception as e:
            print("host_selection: ", e)
    
    def chain_selection_send_keys_click(self, by_locator, elkeys):
        try:
            element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click()
            actions.send_keys(elkeys)
            actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.ENTER)
            sleep(2)
            actions.perform()
            sleep(2)
        except Exception as e:
            print("host_selection: ", e)

    def date_selection_chain(self, by_locator, dkeys, bstrokes=2):
        bdate = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(bdate)
        actions.click()
        sleep(2)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        for i in range(0, bstrokes):
            actions.send_keys(Keys.BACKSPACE)
        actions.send_keys(dkeys)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(5)
        
    def time_selection(self, bstart, bstart_input, bstrokes=1):
        start_time = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(bstart))
        actions = ActionChains(self.driver)
        actions.move_to_element(start_time)
        actions.click()
        sleep(2)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        for i in range(0, bstrokes):
            actions.send_keys(Keys.BACKSPACE)
        actions.send_keys(bstart_input)
        actions.send_keys(Keys.ENTER)
        sleep(2)
        actions.perform()
        sleep(2)

    def action_chain_click(self, by_locator):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        print("Element: ", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        sleep(1)
        actions.click(element)
        actions.perform()
        sleep(1)

    def action_chain_sendkeys_1(self, by_locator, elkeys):
        element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
        print("Element: ", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        sleep(2)
        actions.send_keys(elkeys)
        actions.perform()
        sleep(2)

    def scroll_to_element(self, by_locator):
        a = None
        try:
            element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located(by_locator))
            print("element present")
            self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", element)
            print("moved to element")
            a = 1
            pass
        except:
            print("1st failed")
        if a == None:
            try:
                element = WebDriverWait(self.driver, self.time_delay).until(EC.presence_of_element_located(by_locator))
                self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", element)
                pass
            except:
                print("2nd failed")

    def scroll_to_element_by_xpath(self, by_locator):
        a = None
        try:
            element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
            print("element present")
            self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", element)
            print("moved to element")
            a = 1
            pass
        except:
            print("1st failed")
        if a == None:
            try:
                element = WebDriverWait(self.driver, self.time_delay).until(EC.presence_of_element_located((By.XPATH, by_locator)))
                self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", element)
                pass
            except:
                print("2nd failed")

    def scroll_to_element_to_mid_by_xpath(self, by_locator):
        a = None
        try:
            element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
            print("element present")
            self.driver.execute_script("var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);var elementTop = arguments[0].getBoundingClientRect().top;window.scrollBy(0, elementTop-(viewPortHeight/2));", element)
            print("moved to element")
            a = 1
            pass
        except:
            print("1st failed")
        if a == None:
            try:
                element = WebDriverWait(self.driver, self.time_delay).until(EC.presence_of_element_located((By.XPATH, by_locator)))
                self.driver.execute_script("var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);var elementTop = arguments[0].getBoundingClientRect().top;window.scrollBy(0, elementTop-(viewPortHeight/2));", element)
                pass
            except:
                print("2nd failed")

    def scroll_to_element_by_index(self, by_locator, index):
        a = None
        try:
            element = WebDriverWait(self.driver, self.time_delay).until(EC.visibility_of_all_elements_located((By.XPATH, by_locator)))
            print("element present", element)
            self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", element[index])
            print("moved to element")
            a = 1
            pass
        except:
            print("1st failed")
        if a == None:
            try:
                element = WebDriverWait(self.driver, self.time_delay).until(EC.presence_of_all_elements_located((By.XPATH, by_locator)))
                self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", element[index])
                pass
            except:
                print("2nd failed")

    def quit_driver(self):
        self.driver.quit()

    def print_browser_logs(self):
        request_log = self.driver.get_log("performance")
        # try:
        #     for entry in request_log:
        #         print("in process_browser for loop")
        #         log = json.loads(entry["message"])["message"]
        #         url = "https://ndl.veris.in/api/v4/organization/56/resources/analytics/?date_from=2022-04-07T10:52:20.249Z&date_to=2022-04-07T16:52:20.250Z&resource_id=6871"
        #         if (
        #             url in log["params"]["headers"]["url"]
        #             # or "Network.request" in log["method"]
        #             # or "Network.webSocket" in log["method"]
        #         ):
        #             yield log

        #             content = self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]['requestId']})
        #             print("content: ", content)
        #             break
        # except Exception as e:
        #     print("logging error: ", e)
        events = process_browser_logs_for_network_events(request_log)
        with open("log_entries.txt", "wt") as out:
            for event in events:
                pprint.pprint(event, stream=out)

    def driver_close(self):
        self.driver.close()

    def driver_implicitly_wait(self, wtime):
        self.driver.implicitly_wait(wtime)

    def driver_get_url(self, url):
        self.driver.get(url)

    def take_screenshot(self, name):
        # sleep()
        try:
            os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
            # self.driver.get_screenshot_as_file(os.path.join("screenshot", name))
            self.driver.save_screenshot(os.path.join("screenshot", name))
        except Exception as e:
            print("Screenshot exception: ", e)

def process_browser_logs_for_network_events(logs):
    print("in process_browser")
    for entry in logs:
        print("in process_browser for loop")
        log = json.loads(entry["message"])["message"]

        url = "https://ndl.veris.in/api/v4/organization/56/resources/analytics/?date_from=2022-04-07T10:52:20.249Z&date_to=2022-04-07T16:52:20.250Z&resource_id=6871"
        if (
            url in log["params"]["headers"]["url"]
            # or "Network.request" in log["method"]
            # or "Network.webSocket" in log["method"]
        ):
            yield log