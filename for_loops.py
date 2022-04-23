for letter in "Hola":
    print(letter)

friends = ["Jim", "Karen", "Tom"]
for letter in friends:
    print(letter)

print("\n")
for i in range(len(friends)):
    if i == 0:
        print("First iteration of friends")
    else:
        print(friends[i])

print("\n")
# range() will not include the last number
for i in range(5):
    print(i)

print("\n")
for i in range(3, 5):
    print(i)
