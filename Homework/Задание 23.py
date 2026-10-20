def common_elements():
    a = {i for i in range(100) if i % 3 == 0}
    b = {i for i in range(100) if i % 5 == 0}

    return a.intersection(b)

print(common_elements())