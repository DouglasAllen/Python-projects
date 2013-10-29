""" converts a given temperature in Fahrenheit to Kelvin """

class Fahrenheit2Kelvin:
    def __init__(self, f_temp):
        self.f_temp = f_temp
    def convert(self):
        return ((float(self.f_temp)+459.67)*5/9)


def test():
    f_temp = 32.018
    k_temp = Fahrenheit2Kelvin(f_temp)
    t = k_temp.convert()
    print("{0:f}".format(t))
     
if __name__ == "__main__":
    test()       