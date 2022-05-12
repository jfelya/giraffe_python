def login():
    first_input = str(input("Login (l) or create an account (c)?: ")).lower()
    if first_input == "c":
        signup()
    else:
        with open("user_info.txt", "r") as file_object_read:
            user_input = str(input("Insert your username: ")).lower()
            password_input = str(input("Insert your password: ")).lower()
            user_pass = False
            password_pass = False
            for line in file_object_read:
                if user_input == line:
                    user_pass = True
                if password_input == line:
                    password_pass = True

            if user_pass and password_pass:
                print("You have successfully logged in")
            else:
                print("Your username or password don't match\n")
                login()



def signup():
    user_input = str(input("Insert your username: ")).lower()
    password_input = str(input("Insert your password: ")).lower()
    if user_input != "" and password_input != "":
        with open("user_info.txt", "w") as file_object:
            all_user = user_input + "\n" + password_input
            try:
                file_object.write(all_user)
            except:
                print("Something happened")
        print("You have created your account successfully")
        login()
    else:
        print("You should insert valid data")
        login()


login()
