my_list = ["my_list", 62, 38, "Jimmy", "Selena", "Ryan", 28, "end of the first list"]
print("This is your list: " + str(my_list))

bool_val = input("\nDo you wanna pop the list? \ny/n: ")
if bool_val == "y" or bool_val == "yes" or bool_val == "yeah":
    my_list.pop()
    print("This is your new list: " + str(my_list))

bool_val = input("\nDo you wanna clear the list? \ny/n: ")
if bool_val == "y" or bool_val == "yes" or bool_val == "yeah":
    my_list.clear()
    print("This is your new list: " + str(my_list))

my_list2 = ["my_list2", 99, "end of the second list"]
bool_val = input("\nDo you wanna extend the list? with " + str(my_list2) + "?\ny/n: ")
if bool_val == "y" or bool_val == "yes" or bool_val == "yeah":
    my_list.extend(my_list2)
    print("This is your new list: " + str(my_list))

bool_val = input("\nDo you wanna remove something in the list? \ny/n: ")
if bool_val == "y" or bool_val == "yes" or bool_val == "yeah":
    new_content = input("What is the content you want to remove?: ")
    my_list.remove(new_content)
    print("This is your new list: " + str(my_list))

bool_val = input("\nDo you wanna append something at the end of the list? \ny/n: ")
if bool_val == "y" or bool_val == "yes" or bool_val == "yeah":
    new_content = input("What is the new content you want to add?: ")
    my_list.append(new_content)
    print("This is your new list: " + str(my_list))

bool_val = input("\nDo you wanna insert a new value in the list? \ny/n: ")
if bool_val == "y" or bool_val == "yes" or bool_val == "yeah":
    max_chars = len(my_list)
    position = int(input("In which position do you want to insert the new value? (starting from zero), "
                         "maximum position value is " + str(max_chars) + ": "))
    new_content = input("What is the new content you want to add?: ")

    if position >= 0 and new_content != "":
        my_list.insert(int(position), new_content)
        print("This is your new list: " + str(my_list))
