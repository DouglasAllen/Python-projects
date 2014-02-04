""" converts a given temperature in Fahrenheit to Celcuis"""

class Fahrenheit2Celcuis:
    def __init__(self, f_temp):
        self.f_temp = f_temp
    def convert(self):
        self.temp_c = (self.f_temp-32)*5/9
        return self.temp_c


def test():
    f_temp = 32.018
    temp = Fahrenheit2Celcuis(f_temp)
    temp.convert()
    print("{0:f}".format(temp.temp_c))
     
if __name__ == "__main__":
    test()
    
    

