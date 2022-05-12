num1 = float(input("Enter first number: "))
operator = str(input("Enter operator: "))
num2 = float(input("Enter second number: "))

if operator == "+" or operator == "-" or operator == "*" or operator == "/":
    valid_operator = True
else:
    valid_operator = False

if num1 != 0 and num2 != 0:
    valid_nums = True
else:
    valid_nums = False

# Main logic
if not valid_nums:
    print("You need to insert valid numbers")
elif not valid_operator:
    print("You need to insert a valid operator")
else:

    if operator == "+":
        # the syntax is using an f print with the :, added to the end of that value
        result = num1 + num2
        result2 = f'{result:,}'
        print(str(num1) + " + " + str(num2) + " = " + result2)
    elif operator == "-":
        result = num1 - num2
        result2 = f'{result:,}'
        print(str(num1) + " - " + str(num2) + " = " + result2)
    elif operator == "*":
        result = num1 * num2
        result2 = f'{result:,}'
        print(str(num1) + " * " + str(num2) + " = " + result2)
    elif operator == "/":
        result = num1 / num2
        result2 = f'{result:,}'
        print(str(num1) + " / " + str(num2) + " = " + result2)
    else:
        print("Wrong operator")
