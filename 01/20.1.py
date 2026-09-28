age = input("Введите возраст: ")

if not age.isdigit() or int(age) <= 0:
    print("Неверно, напишите правильный возраст :")
elif int(age) > 0 and int(age) <10:
    print("Milk")
elif  int(age) >= 10 and int(age) < 18:
    print("Juice")
elif int(age) >=18 and int(age) <= 70:
    print("Beer")
elif  int(age) > 70 and int(age) < 100:
    print("Tea")
else:
    print("age must be 1 to 99")



