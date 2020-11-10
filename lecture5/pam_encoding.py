import commlib as cl

fmap = cl.pam_gray_forward_map(16)
bits = cl.random_bits(32)
symbols, bitgroups = cl.bits_to_symbols(bits, fmap, return_bits = True)

print('Symbol mappings:')
print(fmap)
print('Input bits:')
print(bits)
print('Bit groups:')
print(bitgroups)
print('Encoded symbols:')
print(symbols)


