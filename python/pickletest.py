import pickle
d = {'a': 1, 'b': 2, 'c': 3}
f = open('pickle.sv', 'wb')
pickle.dump(d, f)
