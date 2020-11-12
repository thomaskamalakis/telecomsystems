import commlib as cl
import matplotlib.pyplot as plt

M = 16
Nbits = 32
TS = 1e-6

fmap = cl.pam_gray_forward_map(M)
bits = cl.random_bits(Nbits)
symbols, bitgroups = cl.bits_to_symbols(bits, fmap, return_bits = True)

print('Symbol mappings:')
print(fmap)
print('Input bits:')
print(bits)
print('Bit groups:')
print(bitgroups)
print('Encoded symbols:')
print(symbols)


t, x = cl.pam_waveform2(symbols, TS)
plt.close('all')
cl.plot_pam(t, x, M, bits, TS, dy = 1, plot_type = '-o')



