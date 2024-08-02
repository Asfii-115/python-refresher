# adding an item at the end
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
tropical = ("mango", "pineapple", "papaya")  # tuple

thislist.extend(tropical)
print(thislist)
# this extend keywoed works you any iterable
