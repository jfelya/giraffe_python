cedulas = {
    "fely": "26754147"
}
# ,
#     "guislain": "8900121",
#     "magda": "10923330"

ceds = list(cedulas.values())

word = []
for letter in ceds:
    print(f"Letter: {letter}")
    for let in letter:
        print(f"Let: {let}")
        word.append(let)

print(word)