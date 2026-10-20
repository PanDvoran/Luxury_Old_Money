def second_index(text, some_str):
    first = text.find(some_str)
    second = text.find(some_str, first + 1)

    if second == -1:
        return None

    return second

print(second_index("sims", "s"))
