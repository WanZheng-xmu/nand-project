import numpy as np
import pandas as pd


#箱线图
data1=pd.DataFrame()
for i in range(14):
    path='F:\\flash_testing\\data_figure\\page_errors_'+str(105+i)+'.csv'
    data=pd.read_csv(path)
    data1.loc[:,'page1_errors_PS_'+str(105+i)]=data.loc[:,'page1']/147456

for i in range(14):
    path='F:\\flash_testing\\data_figure\\page_errors_'+str(105+i)+'.csv'
    data=pd.read_csv(path)
    data1.loc[:,'page2_errors_PS_'+str(105+i)]=data.loc[:,'page2']/147456

for i in range(14):
    path='F:\\flash_testing\\data_figure\\page_errors_'+str(105+i)+'.csv'
    data=pd.read_csv(path)
    data1.loc[:,'page3_errors_PS_'+str(105+i)]=data.loc[:,'page3']/147456


to_path='F:/flash_testing/data_figure/page_errors_all.csv'
data1.to_csv(to_path)
