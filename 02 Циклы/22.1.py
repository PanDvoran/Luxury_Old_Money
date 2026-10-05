my_list = [6, 55, 0, -100, 33, 12, 10]
print(my_list[-1])
print(my_list[len(my_list)-1])
print(len(my_list))

result = 0
index = 0

while index < len(my_list):
    if my_list[index] > 0:
        result += my_list[index]

    index += 1

print("Результа: ", result)


result = 0
for item in my_list:
    if item > 0:
        result += item


print("Результа: ", result)
