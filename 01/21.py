a = 100

if a > 0:
    result = a / 2
else:
    result = abs(a)

print(result)

# Выше пример сравнения обычный, а ниже тот же пример но записаный в Тернарном виразі
result = a / 2 if a > 0 else abs(a)
print(result)
