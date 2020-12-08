import commlib as cl
import numpy as np

P = np.array([[1, 0],
              [0, 1],
              [0, 0]])

a = cl.systematic_code( P = P )

print('Generator matrix:')
print(a.G)
print('\nParity check matrix:')
print(a.H)
print('\nParity check matrix transpose:')
print(a.Ht)
print('\n Matrix product:')
print(cl.multiply_modulo2(a.G, a.Ht))

