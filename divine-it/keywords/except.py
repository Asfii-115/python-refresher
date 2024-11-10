x = 'hello'
try:
    x>3
except NameError:
    print('you have a var not defined')
except TypeError:
    print('you are comparing values of diff type')            