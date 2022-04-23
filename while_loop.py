# Guessing game

print("\nGuessing game")

secret_word = "yucuta"
guess = ""
i = 0
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if i >= 3:
        out_of_guesses = True
        print("You're out of guesses")
    else:
        guess = input("Enter your guess for the secret word: ")
        i += 1

if guess == secret_word:
    i = 3
    print("You did it!")
