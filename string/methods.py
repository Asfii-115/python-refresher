# -------lower strings--------#

txt = "My Name Is ASFI"
print(txt.casefold())
# casefold considered better than lower()


# ------finding index--------
txt2 = "asfi1i"
print(txt2.find("d"))  # return -1 when not finding unlike index()

print(txt2.index("i"))
print(txt2.rindex("i"))  # finds index from reverse
print(txt2.rfind("i"))


# ------alphabet checking------

print(txt2.isalpha())
print(txt2.isalnum())


# ------join-------

txt3 = "hello world, my name is asfi"
print("#".join(txt3.split()))

# ---------makestrans-------


x = str.maketrans("o", "o", "a")
print(txt3.translate(x))
