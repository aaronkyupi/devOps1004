def square(num):
    print(num*num)


def square1(num):
    return(num*num)


square(4)
square(10)

print(square1(4))


def validate(prompt,low,high, ok, not_ok):
    input_from_user = int(input(prompt))
    if low < input_from_user < high:
        return ok
    else:
        return not_ok

print(validate("enter your age: ", 0, 120,"age ok", "age not ok"))
print(validate("enter your amount of pets: ", 0, 4,"pets ok", "pets not ok"))