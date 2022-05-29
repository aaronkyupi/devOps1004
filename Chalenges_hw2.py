
# Making stairs
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("#", end=" ")
    print('')

print(' \n')

# Making X
size = 7
for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()

print(' \n')

# Calculating sum of the digits in a number
number = input('Enter a number: ')
result = sum(int(digit) for digit in str(number))
print(' The number is : ', number, "The sum of digits is: ", result)
