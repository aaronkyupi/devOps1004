# Excercise 1 and 2
try:
   a = 1 / 0
except:
   print("Division by zero")

# Excercise 3 - Yes it is
try :
    x = 1
finally :
    print('Finally')

# Excercise 4 - all types of exceptions

# Excercise 5
# "Bad Practice" because it will give all errors without their special reason

# Excercise 6
# Except IOError - input/output exceptions
# Except ZeroDivisionError - divison by zero of a number


# Excercise 7:
my_file = open('words.txt','w')
my_file.close()

# Excercise 8
my_file = open('words.txt','w')
my_file.write("Aaron")
my_file.close()

# Excercise 9
my_file = open('words.txt','r')
str = my_file.read()
print(str)
my_file.close()

# Excercise 10
my_file2 = open('utf8.txt','w',encoding='utf-8')
my_file2.write("אהרון")
my_file2.close()

my_file2 = open('utf8.txt','r',encoding='utf-8')
str = my_file2.read()
print(str)

