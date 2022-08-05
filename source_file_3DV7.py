import os
import numpy as np
import csv
import struct
import random

pagesize = 18432 # byte
pagenum = 1152
pagenum = 4224
WLnum = 384
WLnum = 1408

father_path = 'E:/flash_testing/3DV7/source_files/new/'
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


def read_oneWL(file, pagesize):  # to find the state values: 7, 6, 4, 0, 2, 3, 1, 5 or others
    LSB = file.read(pagesize)
    CSB = file.read(pagesize)
    MSB = file.read(pagesize)
    ret = np.zeros(pagesize*8)
    for j in range(pagesize):
        # print(LSB[j], CSB[j], MSB[j])
        ret[j*8:j*8+8] = form_state(LSB[j], CSB[j], MSB[j])
    return ret.tolist()

src_name = 'E:/flash_testing/3DV5/source_files/new/pattern8'
src_name = 'E:/flash_testing/3DV7/New_coding4/0/71/-62'
src_file = open(src_name, 'rb')
src = read_oneWL(src_file, pagesize)
a = set(src)
for i in a:
    print(i, src.count(i))
exit(0)



# fromname = 'F:/temperature_test_2020/data/3DV5/unbalanced/source_files/pattern16'
# fromname = 'pattern18'
# print(fromname)
# fromfile = open(fromname, 'rb')
# for i in range(10):
#     data = fromfile.read(1)
#     num = struct.unpack('B', data)
#     print(i, data, num)
#
# exit(0)

state = [7, 6, 4, 0, 2, 3, 1, 5]  # 3DV7, 3DV5
levl = 10
hh = [[0,1],
      [1,2],
      [2,3],
      [3,4],
      [4,5],
      [5,6],
      [6,7],
      [0,7],
      [1,6],
      [2,5],
      [0,3],
      [1,4],
      [3,5],
      [4,6],
      [2,4],
      ]
hh = np.array(hh)
for k in range(9, 24):
    h_state = hh[k-9, :]
    # toname = father_path + 'pattern' + str(levl)
    toname = father_path + 'pattern' + str(k)
    print(h_state)
    print(toname)
    tofile = open(toname, 'wb')

    for k in range(WLnum):
        page_content = np.zeros((3, pagesize))

        for i in range(pagesize):
            v = np.zeros(8)
            for j in range(8):
                flag = random.randint(0, 1)
                # flag = 0
                if flag == 0:
                    ind = random.randint(0, 7)
                    v[j] = state[ind]
                else:
                    # ind = levl - 1
                    # v[j] = state[ind]

                    flag2 = random.randint(0, 1)
                    v[j] = state[h_state[flag2]]

                    # if k % 2 == 0:  # WLs with odd index and even index have different states
                    #     v[j] = h_state[ind]
                    # else:
                    #     v[j] = h_state2[ind]
            page_content[:, i] = form_byte(v)

        for i in range(3):
            for j in range(pagesize):
                x = int(page_content[i, j])
                data = x.to_bytes(1, 'big')
                tofile.write(data)

        # print(page_content)
        print(page_content.shape)

    tofile.close()

exit(0)


fromname = 'source'
print(fromname)
fromfile = open(fromname, 'rb')

toname = 'out_CSB_half'
tofile = open(toname, 'wb')


for i in range(384):
    for j in range(i*3*pagesize, (i*3+1)*pagesize):
        data = fromfile.read(1)
        tofile.write(data)
    for j in range((i*3+1)*pagesize, (i*3+2)*pagesize):
        data = fromfile.read(1)
        if j%2 == 0:
            a = 0
            data = a.to_bytes(1, 'big')
        tofile.write(data)

    for j in range((i*3+2)*pagesize, (i*3+3)*pagesize):
        data = fromfile.read(1)
        tofile.write(data)

fromfile.close()
tofile.close()


exit(0)


fromname = 'source'
print(fromname)
fromfile = open(fromname, 'rb')
for i in range(10):
    data = fromfile.read(1)
    num = struct.unpack('B', data)
    print(i, data, num)

toname = 'out'
tofile = open(toname, 'wb')
for i in range(10):
    data = 255
    content = data.to_bytes(1, 'big')
    tofile.write(content)



fromfile.close()
tofile.close()







fromname = 'out'
print(fromname)
fromfile = open(fromname, 'rb')
for i in range(10):
    data = fromfile.read(1)
    num = struct.unpack('B', data)
    print(i, data, num)

