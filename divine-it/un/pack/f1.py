# ------unpacking-----


def fun(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4]

fun(*my_list)

# --------packing------
# when no of  args in unknown
def fun2(*args):
    return sum(args)


print(fun2(2, 3, 4, 5, 6, 7, 8))
