from dateutil.relativedelta import relativedelta
import datetime

start_date = datetime.date(1901,1,1)
end_date = datetime.date(2000,12,31)

count = 0
while start_date<=end_date:
    if start_date.weekday() == 6:
        count += 1
    start_date += relativedelta(months=+1)

print(count)
