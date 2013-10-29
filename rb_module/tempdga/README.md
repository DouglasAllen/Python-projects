A test.py file.

'''
Created on Oct 22, 2013

@author: kb9agt
'''

import tempdga.fahrenheit2celsuis

import tempdga.fahrenheit2kelvin

def test():

    f_temp = 32.018
    
    cns = tempdga.fahrenheit2celsuis.Fahrenheit2Celcuis(f_temp)
    
    c_temp = cns.convert()
    
    print("{0:f} degrees Fahrenheit = {1:f} degrees Celcuis".format(f_temp, c_temp))
    
    kns = tempdga.fahrenheit2kelvin.Fahrenheit2Kelvin(f_temp)
    
    k_temp = kns.convert()
    
    print("{0:f} degrees Fahrenheit = {1:f} Kelvin".format(f_temp, k_temp))
    
if __name__ == '__main__':

    test()