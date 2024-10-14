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

# ------update()--------
# same as union()

set1.update(set5)
print(set1)

# -----------intersection---------
s1 = {"apple", "banana", "cherry"}
s2 = {"google", "microsoft", "apple"}
s3 = s1.intersection(s2)
print(s3)

s4 = s1 & s2  # same thing as intersection
print(s4)
# s1.intersection_update(s2)
print(s1)


# ------difference------
s5 = s1.difference(s2)
print(s5)
s6 = s1 - s2
print(s6)
# s1.difference_update(s2)
print(s1)
s7 = s1.symmetric_difference(s2)
print(s7)
s8 = s1 ^ s2
print(s8)
