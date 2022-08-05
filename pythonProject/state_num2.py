import os
import numpy as np
import csv
import struct
import random

#统计各个状态的数量

pagesize = 18432 # byte
pagenum = 1152
WLnum = 384
pagenum = 4224
WLnum = 1408

# from state value to separate byte in each page
# 8 state values to form 1 byte for each page (total 3 bytes)
def form_byte(v):
    r = np.zeros(3)
    p = 7
    for k in range(8):
        t = v[k]
        for i in range(3):
            b = t % 2
            t = t // 2
            r[2-i] = r[2-i] + b * pow(2, p)
        p = p - 1

    return r

# from 3 bytes to form 8 states
def form_state(L, C, M):
    s = np.zeros(8)
    for i in range(8):
        l = L & pow(2, 7 - i)
        l = l >> (7 - i)

        c = C & pow(2, 7 - i)
        c = c >> (7 - i)

        m = M & pow(2, 7 - i)
        m = m >> (7 - i)

        s[i] = l * 4 + c * 2 + m

    return s


def read_oneWL(file, pagesize):
    LSB = file.read(pagesize)
    CSB = file.read(pagesize)
    MSB = file.read(pagesize)
    ret = np.zeros(pagesize*8)
    for j in range(pagesize):
        # print(LSB[j], CSB[j], MSB[j])
        ret[j*8:j*8+8] = form_state(LSB[j], CSB[j], MSB[j])
    return ret



path='F:\\GitRepos\\imba_storage\\workloads\\models\\kaggle-wikipedia-sentences.bin-mapped.bin'
statenum_file = open(path, 'rb')
state=np.zeros(8)
for i in range(WLnum):
    a=read_oneWL(statenum_file,pagesize)
    print(i)
    for j in range(pagesize*8):
        if a[j]==0:
            state[0]=state[0]+1
        if a[j] == 1:
            state[1] = state[1]+1
        if a[j]==2:
            state[2]=state[2]+1
        if a[j]==3:
            state[3]=state[3]+1
        if a[j]==4:
            state[4]=state[4]+1
        if a[j]==5:
            state[5]=state[5]+1
        if a[j]==6:
            state[6]=state[6]+1
        if a[j]==7:
            state[7]=state[7]+1
print(state)

