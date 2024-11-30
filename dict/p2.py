def dict_sum(d):
    sum_d = 0
    for value in d:
        sum_d += d[value]
    return sum_d


print(dict_sum({"a": 10, "b": 20, "c": 30}))


def find_key(d, val):
    for key, value in d.items():
        if value == val:
            return key


print(find_key({"x": 10, "y": 20, "z": 30}, 30))


def add(d, k, v):
    d.update({k: v})
    return d


print(add({"a": 10, "b": 20, "c": 30, "d": 40}, "e", 50))


def merge(d1, d2):
    d1.update(d2)
    return d1


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(merge(dict1, dict2))


def merge_op(d1, d2):
    return d1 | d2


print(merge_op(dict1, dict2))


def merge_loop(d1, d2):
    for key, value in d2.items():
        d1[key] = value
    return d1


print(merge_loop(dict1, dict2))


def max_key(d):
    max_v = 0
    max_k = ""
    for key, value in d.items():
        if value > max_v:
            max_v = value
            max_k = key
    return max_k


print(max_key({"x": 10, "y": 25, "z": 15}))


def max_key_another(d):
    max_value = max(d.values())
    return [key for key, value in d.items() if value == max_value][-1]


print(max_key_another({"x": 10, "y": 25, "z": 15}))


def filter_items(d, fv):
    filtered = {}
    for key, value in d.items():
        if value > fv:
            filtered[key] = value
            # filtered.update({key: value})
    return filtered


print(filter_items({"a": 10, "b": 20, "c": 30}, 15))


def reverse_dict(d):
    rev_d = {}
    for key, value in d.items():
        rev_d[value] = key
    return rev_d


print(reverse_dict({"a": 1, "b": 2, "c": 3}))

from collections import OrderedDict


def key_reverse(d):
    res = OrderedDict(reversed(list(d.items())))
    return dict(reversed(list(d.items())))


print(key_reverse({"a": 1, "b": 2, "c": 3}))


from collections import defaultdict


def group_key(d):
    group_values = defaultdict(list)
    for dictionary in d:
        for key, value in dictionary.items():
            group_values[key].append(value)
    group_values = dict(group_values)
    return group_values


print(group_key([{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]))


students = {
    "Alice": {"math": 80, "science": 90},
    "Bob": {"math": 70, "science": 85},
    "Charlie": {"math": 60, "science": 75},
}

for key, value in students.items():
    value["math"] += 10
print(students)
