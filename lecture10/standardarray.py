import commlib as cl



a = cl.hamming_code( m = 3, compute_codewords = True )
a.build_standard_array()
a.print_standard_array()
print(a.syndromes)