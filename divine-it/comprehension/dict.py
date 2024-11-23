keys = [1, 2, 3, 4, 5]
values = ["a", "b", "c", "d", "e"]

mydict = {k: v for (k, v) in zip(keys, values)}

print(mydict)

# another way

m = dict(zip(keys, values))
print(m)


d = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(d)
