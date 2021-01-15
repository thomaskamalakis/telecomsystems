import commlib as cl
c = cl.lzwcompressor()
filenames = ['across-the-universe.txt', 'all-my-loving.txt']
for filename in filenames:
    c.read_from_file(filename)
    c.compress()
    print(c.bin_msg)
    print('Compression ratio for %s : %6.2f' %(filename, c.compression_level()))

