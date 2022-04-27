import random
# randint(a, b) is gonna give us an integer number between the desired range of numbers


def guess(maxx):
    random_num = random.randint(1, maxx)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Insert a number between 1 and {maxx}: "))
        if guess < random_num:
            print("Too low")
        elif guess > random_num:
            print("Too high")
        else:
            print(f"{random_num} is the number, congratulations!")


def computer_guess(maxxx):
    low = 1
    high = maxxx
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = str(input(f"Guess: {guess}.\nIs the number high? (H), low (L) or correct (C)?: ")).lower()
        # TEST
        print(feedback)
        if feedback == "h":
            high = guess - 1
            print("Low is: " + str(low))
            print("High is: " + str(high))
        elif feedback == "l":
            low = guess + 1
            print("Low is: " + str(low))
            print("High is: " + str(high))

    print(f"The computer guessed {guess}, that's the number!")


computer_guess(10)
