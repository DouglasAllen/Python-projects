from astral import *

#~ from astral import GoogleGeocoder
a = Astral()
#~ a = Astral(GoogleGeocoder)
#~ location = a['Dekalb, Illinois']
#~ timezone = location.timezone
#~ lat, lng = location.latitude, location.longitude
from datetime import date
d = date.today()#(2013, 10, 26)
#~ sun = location.sun(local=True, date=d)
#~ print('Sunrise:    %s' % str(sun['sunrise']))

print(a._julianday(d))
print(a._jday_to_jcentury(a._julianday(d)))
print(a._jcentury_to_jday(a._jday_to_jcentury(a._julianday(d))))
print(a._mean_obliquity_of_ecliptic(a._jday_to_jcentury(a._julianday(d))))
print(a._obliquity_correction(a._jday_to_jcentury(a._julianday(d))))
print(a._geom_mean_long_sun(a._jday_to_jcentury(a._julianday(d))))
print(a._eccentrilocation_earth_orbit(a._jday_to_jcentury(a._julianday(d))))
print(a._geom_mean_anomaly_sun(a._jday_to_jcentury(a._julianday(d))) % 360)

epsilon = a._obliquity_correction(a._jday_to_jcentury(a._julianday(d)))
solar_mean_lng = a._geom_mean_long_sun(a._jday_to_jcentury(a._julianday(d)))
orbital_eccentric = a._eccentrilocation_earth_orbit(a._jday_to_jcentury(a._julianday(d)))
solar_mean_anomaly = a._geom_mean_anomaly_sun(a._jday_to_jcentury(a._julianday(d))) % 360.0
print(solar_mean_anomaly)
eot = a._eq_of_time(a._jday_to_jcentury(a._julianday(d)))
print(eot)
from math import *
y = tan(radians(epsilon) / 2.0)
y = y * y

sin2l0 = sin(2.0 * radians(solar_mean_lng))
sinm = sin(radians(solar_mean_anomaly))
cos2l0 = cos(2.0 * radians(solar_mean_lng))
sin4l0 = sin(4.0 * radians(solar_mean_lng))
sin2m = sin(2.0 * radians(solar_mean_anomaly))

equation_of_time = y * sin2l0 - \
             2.0 * orbital_eccentric * sinm + \
             4.0 * orbital_eccentric * y * sinm * cos2l0 - \
             0.5 * y * y * sin4l0 - \
            1.25 * orbital_eccentric * orbital_eccentric * sin2m
            
print(equation_of_time)
eot = degrees(equation_of_time)
print(eot)
print(eot * 4.0)
solar_true_anomaly = a._sun_true_anomoly(a._jday_to_jcentury(a._julianday(d))) % 360.0
solar_true_lng = a._sun_true_long(a._jday_to_jcentury(a._julianday(d)))
solar_apparent_lng = a._sun_apparent_long(a._jday_to_jcentury(a._julianday(d)))
solar_right_ascension = a._sun_rt_ascension(a._jday_to_jcentury(a._julianday(d)))
print(solar_mean_anomaly)
print(solar_true_anomaly)
print(solar_mean_lng)
print(solar_true_lng)
print(solar_apparent_lng)
print(solar_right_ascension)
eot = solar_mean_anomaly - solar_true_anomaly + solar_apparent_lng - solar_right_ascension
print(eot)
print(eot * 4.0)
eot = solar_mean_anomaly - solar_true_anomaly + solar_true_lng - solar_right_ascension
print(eot)
print(eot * 4.0)
eot = solar_mean_anomaly - solar_true_anomaly + solar_mean_lng - solar_right_ascension
print(eot)
print(eot * 4.0)