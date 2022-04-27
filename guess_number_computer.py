import random
# randint(a, b) is gonna give us an integer number between the desired range of numbers


def guess(maxx):
    random_num = random.randint(1, maxx)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Insert a number between 1 and {maxx}: "))


guess(4)
