import ephem
from astral import *
from astral import GoogleGeocoder

a = Astral(GoogleGeocoder)
location = a['150 Joanne Lane, Dekalb, IL']
print('Latitude: %.02f; Longitude: %.02f' % (location.latitude, location.longitude))
print(location.elevation * 3.28084)

here = ephem.Observer()
here.lon = str(location.longitude)
here.lat = str(location.latitude)

sun = ephem.Sun()
sun.compute(here)

nr = here.next_rising(sun)
nt = here.next_transit(sun)
ns = here.next_setting(sun)

print( "Sun next rising at %s" % ephem.localtime(nr))
print( "Sun next transit at %s" % ephem.localtime(nt))
print( "Sun next setting at %s" % ephem.localtime(ns))