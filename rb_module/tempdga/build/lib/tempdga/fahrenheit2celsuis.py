""" converts a given temperature in Fahrenheit to Celcuis"""

class Fahrenheit2Celcuis:
    def convert(self, f_temp):
        return ((float(f_temp)-32)*5/9)


def test():
    f_temp = 32.018
    c_temp = FahrenheittoCelcuis.convert(FahrenheittoCelcuis, f_temp)
    print("{0:f}".format(c_temp))
     
if __name__ == "__main__":
    test()
    
    

