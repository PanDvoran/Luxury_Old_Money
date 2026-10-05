number = int(input("Введите число: "))

result = 0
while number > 0:
    print("Коректное число: " , number)
    result += number
    number -= 1
print("Какой-то результат: ", result)
