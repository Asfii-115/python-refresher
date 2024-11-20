numbers = [1,2,3,4,5]
print(list(map(lambda x: x**2, numbers)))

words = ["hello", "world", "python"]
print(list(map(lambda x: x.upper(), words)))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list(map(lambda x,y: x+y, list1,list2)))

words = ["apple", "banana", "cherry"]
print(list(map(lambda x: len(x),words)))

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x:x*2 if x%2==0 else x,numbers)))

string_numbers = ["10", "20", "30", "40"]
print(sum(list(map(int,string_numbers))))

n = [1, 2, 3]
print(list(map(lambda x: (x*x,x*x*x), n)))

data = [{"name": "alice", "age": 25}, {"name": "bob", "age": 30}]
c = list(map(lambda x: x['name'].upper(), data))
print(c)
