""" converts a given temperature in Fahrenheit to Kelvin """

class Fahrenheit2Kelvin:
    def convert(self, f_temp):
        return ((float(f_temp)+459.67)*5/9)


def test():
    f_temp = 32.018
    c_temp = FahrenheittoKelvin.convert(FahrenheittoKelvin, f_temp)
    print("{0:f}".format(c_temp))
     
if __name__ == "__main__":
    test()       