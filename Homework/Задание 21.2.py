def correct_sentence(text):
    text = text[0].upper() + text[1:]
    if text[-1] != '.':
        text += "."
    return text



assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print(correct_sentence("greetings, friends."))
print(correct_sentence("hello"))
print(correct_sentence("Greetings. Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))

# У нас есть проверочное слово assert и функция с аргументом и идет проверк- условие == равнеться ли она этому тексту
# СТРОКА 1
# def correct_sentence(text): - мы создаем функцию с аргументом - переменной text у нас только 1 аргумент потому что
# нам нужно прокинуть везде только 1 аргумент str строка - текст. То есть в каждом assert есть своя функция где мы
# прокидуем один аргумент в виде строки - текста str поэтому и создаем функцию с 1 аргументом def correct_sentence(text)
# СТРОКА 2
# text = text[0].upper() + text[1:] - через print мы прокидываем из assert ТОЛЬКО функцию с аргументом str
# Этот аргумент str строка - текст подставляеться в функцию def correct_sentence(text) в аргумент функции в text
# аргумент - переменная text теперь имеет текст что мы прокинули, text = text[0].upper() + text[1:] тут
# у нас text[0] - это мы берем индекс 0 это первый символ текста и через метод .upper() делаем большую букву, теперь
# текст начиается с большой буквы и + text[1:] - мы к символу текста с Большой буквы добавляем все оставшиеся символы,
# весь оставшийся текст --- что переменная text теперь весь текст и первая буква(символ) текста с Большой буквы
#  СТРОКА 3 + 4
# if text[-1] != '.': - мы прокидываем в функцию аргумент str текст, а text[-1] берет последний символ текста и если
# последний символ НЕ точка то if text[-1] != '.' то наш последний символ НЕ равен точке тогда if будет True и сра-
# ботает подусловие  text += "." - к нашему тексту добавляеться точка
# СТРОКА 5
# return text - возвращает результат в print, где мы прокидывали через функцию аргумент
# +++ Если в тексте была точка то if будет False условие не выполняеться и return text пропускает if и возвращает толь-
# ко  изменения с text = text[0].upper() + text[1:]
# !!! ВАЖНО !!!
# Что б все коректно работало return должен быть на уровне функции. Если return будет в if то если мы прокидываем аргу-
# мент где текст с точкой . то if будет False он НЕ срабатывает, а в return вернеться None и расспечатаеться
#
#