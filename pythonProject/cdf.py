import numpy as np
import pandas as pd

path='F:\\cdf_draw\\third_four_chara.csv'

data=pd.read_csv(path)
#print(data)



a=sorted(data.loc[:,'num'],reverse=True)
print(a)
print(len(a))
print(sum(a))
data1=pd.DataFrame(np.random.randn(len(a), 1))
c=np.zeros(len(a))
for i in range(len(a)):
    for j in range(i+1):
        c[i]=c[i]+a[j]
    data1.loc[i:'per']=c[i]/sum(a)

print(data1)
to_path='F:\\cdf_draw\\four\\third.csv'
data1.to_csv(to_path)


