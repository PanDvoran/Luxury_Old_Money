my_list = [0, 1, 0, 12, 3]

while 0 in my_list:
    my_list.remove(0)
    my_list.append(0)

print(my_list)