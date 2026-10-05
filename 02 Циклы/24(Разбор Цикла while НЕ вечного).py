while 10 > 0:
    age = input("Enter your age: ")

    if age.isdigit():
        break
    print("Invalid input. Please enter a valid age.")

print("Your age is:", age)

# while 10 > 0: это услвоие для вечного цикла
# если человек пишет цифру то if age.isdigit(): становится True и потом срабатывает подусловие break
# break делает выход из нашего цикла и снизу в print("Your age is:", age) человеку ввыодиться его возраст
# Если написать буквы вместо цифр то if age.isdigit(): становится False и break НЕ срабатывает
# А срабатывает  print("Invalid input. Please enter a valid age.") потому что он НЕ в if , а идет дальше по коду
# и человеку вылезит подсказка что он ввел неверное значение(что он не должен писать буквы)
