import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('學生社團資料.csv')
df2 = pd.read_csv('學生成績資料.csv')

df3 = pd.merge(df1,df2,
                left_on=['s_id','semester'],
                right_on=['s_id','semester'],
                how='inner')

x = [1,2,3,4,5,6,7,8]
semester = [1021,1022,1031,1032,1041,1042,1051,1052]


average_m = [None]*len(semester)
average_a = [None]*len(semester)
average_l = [None]*len(semester)

for i in range(len(semester)):
    score_m = df3.loc[(df3['semester']==semester[i])&(df3['member_flag']=='Y'),'average']
    total_m = 0
    for score in score_m:
        total_m += score
    average_m[i] = total_m/len(score_m)

    score_a = df3.loc[(df3['semester']==semester[i])&(df3['assistant_manager_flag']=='Y'),'average']
    total_a = 0
    for score in score_a:
        total_a += score
    average_a[i] = total_a/len(score_a)

    score_l = df3.loc[(df3['semester']==semester[i])&(df3['manager_flag']=='Y'),'average']
    total_l = 0
    for score in score_l:
        total_l += score
    average_l[i] = total_l/len(score_l)




plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x,average_m , color = 'c', linestyle = 'solid', label = "社員")
plt.plot(x,average_a, color = 'r', linestyle = 'solid',label = "社幹")
plt.plot(x,average_l, color = 'm', linestyle = 'solid',label = "社長")
plt.xticks(x,semester,rotation='vertical')
plt.xlabel('學期')
plt.ylabel('總體平均成績')
plt.title('社長、社員、社幹成績走勢')
plt.tight_layout()
plt.legend()
plt.show()