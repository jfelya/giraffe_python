my_list = ["my_list", 62, 38, "Jimmy", "Selena", "Ryan", 28, "end of the first list"]
print("This is your list: " + str(my_list))

print("What operation do you want to do to the list?")
operation = int(input("1: Pop \n2: Clear \n3: Extend \n4: Remove \n5: Append \n6: Insert\n"))

if operation == 1:
    my_list.pop()
    print("This is your new list: " + str(my_list))

if operation == 2:
    my_list.clear()
    print("This is your new list: " + str(my_list))

if operation == 3:
    my_list2 = ["my_list2", 99, "end of the second list"]
    my_list.extend(my_list2)
    print("This is your new list: " + str(my_list))

if operation == 4:
    new_content = input("What is the content you want to remove?: ")
    my_list.remove(new_content)
    print("This is your new list: " + str(my_list))

if operation == 5:
    new_content = input("What is the new content you want to add?: ")
    my_list.append(new_content)
    print("This is your new list: " + str(my_list))

if operation == 6:
    max_chars = len(my_list)
    position = int(input("In which position do you want to insert the new value? (starting from zero), "
                         "maximum position value is " + str(max_chars) + ": "))
    new_content = input("What is the new content you want to add?: ")

    if position >= 0 and new_content != "":
        my_list.insert(int(position), new_content)
        print("This is your new list: " + str(my_list))
