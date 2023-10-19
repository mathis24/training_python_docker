from datetime import datetime, timedelta
import time

def datetime_to_string(dt:datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    timestamp = time.time()     # nb seconds since 1/1/1970 (epoch) in UTC
    print(f"current timestamp: {timestamp}")
    
    # convert to datetime
    dt_utc = datetime.utcfromtimestamp(timestamp)
    dt_local = datetime.fromtimestamp(timestamp)
    print(f"year: {dt_utc.year} month: {dt_utc.month} day: {dt_utc.day}")
    print(f"datetime (utc): {dt_utc}\n")
    
    # future date
    dt_utc2 = dt_utc + timedelta(hours=20)
    
    # datetime to string
    sdt = datetime_to_string(dt_utc)
    sdt2 = datetime_to_string(dt_utc2)
    print("Now (utc): ", sdt)
    print("In 20 hours (utc): ", sdt2)
    print("Now (local time): ", datetime_to_string(dt_local))