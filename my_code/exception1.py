# number = int(input("Enter a number: "))
# print("You entered:", number)
# try:
#   your code (which might cause a runtime error)
# except:
#   your error-recovery code

try: 
  number = int(input("Enter a number: "))  
  print("You entered:", number)
except ValueError as err:
  print("That was not a number. " + str(err))
  
#~# Extend try with finally
# try:
#~# open files
#~# do some processing
# except IOError:
# print(’File error.’)
# finally:
#~# close files

