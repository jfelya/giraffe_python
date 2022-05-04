# Creating a list
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
