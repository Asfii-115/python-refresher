f = open('demofile.txt')
print(f.read())
print(f.readline())
for x in f:
    print(f)
f.close()    