import numpy as np

l = [2,3,4,5]       # this is a Python list
print('Value of l:' , l)

x = np.array(l)      # cast the list to an array
print('Value of x:' , x)

e = enumerate(x)     # enumerate the numpy array x
el = list(e)         # this is now a list
print('Value of el:', el)

for i, v in enumerate(x):
    print('index = ',i,' value = ',v)
    
    