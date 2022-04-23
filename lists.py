# PART 3
print("PART 3: Tuples")
# Tuples can't be changed
coordinates = (2, 4)
# coordinates[1] = 5
# You treat it like a list
print(coordinates[0])

# PART 2
print("PART 2:")
lucky_numbers = [55, 28, 66, 33, 22, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Toby"]
print(friends)
print(lucky_numbers)

# This .extend function will add an array and add it to the end of the current array
friends.extend(lucky_numbers)

# This is to insert a value after a certain index
# All the other elements are going to be pushed to the right
friends.insert(3, "This was inserted after the third index")

# This function will add our parameter to the end of the array
friends.append("Creed")

# Just me fooling around to find the middle of the array
middle = round(len(friends) / 2)
friends[middle] = "This is in the middle"

# This is going to remove the element that matches with the parameter
friends.remove("Jim")

print(friends)

# This will remove the last element of a list
friends.pop()

# This will count the amount of times a parameter is repeated on the list
print("Toby is repeated " + str(friends.count("Toby")) + " times on the list")

print(friends)

# This will sort a list in ascending order
lucky_numbers.sort()
print(lucky_numbers)

# Descending order
lucky_numbers.reverse()
print(lucky_numbers)

# This will copy all the values from the previous list into the new one
friends2 = friends.copy()
friends2.insert(0, "Friends2")
print(friends2)

# input_name = input("Now enter a name you want to look on the list: ")
# while friends.index(input_name) >= 0:
#    print(input_name + " is on the list at position: " + str(friends.index(input_name)))

# This will empty the list entirely
# friends.clear()

# PART 1
print("\nPART 1:")
friends = ["Kevin", "Josh", "Jim", "Rose", "Chris", "Scott", "Karen"]
friends[1] = "This value was changed"

print(friends)
# This will grab the element at position 1 all the following elements
print(friends[1:])
# This will grab all the elements from position 2 to position 5
print(friends[2:5])
