my_list = [6, 55, 0, -100, 33, 12, 10]

result = 0
indexes = []

for item in enumerate(my_list):
    if item[1] > 0:
        result += item[1]
        indexes.append(item[0])

print("Результат: ", result)
print("Индексы: ", indexes)



