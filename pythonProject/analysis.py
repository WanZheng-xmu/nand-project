import numpy as np
import pandas as pd


path='F:/flash_testing/3DV7/3DV7118_OutPut/Result/defaultVthErrors.csv'
#data=pd.read_csv(path)

to_path='F:/flash_testing/data_figure/page_errors_118.csv'

data2 = pd.DataFrame(np.random.randn(25, 3))

#求直方图，即每个页的错误平均值
for i in range(25):
    path='F:/flash_testing/fourth_threekao/3DV7'+str(i+119)+'_OutPut/Result/defaultVthErrors.csv'
    #to_path = 'F:/flash_testing/data_figure/page_errors_'+str(i+105)+'.csv'
    data = pd.read_csv(path)
    data['page1'] = data['R3 (L2|L3)'] + data['R7 (L6|L7)']
    data['page2'] = data['R2 (L1|L2)'] + data['R4 (L3|L4)'] + data['R6 (L5|L6)']
    data['page3'] = data['R1 (L0|L1)'] + data['R5 (L4|L5)']

    data1 = pd.DataFrame()
    data1 = data.loc[:, ['page1', 'page2', 'page3']]


    avg_page1 = np.mean(data1.loc[:, 'page1'])
    data1.loc[0, 'page1_avg'] = avg_page1
    data2.iloc[i,0]=avg_page1

    avg_page2 = np.mean(data1.loc[:, 'page2'])
    data1.loc[0, 'page2_avg'] = avg_page2
    data2.iloc[i,1] = avg_page2

    avg_page3 = np.mean(data1.loc[:, 'page3'])
    data1.loc[0, 'page3_avg'] = avg_page3
    data2.iloc[i,2] = avg_page3

    #print(data1)
    #data1.to_csv(to_path)

to_path1='F:/flash_testing/fourth_threekao/page_errors_avg.csv'
data2.to_csv(to_path1)





