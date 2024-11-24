# # try:
# #     x = 10 / 0
# # except ZeroDivisionError:
# #     print("can not divide by zero")

# try:
#     lst = [1, 2, 3, 4, 5]
#     print(lst[7])
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except IndexError:
#     print("index out of range")


# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Division successful:", x)

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Can not divide by zero")
finally:
    print("execution complete")


def check_positive(n):
    if n < 0:
        raise ValueError("must be positive number")
    return n


try:
    check_positive(-5)
except ValueError as e:
    print(e)

try:
    x = int("invalid")
except Exception as e:
    print(f"An error occurred {e}")


class MyCustomError(Exception):
    pass


try:
    raise MyCustomError("This is a custom error.")
except MyCustomError as e:
    print(e)
