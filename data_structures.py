# Creating a list
print("LISTS:\n")
alist = ["math", "science", "math", "art", "engineering", "security", "accountings"]
print(type(alist))
print(alist)

# negative indexes return elements from the end of the list
# imagine the list is a mirror, 0 would return the first element
print(alist[-1])

# Slicing
# the element at the end index is never included
# Only elements from start index till index equaling end-1 will be returned.
print(alist[2:4])

# Adding new elements
# append() inserts at the end
# insert() inserts at a specific index
alist.append("history")
print(alist)
alist.insert(0, "historia")
print(alist)

# Removing
# remove() – Removes the first occurrence from the list that matches the given value
# pop() – remove an element at a specified index from the list. If no index value, the last element will be removed from the list
alist.remove("engineering")
print(alist)
alist.pop()
print(alist)
alist.pop(0)
print(alist)

# Sorting
my_list = ["example", "eximples", "eixamples"]
print(my_list)
# ascending order
my_list.sort()
print(my_list)
# descending order
my_list.sort(reverse=True)
print(my_list)

# Concatenating
conc1 = ["hola1", "hola2"]
conc2 = ["hola3", "hola4", "hola5"]
conc3 = conc1 + conc2
print(conc3)

# LIST COMPREHENSIONS
# using for loop
comp = [1, 2, 3, 4]
print(comp)
square = []
for x in comp:
    square.append(x**2)
print(square)

# using list comprenhension
# SYNTAX:
# [expression for item in iterable if condition == True]
square2 = [x**2 for x in comp]
print(square2)

# Stacks are just list where you only append and pop the end of it
# Queues are just lists where you remove at the beginning

# TUPLES
# they're the same as lists except that they're immutable
print("\nTUPLES:\n")
polo = ("hol11", "extreme")
# you can write it without the parenthesis
polo2 = "holl", "exxxx"
print(polo)
print(polo2)

# Tuple assignment
# tuple packing
planet = ("earth", "mars", "jupiter")

# tuplet unpacking
a, b, c = planet

print(a)
print(b)
print(c)

# imaginary tuples
a, b = 10, 12

print(a)
print(b)

# swapping values in a single line
a, b = b, a
print(a)
print(b)

# You can change a tuple to a list with list()
# And you can change a list into a tuple with tuple()
# but the proccess is expensive as it involves making a copy of the tuple

# DICTIONARIES
# Dictionary uses the item key to quickly find the item value. This concept is called hashing
print("\nDICTIONARIES:\n")
my_jisho = {
    "japan": "tokyo",
    "venezuela": "caracas",
    "usa": "washington",
    "uk": "london",
    "venezuela": "maracaibo"
}
# the item value will be the one associated with the last key
print(my_jisho["venezuela"])

# making a list out of the keys of the dictionary
poli = list(my_jisho.keys())
print(poli)
# using a for loop to get the values
poli2 = my_jisho.values()
for v in poli2:
    print(v)
# We can even access these values simultaneously using the items() method which returns the respective key and value pair for each element of the dictionary.
for key, value in my_jisho.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

# TESTS
print("\nTESTS: ")
cedulas = {
    "fely": "26754147",
    "guislain": "8900121",
    "magda": "10923330"
}

# Gotta convert it to a list since the keys() function doesnt return an iterable variable
ced_keys = list(cedulas.keys())

resp = str(input(f"De quien quieres la cédula? {ced_keys[0]} (1), {ced_keys[1]} (2) ó {ced_keys[2]} (3)?\n").lower())
if resp == "1":
    print(f"La cédula de {ced_keys[0]} es {cedulas[ced_keys[0]]}")
elif resp == "2":
    print(f"La cédula de {ced_keys[1]} es {cedulas[ced_keys[1]]}")
elif resp == "3":
    print(f"La cédula de {ced_keys[2]} es {cedulas[ced_keys[2]]}")
