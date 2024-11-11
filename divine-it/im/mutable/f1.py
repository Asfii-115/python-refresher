x = 10
print(id(x))
x = x+1
print(id(x))
#mutable
#list,dict,set etc
list1 = [1,2,3]
print(id(list1))
list1.append(4)
print(id(list1))

def modify_list(lst):
    lst.append(4)   # Modifies the original list

def modify_string(s):
    s = s + " world"  # Creates a new string, doesn't modify the original

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

my_string = "hello"
modify_string(my_string)
print(my_string)  # Output: "hello" (unchanged)

"""this is multiline"""
