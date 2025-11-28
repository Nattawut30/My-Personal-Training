# Keyword Arguments = an argument preceded by an identifier
#                   helps with readability
#                   order of arguments doesn't matter
#                   1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# The keyword must be precise, you can refine it
# So, make sure any positional arguments are correct
hello("Hello", "Mr.", "Spongebob", "Squarepants")
hello("Hello", "Mr.", last= "John", first= "James")
print()

for x in range(1, 11):
    print(x, end=" ")
print()

print("1", "2", "3", "4", "5", sep="-")
print()

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=66, area=92, first=271, last=6680)
print(phone_num)

