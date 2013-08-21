a = {'interests':['electronics', 'food', 'computers'], 'name':'Douglas'}
print a['name']
print a['interests'][1]
print a
things = {"animals":["dog", "cat", "zebra" ]}
print things

person = {'interests':['electronics', 'food', 'computers'], 
               'name':'Douglas', "eyes":"blue", "hair":"peppered grey"}
for key in person:
	if (key == 'interests'):
		print "interests ...."
		for interest in person[key]:
			print "\tinterest is " + interest
			
	else:
		print "key is " + key + " value is " + person[key]
	
obj = {'a':1,'b': 2, 'c': [1, 3, 5]}

sum = 0
if 'c' in obj:
   for n in obj['c']:
     sum = sum + n

print sum	
