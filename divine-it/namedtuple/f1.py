from collections import namedtuple

point = namedtuple('point', 'x y')
p1 = point(2,3)
print(p1.x)
print(p1.y)

car = namedtuple('car', 'make model year')
my_car = car(make='tesla', model='x', year='2020')
print(my_car.make)
print(my_car.model)
print(my_car.year)

car_dict = my_car._asdict()
print(car_dict)

updated_car = my_car._replace(model = 'y')
print(updated_car)

def accum(st):
    s = ''
    li = []
    for x in range(len(st)):
        s= st[x] * (x+1)
        li.append(s)
    return '-'.join(li).title()

print(accum('abcd'))

def DNA_strand(dna):
    # code here
    pairs = {'A':'T','T':'A', 'G':'C', 'C':'G'}
    return ''.join(pairs[x] for x in dna)
print(DNA_strand('ATTGC'))
        
        