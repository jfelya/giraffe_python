def say_hi(name, age):
    print("Hello " + str(name) + ", you're " + str(age))


say_hi("Fely", 23)
say_hi("Tom", 38)


def cube(number):
    return number * number * number


# The return keyword makes the code exit the function

result = cube(3)
print(result)
