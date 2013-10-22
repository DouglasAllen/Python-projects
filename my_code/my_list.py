# my_list.py

def print_my_list(my_list):
  for each_item in my_list:
    if isinstance(each_item, list):
      print_my_list(each_item)
    else:
      print(each_item)
    
courses = ['Python', 45, [2013, ['USA', 20, 'India', 15, 'Japan', 5,'Germany', 5]]]
    
print_my_list(courses)

courses = ["Ruby", "JRuby", "Clojure", "Go", "Python"]

print(courses[0])
print(courses[1])
print(courses[-1])
print(courses[-3:])
print(courses[:])
print(courses + ["Erlang"])
courses[3] = "GO"
print(courses)
courses.append("Erlang")
print(courses)
print(len(courses))
courses.pop()
print(courses)
print(courses[2:5])
courses[2:5] = []
print(courses)
courses = ['Ruby', 'JRuby', 'Erlang']
print(courses)
courses.remove('JRuby')
print(courses)
courses.insert(0, "JRuby")
print(courses)
courses = ["Ruby", 35678, "JRuby", 1045, "Clojure", 346, "Go", 289,"Python", 45]
print(courses)
for course in courses:
  print(course)
  
courses1 = ['Ruby', 'JRuby']
courses2 = ['Go', 'Python']
courses3 = [courses1, courses2]
print(courses3)
print(courses3[0])
print(courses3[0][1])
courses = ['Python', 45, [2013, ['USA', 20, 'India', 15, 'Japan', 5,'Germany', 5]]]
for each_item in courses:
  print(each_item)
  
mentors = ["Satish", "Victor"]
print(isinstance(mentors, list))

x = 10
y = int(10.01)
if x < y:
  print( x, "is less than", y )
elif x > y:
  print( x, "is greater than", y )
else:
  print( x, "and", y, "are equal")