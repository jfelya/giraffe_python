try:
    # ans = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("You need to insert a number")
except ZeroDivisionError as err:
    print(err)
