import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('個別學生資料.csv',encoding='big5')
df2 = pd.read_csv('畢業後問卷.csv',encoding='big5')

df3 = pd.merge(df1,df2,
                left_on='S_ID',
                right_on='s_id',
                how='inner')

test = df3.loc[(df3['參加社團']=='Y')]
ans1 = df3.loc[(df3['參加社團']=='Y')&(df3['question']=='您目前未就業的原因為何?_1'),'ans_description']  #進修中
ans2 = df3.loc[(df3['參加社團']=='Y')&(df3['question']=='您目前未就業的原因為何?_2'),'ans_description']  #尚未找到工作
ans3 = df3.loc[(df3['參加社團']=='Y')&(df3['question']=='您目前的工作狀況為何？(本題選答1、2、3項者，第6題無須填答)_1'),'ans_description']   #工作中
total= len(test['S_ID'].value_counts())
studing = len(ans1)
finding = len(ans2)
working = len(ans3)

label = ['進修中','待業中','工作中']
size = [studing/total,finding/total,working/total]



plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.pie(size,                           # 數值
        labels = label,                 # 標籤
        autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {"fontsize" : 12})

plt.axis('equal')                                          # 使圓餅圖比例相等
plt.title('參加社團學生之畢業後狀況')
plt.legend(loc = "best")
plt.show()





