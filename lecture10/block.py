import commlib as cl
import numpy as np

P = np.array([[1, 0],
              [0, 1],
              [0, 0]])

a = cl.systematic_code( P = P )
print('Code words:')
a.print()
a.calc_distances()
a.calc_weights()
print('\nDistances:')
print(a.distances)
print('\nWeights:')
print(a.weights)