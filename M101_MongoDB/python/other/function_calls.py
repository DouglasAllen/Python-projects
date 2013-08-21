fruits = ["apple", "orange", "grape", "kiwi", "orange", "apple"]

def analyze_list(list):
	counts = {}
	for item in list:
		if item in counts:
			counts[item] = counts[item] +1
		else:
			counts[item] = 1
	
	return counts
		
counts = analyze_list(fruits)
print counts