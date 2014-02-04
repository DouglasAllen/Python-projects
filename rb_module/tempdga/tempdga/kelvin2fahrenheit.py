""" converts a given temperature in Kelvin to Fahrenheit"""

class Kelvin2Fahrenheit:
    def __init__(self, k_temp):
        self.k_temp = k_temp
    def convert(self):
        self.f_temp = self.k_temp * 9/5 - 459.67
        return self.f_temp


def test():
    k_temp = 273.160000
    temp = Kelvin2Fahrenheit(k_temp)
    temp.convert()
    print("{0:f}".format(temp.f_temp))
     
if __name__ == "__main__":
    test()       