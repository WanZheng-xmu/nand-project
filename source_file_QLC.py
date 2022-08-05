import os
import numpy as np
import csv
import struct
import random

pagesize = 18432 # byte
pagenum = 1152
pagenum = 4224
WLnum = 384
WLnum = 704

father_path = 'E:/pattern/'
# from state value to separate byte in each page
# 8 state values to form 1 byte for each page (total 4 bytes)
def form_byte(v):
    r = np.zeros(4)
    p = 7
    for k in range(8):
        t = v[k]
        for i in range(4):
            b = t % 2
            t = t // 2
            r[2-i] = r[2-i] + b * pow(2, p)
        p = p - 1

    return r
'''
fromname = 'F:/temperature_test_2020/data/3DV5/unbalanced/source_files/pattern16'
fromname = father_path + 'pattern0'
# fromname = 'pattern18'
# print(fromname)
fromname = 'E:/flash_testing/N48R/16Scan/0'
fromfile = open(fromname, 'rb')
for i in range(10):
    data = fromfile.read(1)
    num = struct.unpack('B', data)
    print(i, data, num)

exit(0)
'''

state = [15,11,10,8,12,4,0,2,3,1,9,13,5,7,6,14]  # N48R

levl = 30
h_state = [15, 1, 6, 12]
toname = father_path + 'pattern' + str(levl)
# toname = father_path + 'pattern19'
tofile = open(toname, 'wb')


for k in range(WLnum):
    page_content = np.zeros((4, pagesize))

    for i in range(pagesize):
        v = np.zeros(8)
        for j in range(8):
            flag = random.randint(0, 7)
            #flag = 1
            if flag == 0:
                #ind = levl - 1
                v[j] = state[1]
                #v[j] = 15

                #ind = random.randint(0, 3)
                #v[j] = h_state[ind]
            else:
                ind = random.randint(0, 15)
                v[j] = state[ind]

                # flag2 = random.randint(0, 1)
                # v[j] = h_state[flag2]

                # if k % 2 == 0:  # WLs with odd index and even index have different states
                #     v[j] = h_state[ind]
                # else:
                #     v[j] = h_state2[ind]
        page_content[:, i] = form_byte(v)

    for i in range(4):
        for j in range(pagesize):
            x = int(page_content[i, j])
            data = x.to_bytes(1, 'big')
            tofile.write(data)

    # print(page_content)
    print(page_content.shape)

tofile.close()
exit(0)

