# The 'with' statement ensures that the file is closed even if your program throws an exception when reading the file.
# If you want to read a file line by line, this would be a better option. The 'for line in f:' iterates over the file as a list. The 'line' variable includes the trailing '\n' or '\r\n', so you'll want to strip those.
with open("employees.txt", "r") as t:
    for line in t:
        print(line.strip())

print("\n Second read: ")
# if employee_file.readable():
#     print("The file is readable and ready to use")
# else:
#     print("The file cant be accessed")

employee_file = open("employees.txt", "r")
# Repeating the function will make the program read the next line of text
# Seems like the file should be fresh and unread for the readlines() to work
for emp in employee_file.readlines():
    print(emp)

# This will spit out all the text in the file
# print(employee_file.read())



# Good idea to close the file when done using it
employee_file.close()