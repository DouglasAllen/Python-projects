""" converts a given temperature in Fahrenheit to Celcuis"""

class Fahrenheit2Celcuis:
    def __init__(self, f_temp):
        self.f_temp = f_temp
    def convert(self):
        return ((float(self.f_temp)-32)*5/9)


def test():
    f_temp = 32.018
    c_temp = Fahrenheit2Celcuis(f_temp)
    t = c_temp.convert()
    print("{0:f}".format(t))
     
if __name__ == "__main__":
    test()
    
    

