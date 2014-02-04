""" converts a given temperature in Fahrenheit to Kelvin"""

class Fahrenheit2Kelvin:
    def __init__(self, f_temp):
        self.f_temp = f_temp
    def convert(self):
        self.k_temp = (self.f_temp + 459.67) * 5/9
        return self.k_temp


def test():
    f_temp = 32.018
    temp = Fahrenheit2Kelvin(f_temp)
    temp.convert()
    print("{0:f}".format(temp.k_temp))
     
if __name__ == "__main__":
    test()