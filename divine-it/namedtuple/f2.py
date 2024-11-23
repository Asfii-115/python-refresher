# ------basic usage-------
from collections import namedtuple

point = namedtuple("Point", ["x", "y", "z"])

p1 = point(10, 20, 30)
p2 = point(x=11, y=22, z=33)
print(p1.x)
print(p1.y)
print(p1.z)
print(p2.z)
a, b, c = p1
print(a, b, c)
print(p1._fields)
p3 = point(1, 2, None)
p3 = p3._replace(z=3)
print(p3)

p3_dict = p3._asdict()
print(p3_dict)
