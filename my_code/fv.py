def calculate_new_balance(d, r):   
    return(d + d * r / 100 )    

if __name__ == "__main__":
  r, d, n = 0.5, 1000.00, 12
  month = n + 1  
  print("Given the following values I will calculate your new balance for each month")
  print("The formula is (new balance = deposit * (1 + rate)^months)")
  print("The interest rate is %.2f percent monthly." % (r))
  print("Your deposit is %.2f." % (d))
  print("You wish to see the balance after each month")
  while n > 0:
    d = calculate_new_balance(d, r)
    print("balance after %d months is %.2f." % (month - n, d))   
    n -= 1 
    
    
#~ def calculate_new_balance(n, d, r):
  #~ return(d * (1 + r / 100) ** n)
      

#~ if __name__ == "__main__":
  #~ n, d, r = 12, 1000, 0.5  
  #~ print("Given the following values I will calculate your new balance.")
  #~ print("The formula is (new balance = deposit * (1 + rate)^months).")
  #~ print("The interest rate is %.2f percent monthly." % (r))
  #~ print("Your deposit is %.2f." % (d))
  #~ print("You wish to see the balance after %d months." % (n))
  #~ print("balance after %d months is %.2f." % (n, calculate_new_balance(n, d, r)))      
    