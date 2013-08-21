#~ from datetime import datetime
#~ from time import time
#~ import datetime


#~  8.1.1. Available Types
#~ print datetime 
#~ print datetime.date
#~ from datetime import date
#~ print date.today()

#~ print datetime.time

#~ print datetime.tzinfo

#~ print datetime.today

#~ print datetime.time()
#~ print datetime.datetime
#~ print datetime.datetime(2012, 11, 15)
#~ print datetime.datetime.today()
#~ while datetime.datetime.today() != 1:
	#~ print datetime.datetime.today()

#~ from datetime import timedelta
#~ year = timedelta(days=365)
#~ another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)  # adds up to 365 days
#~ print year.total_seconds()

#~ year == another_year

#~ ten_years = 10 * year
#~ print ten_years, ten_years.days // 365

#~ nine_years = ten_years - year
#~ print nine_years, nine_years.days // 365

#~ three_years = nine_years // 3;
#~ print three_years, three_years.days // 365

#~ print abs(three_years - ten_years) == 2 * three_years + year

import time as t

print t.accept2dyear
print t.altzone 
print t.asctime() 
print t.clock() 
print t.ctime()
print t.daylight
print t.gmtime().tm_year
print t.localtime()
print t.mktime(t.localtime())
print t.sleep(2) 
print t.strftime("%a, %d %b %Y %H:%M:%S +0000") 
print t.strptime("31 May 13", "%d %b %y")
print t.struct_time
print t.time()
print t.timezone / 3600 
print t.tzname

