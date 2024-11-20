numbers = [1, 2, 3, 4, 5,6]
x = list(map(lambda x: x*2,numbers))
print(x)

y = list(filter(lambda x: x%2==0,numbers))
print(y)

data = [(1, 3), (4, 1), (2, 2)]
print(sorted(data,key=lambda x: x[1]))

words = ["radar", "python", "level", "world"]
print(list(map(lambda x: x==x[::-1],words)))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print(list(map(lambda x,y,z: x+y+z,list1,list2,list3)))