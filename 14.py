try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a / b)
    r = open("file_not_exists.txt")
except Exception as e:
    print("something went wrong")
    print(e.args)
except ZeroDivisionError:
    print("cant devide by zero")
except FileNotFoundError:
    print("cant open file")
print("blablbla")