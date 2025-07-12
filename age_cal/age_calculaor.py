import time
from calendar import isleap

def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

def month_days(year,month):
    if month in [1,3,5,7,8,10,13]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        return 29 if isleap(year) else 28
    else:
        return "Invalid month"
#name = input("input your name: ")
age = input("input your Date of birth: ")
Local_time=time.localtime(time.time())

try:
    year, month,day=map(int,age.split("-"))
    print(f"Year: {year}")
    print(f"Leap Year: {judge_leap_year(year)}")
    print(f"Days in month {month}: {month_days(year, month)}")

except ValueError:
    print("Invalid format. Please enter DOB in YYYY-MM-DD format.")
year = int(age)
month = year * 12 + Local_time.tm_mon
day = 0

begin_year = int(Local_time.tm_year) - year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if judge_leap_year(y):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(Local_time.tm_year)
for m in range(1, Local_time.tm_mon):
    day = day + month_days(m, leap_year)

day = day + Local_time.tm_mday

print("%d months or %d days" % (month, day))