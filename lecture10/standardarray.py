import commlib as cl
import numpy as np

a = cl.hamming_code( m = 3, compute_codewords = True )
a.build_standard_array()