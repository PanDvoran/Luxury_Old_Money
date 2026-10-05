number = 0

while number < 10:
    number = number + 1
    if number == 5:
        continue
    print(number)

# number = 0
# while number < 10: условие до которого числа цикл
# number = number + 1 - это подусловие while в к каждому number + 1 в каждом цикле
# if number == 5: если наш number стал 5(после 4 цикла) то это условие True и срабатывает continue
# наш цикл 5 пропускается(за счет continue)
# В Терминале: мы получим ответ number по каждому цикул( от до 10, кроме 5, потому что 5 цикл пропускается)