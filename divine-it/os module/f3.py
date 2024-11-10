f = open('demofile.txt', 'a')
f.write('more content added to demo file')
f.close()

f = open('demofile.txt', 'r')
print(f.read())

f = open('demofile2.txt', 'w')
f.write('new file has been created')
f.close()
f = open('demofile2.txt')
print(f.read())

f = open('demofile3.txt', 'a')
f.write('this file will be deleted')
f.close()

f = open('demofile3.txt')
print(f.read())

import os
if os.path.exists('demofile3.txt'):
    os.remove('demofile3.txt')
else:
    print('this file does not exist')    