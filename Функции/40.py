def func(**kwargs):
    print("a:", kwargs["a"])
    print("b:", kwargs["b"])
    print("c:", kwargs["c"])
    print("--------")


d = {"b": 1, "a": 2, "c": 3}

func(**d)