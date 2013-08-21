def mult(a, b):
	print b
	if b == 0:
		return 0
		
	rest = mult(a, b - 1)
	print rest
	
	value = a + rest
	print value
	
	return value
#~ print "3 * 2 = ", mult(3, 2)
mult(3, 4)