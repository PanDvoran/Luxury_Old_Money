import string

name = input("Введите имя: ")
name = name.title()
result = ""
result = "#" + result

for char in name:
    if char in string.punctuation or char == " ":
        continue
    result += char

if len(result) > 140:
    result = result[:140]

print(result)
