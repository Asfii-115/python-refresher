txt = ",,best things, in life, are free"
# print("free" in txt)  # true
# print("expensive" not in txt)  # true
# print("expensive" in txt)  # false

# txt = "best things in life are free"
# if "free" in txt:
#     print("yes, free is in txt")

# ---------Slicing---------
# print(txt[4:10])
# print(txt[4:])  # from 4 to end
# print(txt[:5])  # from start to five
# print(txt[:])  # whole thing
# print(txt[:-5])
# print(txt[-13:-4])


# ----------Modify------------
# print(txt.upper())
print(txt.lower())
# print(txt.strip())  # removes whitespace
# print(txt.replace("f", "p"))
# # split() returns a list by separator
# print(txt.split(","))
# print(txt.capitalize())
# a = ["text", "photo", "bio", "ziaul"]
# b = [2, 5, 1, 3, 7]
# a.sort()
# a.reverse()
# b.sort(reverse=True)
# print(a)
# print(b)
print(txt.center(24))
print(txt.casefold())
print(txt.count("e"))
print(txt.count("e", 10, 30))  # specifying checking length
print(txt.find("free"))
print(txt.index("free"))
print(txt.islower())
print(txt.isupper())
# print(" ".join(a))
print(txt.title())  # converts the first character of each word
print(txt.swapcase())
print(txt.strip(","))

# --------concatanate---------
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# -------formatting----------
# age = 24
# new_txt = f"My name is Asfi and I am {age} years old"
# new_txt2 = f"My name is Asfi and I am {4*4} years old"
# print(new_txt)
# print(new_txt2)

# -----------Escape characters---------

name = 'We are the so-called "Vikings" from the north.'
print(name)
