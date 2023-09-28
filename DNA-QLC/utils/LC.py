"""

This module is for error correction
"""


import math
import numpy as np

def encode_lc(origin):
    len_org = len(origin)
    len_enc = len_org
    while(len_org > len_enc - math.ceil(np.log2(len_enc))-1):
        len_enc = len_enc + 1
    ind = []
    for i in range(len_enc-1):
        if np.log2(i+1) - int(np.log2(i+1)) != 0:
            ind.append(i+1)
    pla_1 = np.dot(ind,origin)
    rem = 2*len_enc - pla_1 % (2*len_enc)
    if rem > 2**(math.ceil(np.log2(len_enc))) - 1:
        rem = rem - len_enc
        bina = bin(rem)
        par = []
        for i in range(2,len(bina)):
            par.append(int(bina[i]))
        loc = 0
        for i in range(len_enc - 1):
            if np.log2(i + 1) - int(np.log2(i + 1)) == 0:
                loc += 1
                if loc <= len(par):
                    origin.insert(i, par[-loc])
                else:
                    origin.insert(i, 0)
        origin.insert(len_enc, 1)
    else:
        bina = bin(rem)
        par = []
        for i in range(2,len(bina)):
            par.append(int(bina[i]))
        loc = 0
        for i in range(len_enc - 1):
            if np.log2(i + 1) - int(np.log2(i + 1)) == 0:
                loc += 1
                if loc <= len(par):
                    origin.insert(i, par[-loc])
                else:
                    origin.insert(i, 0)
        origin.insert(len_enc, 0)

    return origin