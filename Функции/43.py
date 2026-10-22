def func(a,b):
    res = (a + b)**2
    yield res
    res += 45
    yield res
    res += 100
    yield res




print(list(func(10,20)))

