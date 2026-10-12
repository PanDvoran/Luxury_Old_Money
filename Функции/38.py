name = "Bob"


def func_1():
    def func_3():
        name = "Charlie"
        print("go, " + name)

    name = "Alice"
    print("Hello, " + name + "!")


def func_2():
    print("hi, " + name)


print(name + "!")
print(func_1())
func_2()
print("Bye, " + name)

