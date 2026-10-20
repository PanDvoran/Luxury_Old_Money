

def say_hi(name, age):
    answer = f"Hi. My name is {name} and I'm {age} years old"
    return answer


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"

print(say_hi("Alex", 32))
print(say_hi("Frank", 68))


# По условиям задачи у нас уже есть кусок готового кода:
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old" и второй вариант
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
# СТРОКА 1
# def say_hi(name, age): - мы срздаем функцию где указываем два аргумента. Именно два аргумента потому что нам нужно
# подставить только имя и возраст и потому что в функцию прокидываем только 2 аргумента: "Alex", 32 и "Frank", 68
# СТРОКА 2
# answer = f"Hi. My name is {name} and I'm {age} years old" - мы используем f-строки что бы в текст с помощью аргумен-
# тов можно было подставить хначение в name, age как {name}, {age} - это наши ящики куда мы будем подставлять значения
# наших аргументов, answer это переменная, которая имеет f-строку
# СТРОКА 3
# return answer - наш return возвращает значение переменной answer, а именно f-строку и return дает этот ответ в
# print, елси напишем print и функцию с аргументами мы получим ответ
# СТРОКА 4
# assert - assert равняеться какому-то тексту и он проверяет что функция через f-строку  возвращает точь в точь
# текст, которому равняеться assert, если текст равняеться то это True и код работает нормально, если НЕ равняеться то
# это False и мы получаем падения кода
