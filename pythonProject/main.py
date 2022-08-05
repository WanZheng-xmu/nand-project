import os
import numpy as np
import pandas as pd
import csv
import struct
import random

import matplotlib.pyplot as plt


path='E:/flash_testing/N48R/5Scan_OutPut/Result/defaultVthErrors.csv'
data=pd.read_csv(path)
#print(data.head(5))
#print(data.columns)
#print(data.shape)
#print(data.loc[7:10,["R1 (L0|L1)","R2 (L1|L2)"]])

to_path='E:/flash_testing/page_errors_pattern5.csv'
#pattern1在L9状态写入比较多
to_path1='E:/flash_testing/page_errors_pattern20.csv'
#pattern20在均衡写入


data['page1']=data['R5 (L4|L5)']+data['R10 (L9|L10)']+data['R12 (L11|L12)']+data['R15 (L14|L15)']
data['page2']=data['R1 (L0|L1)']+data['R4 (L3|L4)']+data['R6 (L5|L6)']+data['R11 (L10|L11)']
data['page3']=data['R3 (L2|L3)']+data['R7 (L6|L7)']+data['R9 (L8|L9)']+data['R13 (L12|L13)']
data['page4']=data['R2 (L1|L2)']+data['R8 (L7|L8)']+data['R14 (L13|L14)']
data['errors_sum']=data['page1']+data['page2']+data['page3']+data['page4']
data['page1_RBER']=data['page1']/147456
data['page2_RBER']=data['page2']/147456
data['page3_RBER']=data['page3']/147456
data['page4_RBER']=data['page4']/147456
data['WL_RBER']=data['errors_sum']/589824
#print(data)

data1=pd.DataFrame()
data1=data.loc[ : ,['page1','page2','page3','page4','errors_sum','page1_RBER','page2_RBER','page3_RBER','page4_RBER','WL_RBER']]

avg_page1=np.mean(data1.loc[:,'page1'])
data1.loc[0,'page1']=avg_page1

avg_page2=np.mean(data1.loc[:,'page2'])
data1.loc[0,'page2']=avg_page2

avg_page3=np.mean(data1.loc[:,'page3'])
data1.loc[0,'page3']=avg_page3

avg_page4=np.mean(data1.loc[:,'page4'])
data1.loc[0,'page4']=avg_page4

avg_page1_RBER=np.mean(data1.loc[:,'page1_RBER'])
data1.loc[0,'page1_RBER']=avg_page1_RBER

avg_page2_RBER=np.mean(data1.loc[:,'page2_RBER'])
data1.loc[0,'page2_RBER']=avg_page2_RBER

avg_page3_RBER=np.mean(data1.loc[:,'page3_RBER'])
data1.loc[0,'page3_RBER']=avg_page3_RBER

avg_page4_RBER=np.mean(data1.loc[:,'page4_RBER'])
data1.loc[0,'page4_RBER']=avg_page4_RBER

avg_errors_sum=np.mean(data1.loc[:,'errors_sum'])
data1.loc[0,'errors_sum']=avg_errors_sum

avg_WL_RBER=np.mean(data1.loc[:,'WL_RBER'])
data1.loc[0,'WL_RBER']=avg_WL_RBER


#data1=data1.append(col_mean,ignore_index=True)

data1.to_csv(to_path)
col_mean=data1.mean(axis=0)
print(col_mean)


data2=pd.read_csv(to_path1)
col_mean2=data2.mean(axis=0)
print(col_mean2)


'''
x=np.array(data.iloc[:,0])
y1=np.array(data1['page1'])
y2=np.array(data1['page2'])
y3=np.array(data1['page3'])
y4=np.array(data1['page4'])

plt.plot(x,y1,x,y2,x,y3,x,y4)
plt.title('page_errors')
plt.xlabel('WL')
plt.ylabel('errors_num')
plt.show()


'''
