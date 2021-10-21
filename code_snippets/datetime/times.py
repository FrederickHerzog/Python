from time import localtime, time, ctime, sleep
from datetime import date, timezone, datetime
from datetime import timedelta


#Converts seconds to datetime
l = localtime(1634846971.8821511)
print(l.tm_year)
print(l.tm_mon)
print(l.tm_mday)
print(l.tm_yday)
print()
print(l)
print("-------------------------")

#Get todays date
today = date.today()
print(today)
print("------------------------")
now = datetime.now()
print(now)
print("--------------------------")

#strftime
date_str = now.strftime("%m-%d-%Y")
print(date_str)
print("-------------------------")
#TimeWithdatetime
tt = now.strftime("%H:%M:%S")
print(tt)
print()
#Time
seconds = time()
print("Seconds since epoch =", seconds)	
print("``````````````````````````````````")

# seconds passed since epoch
local_time = ctime(seconds)
print("Local time:", local_time)	


#TDelta
curr = datetime.now()
x_date_time = datetime(year=2021, month=10, day=21, hour=15, minute=30)
print("Today {}".format(curr))
print("New Date {}".format(x_date_time))
timedel = curr - x_date_time
print(" Diff - {}".format(timedel))
print('Given Date:', curr)
# add 4 weeks in given date
new_date = curr + timedelta(weeks=10)
print('Future Date:', new_date)
#Date regex 

'''

YYYY-MM-DD

/^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/

'''

'''
YYYYMMDD

/^\d{4}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$/

'''

'''
YYYY/MM/DD

/^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$/

'''