add_ = lambda x: x + 15
mul_ = lambda x, y: x * y
print(add_(10))
print(mul_(10, 20))

subject_marks = [
    ("English", 88),
    ("Science", 90),
    ("Maths", 97),
    ("Social sciences", 82),
]

subject_marks.sort(key=lambda x: x[1])
print(subject_marks)

dict_ = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]
dict_.sort(key=lambda x: x["color"])
print(dict_)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([lambda arg=x: arg * arg for x in lst])
