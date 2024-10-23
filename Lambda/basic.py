numbers = [1, 2, 3, 4, 5, 6]

sn = list(map(lambda a: a * a, numbers))
print(sn)

print(list(map(str, numbers)))

even_ = list(filter(lambda a: a % 2 == 0, numbers))
print(even_)

from functools import reduce

print(reduce(lambda x, y: x * y, numbers))

tuples = [(1, 3), (2, 1), (4, 2)]
print(sorted(tuples, key=lambda x: x[1]))

factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
print(factorial(5))

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
print(sorted(people, key=lambda x: x["age"]))
