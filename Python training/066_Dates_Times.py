# Dates and Time using our system

import datetime

date = datetime.date(year=2025, month=1, day=30) # American format
today = datetime.date.today() # Present day

time = datetime.time(hour=12, minute=30, second=0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S, %m-%d-%Y ") # hours format
# Capital letter or small letter have impact on output

target_datetime = datetime.datetime(year=2030, month=1, day=30, hour=12, minute=30, second=1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed.")
else:
    print("Target date has not passed.")

print(date)
print(today)
print(time)
print(now)