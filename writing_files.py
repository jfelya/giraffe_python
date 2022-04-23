# Open a file with access mode 'a'
# w would overwrite the entire text
with open("employees2.txt", "a+") as file_object:
    # Append 'hello' at the end of file
    text_insert = input("Type the text you want to append to the file: ")
    text_insert2 = "\n" + text_insert
    file_object.write(text_insert2)

with open("employees2.txt", "r") as file_object:
    for line in file_object:
        print(line.strip())