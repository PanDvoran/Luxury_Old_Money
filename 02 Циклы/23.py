number = int(input("Enter a number: "))

result = 0

while number > 0:
    print("Current number:", number)

    if number % 5 == 0:
        print("Number is divisible by 5. Skipping this iteration.")
        continue

    result += number  # result = result + number

    if result >= 1000:
        print("Result has reached or exceeded 1000. Breaking the loop.")
        break

    number -= 1

else:
    print("Loop has ended.")

print("Sum of numbers:", result)

#
# Если у нас number будет таким числом что при деление на 5 у нас будет ровное число без остатка то это будет True
# То есть if number % 5 == 0: условие говорит после деление будет ровное число и остатка после комы не будет то это True
# Если сумма результатов к примеру будует 1050 это больше 1000 по второму if тогда это True и выполняется break
# мы выходим с программы
# else сработает если наш while number > 0: станент по условие False к примеру number будет 0 или -1, тогда будет else