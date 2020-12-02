import commlib as cl
import numpy as np

P = np.array([[1, 0],
              [0, 1],
              [0, 0]])

a = cl.systematic_code( P = P )
