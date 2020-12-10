import commlibv as cl

c1 = cl.codeword([1,0,0,1,1])
c2 = cl.codeword([1,1,0,1,0])
c = c1 + c2
print(c1)
print(c2)
print(c)