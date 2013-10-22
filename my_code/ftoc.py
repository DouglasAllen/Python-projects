# ftoc.py

from decimal import *
getcontext().prec = 3
def convert(degf):
  return Decimal((degf - 32)) * Decimal(5) / Decimal(9)  
  
def gets():
  return input()
  
def puts(data):
  print(data)
  
def main():
  begin    = """   I will convert Fahrenheit degrees to Celsius degrees for you.
   Please enter the degrees in Fahrenheit at the prompt, entry =: ."""
  prompt = "   entry =:"  
  response1st   = "   Your entry was "
  response2nd   = " degrees Fahrenheit."
  answer1st   = "   The result of my calculation is "
  answer2nd   = " degrees Celsius"
  puts("")
  puts(begin)  
  puts("")
  puts(prompt)
  degf = gets()
  puts("")
  puts(response1st + degf + response2nd) 
  puts("")
  answer = str(convert(float(degf))) 
  puts(answer1st + answer + answer2nd)
  puts("") 
  
if __name__ == "__main__":
  main()
  #~ print("I will convert Fahrenheit degrees to Celsius degrees for you")
  #~ print("Please enter the degrees in Fahrenheit at the prompt")
  #~ degf = input("entry =: ")
  #~ print("Your entry was " + degf + " degrees Fahrenheit")
  #~ print("The result of my calculation is " + convert(degf) + " degrees Celsius." ) 