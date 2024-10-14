# ---------joining sets-----------
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set4 = set1 | set2  # same thing as using union
print(set4)

set5 = {"x", "y", "z"}

set6 = set1.union(set2, set5)
print(set6)
# you can do the same thing using | as well
# union is better to use as it can join different iterables

tuple1 = (4, 5, 6)
set7 = set2.union(tuple1)
print(set7)
