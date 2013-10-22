A test.py file.

'''
Created on Oct 22, 2013

@author: kb9agt
'''

import tempdga.fahrenheit2celsuis

import tempdga.fahrenheit2kelvin

def test():

    f_temp = 32.018
    
    cns = tempdga.fahrenheit2celsuis.Fahrenheit2Celcuis
    
    c_temp = cns.convert(cns, f_temp)
    
    print("{0:f}".format(c_temp))
    
    kns = tempdga.fahrenheit2kelvin.Fahrenheit2Kelvin
    
    k_temp = kns.convert(kns, f_temp)
    
    print(k_temp)
    
if __name__ == '__main__':

    test()