# Open a file with access mode 'a'
with open("employees2.txt", "a+") as file_object:
    # Append 'hello' at the end of file
    file_object.write("\nhello")
    print(file_object.read())
