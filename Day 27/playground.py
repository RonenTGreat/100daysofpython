def add(*args):
    add_num = 0
    for n in args:
        add_num += n
    print(add_num)


# add(3, 5, 6)

def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
