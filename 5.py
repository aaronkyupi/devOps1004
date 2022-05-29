isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
my_names = ["adi", "ben", "noam", "artur", "ron" ]
my_list = []
c = [1, 2, 3]
d = [1, 2, 3]

if a == b:
    print("a equals b")
if c == d:
    print("c equals d")
if a is b:
    print("a equals b")
if c is d:
    print("c equals d")

if my_list:
    print("my list is not empty")

if len(my_names) > 2:
    print("I remember enough names")

if "zohar" in my_names:
    print("it is in the list")
else:
    print("it is not in the list")

if a < b and not (strThree == 3 or isTrue == 4):
    print("a is less than b")
elif a == b:
    print("a is equal b")
else:
    print("a is greater than b")

age = int(input("Enter your age: "))
if 0 < age < 120:
    print("age is ok")
