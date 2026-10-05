list_1 = [2, 222, 224, "New", (), [], 0]

a = len(list_1) // 2

if len(list_1) % 2:
    a += 1

list_2 = list_1[0:a]
list_3 = list_1[a:]

list_4 = [list_2, list_3]

print(list_4)
