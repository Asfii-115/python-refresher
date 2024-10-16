thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict  # ref not a copy
print(mydict)

mydict1 = thisdict.copy()  # or using dict()
print(mydict1)
