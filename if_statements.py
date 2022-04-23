is_male_logic = input("Are you male? y/n: ")
is_tall_logic = input("Are you tall? y/n: ")

# Filling up the variables according to the user's input
if is_male_logic == "y" or is_male_logic == "yes" or is_male_logic == "Y" or is_male_logic == "Yes" or is_male_logic \
        == "yeah" or is_male_logic == "Yeah":
    is_male = True
else:
    is_male = False

if is_tall_logic == "y" or is_tall_logic == "yes" or is_tall_logic == "Y" or is_tall_logic == "Yes" or is_tall_logic \
        == "yeah" or is_tall_logic == "Yeah":
    is_tall = True
else:
    is_tall = False

# End of the filling

# Start of the logic process
if is_male and is_tall:
    print("You're a tall man")
elif not is_male and is_tall:
    print("You're a tall woman")
elif is_male and not is_tall:
    print("You're a short man")
else:
    print("You're a short woman then!")
