import ephem

here = ephem.Observer()
here.lon = '-88.7431' # my coordinates
here.lat = '41.9475'

sun = ephem.Sun()
sun.compute(here)

nr = here.next_rising(sun)
nt = here.next_transit(sun)
ns = here.next_setting(sun)

print "Sun next rising at %s" % ephem.localtime(nr)
print "Sun next transit at %s" % ephem.localtime(nt)
print "Sun next setting at %s" % ephem.localtime(ns)