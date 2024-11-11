def mn(n):
    return n*3

giv = map(mn, [1,2,3])
print([x for x in giv])

#------filter----
def voting_age(age):
    if age>18:
        return age

lst = [18,19,17,15,20,23]
x = filter(voting_age, lst)
print([y for y in x]) 

#----reduce----
from functools import reduce
def add_no(x,y):
    return x+y
lst2 = [2,3,4,5,6]
t = reduce(add_no,lst2)
print(t) #reduce returns a single value