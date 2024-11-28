import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)
print(x)

y = re.findall("ai", txt)
print(len(y))

o = re.search('^The',txt)
print(o)

p = re.sub('\s','9',txt)
print(p)

q = re.search('ai',txt)
print(q)
print(q.span())
print(q.string)

#-----p1
text = "There are 3 cats, 4 dogs, and 5 birds."
z = re.findall('[0-9]',text)
print(z)

#-----p2
text2 = "Bob bought bananas and blueberries."
c = re.findall('[b]',text2)
print(c)