number = int(input("Введите число: "))

while number > 9:
    result = 1

    while number > 0:
        last_digit = number % 10
        result *= last_digit
        number //= 10

    number = result

print(number)