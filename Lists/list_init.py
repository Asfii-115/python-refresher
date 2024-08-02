# list() to make a list
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "mango"
# print(thislist)

newlist = ["apple", "banana", "cherry", "mango", "lemon"]
newlist[1:3] = ["blackcurrant", "watermelon"]
print(newlist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist.insert(2, "pineapple")
print(thislist)
