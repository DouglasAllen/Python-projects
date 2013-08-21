a = dict(one=1, two=2) 
b = dict({'one': 1, 'two': 2}) 
c = dict(zip(('one', 'two'), (1, 2))) 
d = dict([['two', 2], ['one', 1]])
e = dict.__new__(dict)

print a, b, c, d, e

print len(a), len(b), len(c), len(d)

print a['one'], d['two'] #, c['three']

d['two'] = 4
print d['two']

del d['two']
print d

print "is key 'two' in d?", 'two' in d
d['two'] = 2
print "is key 'two' in d?", 'two' in d

print "is key 'two' not in d?", 'two' not in d
del d['two']
print "is key 'two' not in d?", 'two' not in d

