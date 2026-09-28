age = input("Введите возраст: ")

if not age.isdigit() or int(age) <= 0:
    print("Неверно, напишите правильный возраст. ")
elif 0 < int(age) < 10:
    print("Milk")
elif  10 <= int(age) < 18:
    print("Juice")
elif 18 <= int(age) <= 70:
    print("Beer")
elif  70 < int(age) < 100:
    print("Tea")
else:
    print("age must be 1 to 99")



