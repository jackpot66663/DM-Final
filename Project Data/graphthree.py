import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r'NotoSansTC-Medium.otf')

df = pd.read_csv('個別學生資料.csv',encoding='big5')

club = ['有參加社團','無參加社團']
x = [1,1.4]

num_yes = df.loc[(df.參加社團=='Y')&(df.二一不及格次數==1),'S_ID']
num_no = df.loc[(df.參加社團=='N')&(df.二一不及格次數==1),'S_ID']

y = [len(num_yes),len(num_no)]

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.bar(x,y,color='b',tick_label = club,width=0.2)
plt.title('二一次數與有無參加社團比較',fontProperties=font)
plt.ylabel('二一次數',fontProperties=font)
plt.show()