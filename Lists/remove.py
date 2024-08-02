# remove() removes any specied items in the list
thislist = ["a", "b", "c", "d", "a"]
thislist.remove("a")
print(thislist)
# only reomves the first occurrence

# use pop() for indexing remove
thislist.pop(-1)
print(thislist)

# using del
del thislist[1]
print(thislist)

# use del to completely delete the list
# del thislist

# clear() empties the list
thislist.clear()
print(thislist)
