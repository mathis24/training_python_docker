import time
import datetime
import pytz

# #########################
# Global vars

TIMEZONE = "Asia/Tokyo"
WAITING_TIME = 60           # in seconds

# #########################
# Function

def get_time_in_timezone(tzname:str) -> str:
    tz = pytz.timezone(tzname) 
    datetime_in_tz = datetime.datetime.now(tz)
    time_in_tz = datetime_in_tz.strftime("%H:%M:%S")
    
    return time_in_tz

# #########################
# Main

if __name__ == "__main__":
    # print(pytz.all_timezones) # list of all timezones
    
    while True:
        cur_time = get_time_in_timezone(TIMEZONE)
        print(f"The current time in {TIMEZONE} is:", cur_time)
        time.sleep(60)