import string
import keyword

name = input("Введите название: ")
result = True

if name[0].isdigit():
    result = False

if name.lower() != name:
    result = False

for i in string.punctuation:
    if i in name and i != "_":
        result = False

if " " in name:
    result = False



if name in keyword.kwlist:
    result = False

if name.strip("_") == "" and len(name) > 1:
    result = False


print(result)

