import random

a = []

for i in range(random.randint(3, 10)):
    a.append(random.randint(1, 10))

b = [a[0], a[2], a[-2]]

print(a)
print(b)