import time as t

year = str(t.gmtime().tm_year)
month = str(t.gmtime().tm_mon)
day = str(t.gmtime().tm_mday)
date_str = year+"/"+month+"/"+day
hour = str(t.gmtime().tm_hour)
min = str(t.gmtime().tm_min)
sec = str(t.gmtime().tm_sec)
time_str = hour+":"+min+":"+sec
print "Date Time now = %s" % date_str + " " + time_str

import ephem
d = ephem.Date(date_str + " " + time_str)
print "Ephem Date Time now = %s" % d
#~ print "Ephem Seconds now:", d.tuple()[5]
print "Ephem Julian Date now = %f" % ephem.julian_date()
print "Delta t now = %f" % ephem.delta_t()
gm = ephem.Observer()
gm.lon = '0.0'
print "GA Sidereal Time now = %s" % gm.sidereal_time()
print "%f" % (gm.sidereal_time() * 180.0 / ephem.pi)
here = ephem.Observer()
here.lon = '-88.7431'
print "LA Sidereal Time now = %s" % here.sidereal_time()
print "%f" % (here.sidereal_time() * 180.0 / ephem.pi)

here.lat = '41.9475'
here.elevation = 278

sid_time_dif = (gm.sidereal_time() - here.sidereal_time()) * 180.0 / ephem.pi
print sid_time_dif / 15.0
here.compute_pressure()
print here.pressure
s = ephem.Sun()
mu = ephem.Mercury()
v = ephem.Venus()
m = ephem.Mars()
j = ephem.Jupiter()
sat = ephem.Saturn()
u = ephem.Uranus()
n = ephem.Neptune()
p = ephem.Pluto()
s.compute(here)
mu.compute(here)
v.compute(here)
m.compute(here)
j.compute(here)
sat.compute(here)
u.compute(here)
n.compute(here)
p.compute(here)
print "Sun now ", "RA = %s" % s.ra, "Dec = %s" % s.dec, "Alt = %s" % s.alt,  "Az = %s" % s.az
print ephem.constellation(s)
print "Mercury now ", "RA = %s" % mu.ra, "Dec = %s" % mu.dec, "Alt = %s" % mu.alt,  "Az = %s" % mu.az
print ephem.constellation(mu)
print "Venus now ", "RA = %s" % v.ra, "Dec = %s" % v.dec, "Alt = %s" % v.alt,  "Az = %s" % v.az
print ephem.constellation(v)
print "Mars now ", "RA = %s" % m.ra, "Dec = %s" % m.dec, "Alt = %s" % m.alt,  "Az = %s" % m.az
print ephem.constellation(m)
print "Jupiter now ", "RA = %s" % j.ra, "Dec = %s" % j.dec, "Alt = %s" % j.alt,  "Az = %s" % j.az
print ephem.constellation(j)
print "Saturn now ", "RA = %s" % sat.ra, "Dec = %s" % sat.dec, "Alt = %s" % sat.alt,  "Az = %s" % sat.az
print ephem.constellation(sat)
print "Uranus now ", "RA = %s" % u.ra, "Dec = %s" % u.dec, "Alt = %s" % u.alt,  "Az = %s" % u.az
print ephem.constellation(u)
print "Neptune now ", "RA = %s" % n.ra, "Dec = %s" % n.dec, "Alt = %s" % n.alt,  "Az = %s" % n.az
print ephem.constellation(n)
print "Pluto now ", "RA = %s" % p.ra, "Dec = %s" % p.dec, "Alt = %s" % p.alt,  "Az = %s" % p.az
print ephem.constellation(p)
