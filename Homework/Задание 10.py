list_1 = [2, 222, 224, "New", (), [], 000]
list_2 = list_1[0:4]
print(list_2)
list_3 = []
list_3.extend(list_1 + list_2)
print(list_3)

