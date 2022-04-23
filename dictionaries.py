monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Jan"])
# Object.get() makes us get a null value off the key if not found, not throwing an error
# and you can assign a default value on the second parameter
print(monthConversion.get("Luv", "Not a valid key"))
