from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from datetime import timedelta
# import pytz

class TestData:
    
    CHROME_EXECUTABLE_PATH = "chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "C:\WebDrivers\geckodriver-v0.30.0-win64\geckodriver"

    BASE_URL = "https://ndl.veris.in/login/NewLogin"
    # BASE_URL = "http://localhost:3000/login/domain"
    DOMAIN = "ndl"
    USER_NAME = "neeraj.dhiman@veris.in"
    PASSWORD = "Passw0rd@123"
    USER_NAME_2 = "shailendra.tiranga@veris.in"
    PASSWORD_2 = "Ttpl@12345"

    LOGIN_PAGE_TITLE = "Veris | Powering Future Workplaces"

    
    def time_select_start_1():
        now = datetime.now()
        future_time = now + timedelta(minutes=15)
        current_time = future_time.strftime("%H:%M")
        print("time_select_start_1: ", current_time)
        return current_time

    def time_select_end_1():
        now = datetime.now()
        future_time = now + timedelta(minutes=30)
        future_time_1 = future_time.strftime("%H:%M")
        print("time_select_end_1: ", future_time_1)
        return future_time_1

    def time_select_end_2():
        now = datetime.now()
        future_time = now + timedelta(minutes=20)
        future_time_1 = future_time.strftime("%H:%M")
        print("time_select_end_2: ", future_time_1)
        return future_time_1
    
    def time_select_start_3():
        now = datetime.now()
        future_time = now + timedelta(minutes=25)
        current_time = future_time.strftime("%H:%M")
        print("time_select_start_3: ", current_time)
        return current_time

    def time_select_end_3():
        now = datetime.now()
        future_time = now + timedelta(minutes=45)
        future_time_1 = future_time.strftime("%H:%M")
        print("time_select_end_3: ", future_time_1)
        return future_time_1
    
    def time_overlapping_start_1():
        now = datetime.now()
        future_time = now + timedelta(minutes=25)
        current_time = future_time.strftime("%H:%M")
        print("time_overlapping_start_1: ", current_time)
        return current_time

    def time_overlapping_end_1():
        now = datetime.now()
        future_time = now + timedelta(minutes=45)
        future_time_1 = future_time.strftime("%H:%M")
        print("time_overlapping_end_1: ", future_time_1)
        return future_time_1

    def booking_date_1():
        now = datetime.now()
        future_time = now + timedelta(days=5)
        bdate = future_time.strftime("%d %b %Y")
        print("booking_date_1: ", bdate)
        return bdate

    def repeat_till_date_1():
        now = datetime.now()
        future_time = now + timedelta(days=30)
        bdate = future_time.strftime("%d %b %Y")
        print("repeat_till_date_1: ", bdate)
        return bdate

    def room_start_datetime():
        now = datetime.now()
        future_time = now + timedelta(minutes=15)
        rsdate = future_time.strftime("%d %b %Y %H:%M")
        print("rsdate: ", rsdate)
        return rsdate

    def room_end_datetime():
        now = datetime.now()
        future_time = now + timedelta(minutes=16)
        redate = future_time.strftime("%d %b %Y %H:%M")
        print("redate: ", redate)
        return redate

    def room_start_overlapping_datetime():
        now = datetime.now()
        future_time = now + timedelta(minutes=20)
        rsodate = future_time.strftime("%d %b %Y %H:%M")
        print("rsdate: ", rsodate)
        return rsodate

    def room_end_overlapping_datetime():
        now = datetime.now()
        future_time = now + timedelta(minutes=40)
        reodate = future_time.strftime("%d %b %Y %H:%M")
        print("redate: ", reodate)
        return reodate

    '''Desk Booking details'''
    DEFAULT_HOSTNAME = "Neeraj Dhiman"
    DEFAULT_HOSTEMAIL = "neeraj.dhiman@veris.in"
    HOST1_NAME = "Shail"
    HOST1_FULLNAME = "Shailendra Tiranga"
    HOST1_EMAIL = "shailendra.tiranga@veris.in"
    HOST2_NAME = "Himans"
    HOST2_FULLNAME = "Himanshi Sharma"
    HOST2_EMAIL = "himanshi.sharma@veris.in"
    BOOKING_DATE = booking_date_1()
    BOOKING_DATE1 = booking_date_1()
    TIME_START = time_select_start_1()
    TIME_END = time_select_end_1()
    TIME_END2 = time_select_end_2()
    TIME_START3 = time_select_start_3()
    TIME_END3 = time_select_end_3()
    TIME_OVERLAPPING_START = time_overlapping_start_1()
    TIME_OVERLAPPING_END = time_overlapping_end_1()
    TILL_NEXT_DAY_START_TIME = "26 Apr 2022 23:55"
    TILL_NEXT_DAY_START_TIME_1 = "26 Apr 2022 23:55"
    TILL_NEXT_DAY_END_TIME = "27 Apr 2022 01:30"
    REPEAT_TILL_DATE = f"{repeat_till_date_1()} 01:00"
    REPEAT_TILL_DATE2 = f"{repeat_till_date_1()} 23:00"
    DESK_NO_1 = None

    '''Room booking'''
    ROOM_AGENDA = "Automation testing"
    NEW_CONTACT_1 = "Rahul1"
    NEW_CONTACT_1_EMAIL = "rahul1@gmail.com"
    NEW_CONTACT_2 = "Rahul2"
    NEW_CONTACT_2_EMAIL = "rahul2@gmail.com"
    ROOM_START_DATE = room_start_datetime()
    ROOM_END_DATE = room_end_datetime()
    CONTACT_1_IS_DRAFTED_FALSE = "test veris"
    CONTACT_1_IS_MEMBER = "Johnathan Gracer"
    CONTACT_2_IS_MEMBER = "Mark Jacob"
    CONTACT_3_IS_MEMBER = "Shailendra Tiranga"
    ROOM_OVERLAPPING_TIME_START = room_start_overlapping_datetime()
    ROOM_OVERLAPPING_TIME_END = room_end_overlapping_datetime()
    ROOM_OVERLAPPING_TIME_END_2 = "27 Apr 2022 01:10"
    ROOM_OVERLAPPING_TIME_START_1 = "27 Apr 2022 01:15"
    ROOM_OVERLAPPING_TIME_END_1 = "27 Apr 2022 01:30"
    REPEAT_FREQUENCY = "1"
    WEEKLY_REPEAT_TILL_DATE = "2 May 2022"
    WEEKLY_REPEAT_TILL_DATE2 = "24 Apr 2022"

    '''Amenities'''
    AM_1 = "Dual"
    DUAL_MONITOR = "Dual Monitor"
    AM_QUANTITY = "2"


    '''Tag'''
    TAG = "Engineering Deck"
