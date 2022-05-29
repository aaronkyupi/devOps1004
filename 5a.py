a = ("hello world")
my_names = ["adi", "ben", "noam", "artur", "ron"]

print(list(range(1,10, 1)))

for i in range(1, 6):
    print(f"{i} hello")

for name in my_names:
    print(f"hello {name}")
    if name == "arthur:" :
        break
# there is also "continue"

else:
    print("printed all names")

for i in range(len(my_names)):
    print(i)
    print(type(i))
    print(my_names[i])

a = 0
while a < 5:
    print(a)
    a = a+1

l = []
current_input = input("enter letter: ")
while current_input != "q":
    l.append(current_input)
    current_input = input("enter letter: ")

print(f"inputs are {l}")

n = [1, 2, 3, 4,5]
result = []
for num in n:
    result.append(num * 2)

result = [num * 2 for num in n if num > 2]