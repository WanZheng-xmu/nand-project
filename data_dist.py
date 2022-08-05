import os
import numpy as np
import csv
import struct
import random
import matplotlib.pyplot as plt
# import seaborn as sns



pagesize = 18432 # byte
pagenum = 1152
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

def read_dist_file(fname):
    with open(fname) as f:
        f_csv = csv.reader(f)
        ret1 = []
        ret2 = []
        for row in f_csv:
            ret1.append(int(float(row[0])))
            ret2.append(int(float(row[1])))
    return ret1, ret2


def count_three(x, y, k, key): # count the percentage of key
    ret = 0
    for i in range(y.shape[0]):
        c = 0
        tmp = x[i]
        for j in range(k+1):
            cha = tmp // pow(10, k-j)
            tmp = tmp % pow(10, k-j)
            c = c + (cha == key)
        # print(c)
        ret = ret + c * y[i]
    return ret



def state_dist(x, y, k):
    ret = np.zeros(y.shape[0] * (k + 1))
    idx = 0
    for i in range(y.shape[0]):
        tmp = x[i]
        for j in range(k + 1):
            cha = tmp // pow(10, k - j)
            tmp = tmp % pow(10, k - j)
            ret[idx] = cha
            idx = idx + 1
    return ret



path='F:\\flash_testing\\3DV7source_files\\pattern4'
fromfile= open(path, 'rb')

state_all = []
for i in range(WLnum):
    LSB = fromfile.read(pagesize)
    CSB = fromfile.read(pagesize)
    MSB = fromfile.read(pagesize)
    for j in range(pagesize):
        state_all.append(form_state(LSB[j], CSB[j], MSB[j]))

length = state_all.__len__()
print(length)
# print(state_all)
state_all = np.array(state_all)
state_all = np.reshape(state_all, -1)
state_all = state_all.tolist()
# dic = {k:state_all.count(k) for k in set(state_all)}
# print(dic)
fromname='F:\\third'
dist =[]
for k in set(state_all):
    x = state_all.count(k)
    dist.append([k, x])
dist = np.array(dist)
with open(fromname+'_one_chara.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(dist.shape[0]):
        employee_writer.writerow(dist[i])

state_all2 = []
for i in range(length//2):
    state_all2.append(state_all[i*2]*10+state_all[i*2+1])
# dic2 = {k:state_all2.count(k) for k in set(state_all2)}
# print(dic2)
dist =[]
for k in set(state_all2):
    x = state_all2.count(k)
    dist.append([k, x])
dist = np.array(dist)
with open(fromname+'_two_chara.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(dist.shape[0]):
        employee_writer.writerow(dist[i])
'''
state_all3 = []
for i in range(length//3):
    state_all3.append(state_all[i*3]*100+state_all[i*3+1]*10+state_all[i*3+2])
# dic3 = {k:state_all3.count(k) for k in set(state_all3)}
# print(dic3)
dist =[]
for k in set(state_all3):
    x = state_all3.count(k)
    dist.append([k, x])
dist = np.array(dist)
with open(fromname+'_three_chara.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(dist.shape[0]):
        employee_writer.writerow(dist[i])
'''

state_all4 = []
for i in range(length//4):
    state_all4.append(state_all[i*4]*1000+state_all[i*4+1]*100+state_all[i*4+2]*10+state_all[i*4+3])
# dic4 = {k:state_all4.count(k) for k in set(state_all4)}
# print(dic4)
dist =[]
for k in set(state_all4):
    x = state_all4.count(k)
    dist.append([k, x])
dist = np.array(dist)
with open(fromname+'_four_chara.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(dist.shape[0]):
        employee_writer.writerow(dist[i])

# sns.distplot(state_all, hist=False, kde_kws={"color":"red","linestyle":"-"}, norm_hist=True, label="original") 
# sns.distplot(state_all2, hist=False, kde_kws={"color":"blue","linestyle":"--"}, norm_hist=True, label="output") 

exit(0)

'''
state = [7, 6, 4, 0, 2, 3, 1, 5]

h_state = [0, 0, 0, 0]
toname = 'pattern1'

tofile = open(toname, 'wb')

for k in range(WLnum):
    page_content = np.zeros((3, pagesize))

    for i in range(pagesize):
        v = np.zeros(8)
        for j in range(8):
            flag = random.randint(0, 1)
            flag = 0
            if flag == 0:
                ind = random.randint(0, 7)
                v[j] = state[ind]
            else:
                ind = random.randint(0, 3)
                v[j] = h_state[ind]
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
'''
