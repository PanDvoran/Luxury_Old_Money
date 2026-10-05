my_list = [6, 55, 0, -100, 33, 12, 10]

result = 0
indexes = []
index = 0

for item in my_list:
    if item > 0:
        result += item
        indexes.append(index)
    index += 1




print("Результа: ", result)
print("Индексы: ", indexes)
