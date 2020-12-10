import commlib as cl
import numpy as np

a = cl.hamming_code( m = 3, compute_codewords = True )
#
print('Generator matrix:')
print(a.G)
print('\nParity check matrix:')
print(a.H)
print('\nParity check matrix transpose:')
print(a.Ht)
print('\n Matrix product:')
print(cl.multiply_modulo2(a.G, a.Ht))
print('\n Codewords:')
print(a.cw)
print('\n message mapping')
a.print()