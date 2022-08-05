import os
import numpy as np
import pandas as pd
import csv
import struct
import random
import matplotlib.pyplot as plt

#电压偏移量
path1='F:/flash_testing/N48R/20Scan_OutPut/VthList/WL0068Frame00V.csv'
Vth_avg_diff=pd.read_csv(path1)




to_path='F:/flash_testing/pretest/Vth_avg_pattern20.csv'


#求16个状态中每个状态的电压平均值
'''

data=pd.DataFrame()
for i in range(1,17):
    x = np.array(Vth_avg_diff.iloc[:, 0] * Vth_avg_diff.iloc[:,i])
    sum_num=sum(Vth_avg_diff.iloc[:,i])
    sum_Vth=sum(x)
    avg_sum = sum_Vth / sum_num
    a=str(i)
    data.loc[0,'state'+a]=avg_sum


#求每个pattern的16个状态的电压值与even写入的电压值的差值--查看电压偏移值
for i in range(1,17):
    a = str(i)
    m=data.loc[0,'state'+a]
    n=even_write.loc[0,'state'+a]
    diff=m-n
    diff1=round(diff,10)
    data.loc[1,'state'+a]=diff1

print(data)

data.to_csv(to_path)
'''
#求even的电压平均值

data_even=pd.DataFrame()
for i in range(1,17):
    x = np.array(Vth_avg_diff.iloc[:, 0] * Vth_avg_diff.iloc[:,i])
    sum_num=sum(Vth_avg_diff.iloc[:,i])
    sum_Vth=sum(x)
    avg_sum = sum_Vth / sum_num
    a=str(i)
    data_even.loc[0,'state'+a]=avg_sum
data_even.to_csv(to_path)

path='F:/flash_testing/pretest/Vth_avg_pattern20.csv'
even_write=pd.read_csv(path)

#求每个pattern的16个状态的电压值与even写入的电压值的差值--查看电压偏移值
for i in range(1,17):
    a = str(i)
    m=data_even.loc[0,'state'+a]
    n=even_write.loc[0,'state'+a]
    diff=m-n
    diff1=round(diff,10)
    data_even.loc[1,'state'+a]=diff1

data_even.to_csv(to_path)




#求其他的电压平均值和偏移值

data1=pd.DataFrame(np.random.randn(6, 16))
for i in range(6):
    path='F:/flash_testing/N48R/'+str(i)+'Scan_OutPut/VthList/WL0068Frame00V.csv'
    to_path = 'F:/flash_testing/pretest/Vth_avg_pattern'+str(i)+'.csv'
    Vth_avg_diff = pd.read_csv(path)

    data=pd.DataFrame()
    for j in range(1,17):
        x = np.array(Vth_avg_diff.iloc[:, 0] * Vth_avg_diff.iloc[:, j])
        sum_num = sum(Vth_avg_diff.iloc[:, j])
        sum_Vth = sum(x)
        avg_sum = sum_Vth / sum_num
        a = str(j)
        data.loc[0, 'state' + a] = avg_sum

    for z in range(1,17):
        a = str(z)
        m = data.loc[0, 'state' + a]
        n = even_write.loc[0, 'state' + a]
        diff = m - n
        diff1 = round(diff, 10)
        data.loc[1, 'state' + a] = diff1
        data1.iloc[i,z-1]=diff1

    data.to_csv(to_path)

path_all='F:/flash_testing/pretest/Vth_avg_all.csv'
data1.to_csv(path_all)






'''
x1=np.array(WL0587.iloc[:,0])
y1=np.array(WL0587.loc[:,'L0':'L15'])
x2=np.array(WL0068.iloc[:,0])
y2=np.array(WL0068.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]])
print(y1)

plt.plot(x1,y1,color='red')
plt.plot(x2,y2,color='blue')
plt.title('VthList')
plt.xlabel('Vth')
plt.ylabel('num')
plt.show()
'''
