character_name = "Fely"
character_age = "23"
custom_string = "The nine tailed fox attacked the village"

print(custom_string.replace("nine", "eight"))

# The built-in function will look up the position of the paramater passed
# If the parameter is not found the function will throw an error
print("The index of \"Fox\" is: ")
print(custom_string.index("fox"))

custom_array = ["Fe", "ly"]
print(custom_array[0])

# Printing out the last letter of the variable using array index to look for it
print(character_name[len(character_name) - 1])

print("There once was a man named " + character_name.upper() + ",")

# This function returns a boolean value about the variable being in upper case or not
print(character_name.upper().isupper())

# This function returns the number of characters in the variable
print(len(character_name))

print("he was " + character_age + " years old. ")
character_name = "Tom"
character_age = "48"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

number1 = 2
number2 = 3.32
total = number1 + number2

print("\n\"Total\" with a variable combining the two:")
print(total)
print("\n\"Total\" in the print statement:")
print(number1 + number2)
