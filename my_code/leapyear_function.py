# leapyear_function.py
def isLeapYear (year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return(True)
    else: return(False)
      
def main():
  print(isLeapYear(2000))
  print(isLeapYear(1996))
  print(isLeapYear(1900))
  
if __name__ == "__main__":
  main()