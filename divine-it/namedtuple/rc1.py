from collections import namedtuple

Student = namedtuple('Student',['name','age','by'])

s = Student('xai',24,2000)

print(s.name)
print(s.by)