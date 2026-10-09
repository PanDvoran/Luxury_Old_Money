my_list = [0, 1, 7, 2, 4, 8]

result = 0

for i in range(0, len(my_list), 2):
    result += my_list[i]

if my_list:
    result *= my_list[-1]
else:
    result = 0

print(result)