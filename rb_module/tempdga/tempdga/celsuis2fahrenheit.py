""" converts a given temperature in Celcuis to Fahrenheit"""

class Celcuis2Fahrenheit:
    def __init__(self, c_temp):
        self.c_temp = c_temp
    def convert(self):
        self.temp_f = self.c_temp * 9/5 + 32
        return self.temp_f


def test():
    c_temp = 0.01000
    temp = Celcuis2Fahrenheit(c_temp)
    temp.convert()
    print("{0:f}".format(temp.temp_f))
     
if __name__ == "__main__":
    test()