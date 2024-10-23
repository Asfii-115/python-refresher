x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))


def my_func(n):
    return lambda a: a * n


my = my_func(2)
print(my(5))
