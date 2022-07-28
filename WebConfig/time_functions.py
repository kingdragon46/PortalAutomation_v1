from datetime import datetime, timedelta
from pytz import timezone
from random_name_generator import ran_name
from random import randint
import re

class WebConfigFunctions:
    
    def time_select(m):
        now = datetime.now()
        future_time = now + timedelta(minutes=m)
        current_time = future_time.strftime("%H:%M")
        print("time_select_start_1: ", current_time)
        return current_time

    def booking_date(d=None):
        now = datetime.now()
        if d is not None:
            future_time = now + timedelta(days=d)
            bdate = future_time.strftime("%d %b %Y")
        else:
            bdate = now.strftime("%d %b %Y")
        print("booking_date: ", bdate)
        return bdate

    def repeat_till_date(dys):
        now = datetime.now()
        future_time = now + timedelta(days=dys)
        bdate = future_time.strftime("%d %b %Y")
        print("repeat_till_date: ", bdate)
        return bdate

    def timetest():
        format = "%Y-%m-%d %H:%M:%S %Z%z"
        # Current time in UTC
        now_utc = datetime.now(timezone('UTC'))
        print(now_utc.strftime(format))
        # Convert to Asia/Kolkata time zone
        now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
        print(now_asia.strftime(format))
        print(type(now_asia.strftime(format)))

    def repeat_till_date2(dys=None):
        now = datetime.now()
        if dys is not None:
            future_time = now + timedelta(days=dys)
        else:
            future_time = now
        bdate = future_time.strftime("%Y-%m-%d")
        print("repeat_till_date2: ", bdate)
        return bdate

    def cal_date_format(future_time):
        bdate = datetime.strptime(future_time, '%d %b %Y').strftime("%Y-%m-%d")
        print("cal_date_format: ", bdate)
        return bdate

    def tr_date_format(future_time):
        bdate = datetime.strptime(future_time, '%d %b %Y %H:%M').strftime("%b %d, %Y %H:%M")
        print("tr_date_format: ", bdate)
        return bdate

    def till_next_day_date(dys=None):
        now = datetime.now()
        if dys is not None:
            future_time = now + timedelta(days=dys)
            bdate = future_time.strftime("%d %b %y")
        else:
            bdate = now.strftime("%d %b %y")
        print("till_next_day_date: ", bdate)
        return bdate

    def bulk_invite_dateFormat(dys=None, min=None):
        now = datetime.now()
        if dys is not None:
            future_time = now + timedelta(days=dys)
            bdate = future_time.strftime("%d/%m/%Y %H:%M %p")
        if min is not None:
            future_time = now + timedelta(minutes=min)
            bdate = future_time.strftime("%d/%m/%Y %H:%M %p")
        else:
            bdate = now.strftime("%d/%m/%Y %H:%M %p")
        print("bulk_invite_dateFormat: ", bdate)
        return bdate

    def room_datetime(d,m):
        now = datetime.now()
        future_time = now + timedelta(days=d, minutes=m)
        rsdate = future_time.strftime("%d %b %Y %H:%M")
        print("room_datetime: ", rsdate)
        return rsdate

    def current_datetime():
        now = datetime.utcnow()
        loc_time = now.strftime("%Y_%m_%dT%H.%M.%S")
        print("current_datetime: ", loc_time)
        return loc_time

    def room_start_overlapping_datetime():
        now = datetime.now()
        future_time = now + timedelta(minutes=20)
        rsodate = future_time.strftime("%d %b %Y %H:%M")
        print("room_start_overlapping_datetime: ", rsodate)
        return rsodate

    def room_end_overlapping_datetime():
        now = datetime.now()
        future_time = now + timedelta(minutes=40)
        reodate = future_time.strftime("%d %b %Y %H:%M")
        print("room_end_overlapping_datetime: ", reodate)
        return reodate

    def name_to_mail(a):
        b = a.replace(" ", ".").lower()
        c = f'{b}@example.com'
        return c


    def random_phn():
        b = randint(10000000, 99999999)
        return f"+919{b}"
        
    
    def validate_email(email):
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")
        if not EMAIL_REGEX.match(email):
            return False
        return True