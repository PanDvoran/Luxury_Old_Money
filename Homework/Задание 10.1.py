





list_1 = [2, 222, 224, "New", (), [], 0]
list_2 = list_1[0:4]
list_3 = list_1[4::]
list_4 = []
list_4.append(list_2)
list_4.append(list_3)

print(list_4)

