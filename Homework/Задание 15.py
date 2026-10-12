import string
import keyword

name = input("Введите название: ")
result = True

if name[0].isdigit():
    result = False

if not name.islower():
    result = False

for i in string.punctuation:
    if i in name and i != "_":
        result = False

if " " in name:
    result = False



if name in keyword.kwlist:
    result = False

if "__" in name:
    result = False


print(result)

# name = input("Введите название: ") - через input человек вводит название и оно содержиться в переменной name
# if name[0].isdigit(): - если наше название первый символ цифры то выполняеться подусловие result = False
# if not name.islower(): - если наше название НЕ с маленьких букв, а значит с больших, выполняет подусл result = False
# for i in string.punctuation: - в i поочерди подставляеться каждый знак пунктуации эти знаки беруться со
# string.punctuation(ящик в котором лежат все знаки пунктуации) для этого используем библиотеку string что бы выполнить
# проверку на punctuation
# if i in name and i != "_": - if i in name - проверяет присутствует ли знак пунктуации в нашем названии,
# i != "_" проверяет и говорит что все знаки пунктуации кроме _(нижнего подчеркивания) запрещены, если у нас в названии
# будут любые знаки кроме _(нижнего подчеркивания), условие if выполняеться и по коду получаем result = False
# if name in keyword.kwlist: - если наше название имеет зарегестрированое слово, условие выполняеться и по коду полусим
# result = False
# if "__" in name: - если в нашем названии два __(нижних подчеркивания) то условие выпол, по коду получим result = False
# мы пишем после каждого if в середине него result = False, а НЕ print(result) - потому что если к примеру название 3m?
# у нас будет несколько print False то один if напечатает False из-за цифры 3 , а второй if напечатает False из-за ?
