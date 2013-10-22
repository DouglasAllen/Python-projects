the_file = open('temp.txt', 'w')
print(the_file)
the_file.close()
the_file = open('temp.txt', 'r')
the_file.read()
the_file.close()

with open('my_list.py', 'r') as my_file:
  read_data = my_file.read()
  
print(read_data)

print(my_file.closed)

#~ with open('my_list.pl', 'r') as my_file:
  #~ read_data = my_file.read()
  
my_file = open('my_list.py', 'r')

for line in my_file:
  # Appends a space instead of a newline
  print(line, end='')
  
my_file.close()

f = open('workfile', 'wb')
f.write(b'0123456789abcdef')
f.seek(-3, 2)
f.seek(-3, 2)
f.close