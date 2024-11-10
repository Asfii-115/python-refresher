# def cube(y):
#     return y*y*y

 
# lambda_cube = lambda y: y*y*y
# print(cube(5))
# print(lambda_cube(5)) 


r = [lambda arg=x: arg*10 for x in range(1,5)]
for i in r:
    print(i())
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())


max = lambda a,b: a if (a>b) else b
print(max(1,2))    