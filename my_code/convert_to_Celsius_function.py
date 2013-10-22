# Fahrenheit_to_Celsius.py
 
from decimal import *
getcontext().prec = 3
class Fahrenheit_to_Celsius:
  def convert(degf):
    return Decimal((degf - 32)) * Decimal(5) / Decimal(9)
 
def main():
  begin = """
    I will try to convert Fahrenheit degrees to Celsius degrees for you. 
    Plaese don't enter letters or I will error on you. lol
    If you don't understand then just hit enter or return on your keyboard.
          """
  
  print(begin)      
  entry = input("entry = : ") 
    
  if entry != "":
    degf = float(entry)     
    print("""
        Your entry was %.3f degrees Fahrenheit.
        The result of my calculation was %.3f degrees Celsius.
              """ % ((degf),  Fahrenheit_to_Celsius.convert(degf))) 
  else:
    print("""
        That wasn't valid input!
        Please enter the degrees in Fahrenheit as a number you wish to convert to degrees Celsius and try again.
              """)         
    
if __name__ == "__main__":    
    main()
    
                  
    
"""
    I will try to convert Fahrenheit degrees to Celsius degrees for you. 
    Plaese don't enter letters or I will error on you. lol
    If you don't understand then just hit enter or return on your keyboard.
    
entry =: 32.018
    
        Your entry was 32.018 degrees Fahrenheit.
        The result of my calculation was 0.010 degrees Celsius.
"""