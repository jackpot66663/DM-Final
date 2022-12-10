import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

df1 = pd.read_csv('學生社團資料.csv')
df2 = pd.read_csv('學生成績資料.csv')

df3 = pd.merge(df1,df2,
                left_on=['s_id','semester'],
                right_on=['s_id','semester'],
                how='inner')

x = [1,2,3,4,5,6,7,8]
semester = [1021,1022,1031,1032,1041,1042,1051,1052]
club = ['系學會','學術性社團','聯誼性社團','服務性社團','康樂性社團']

for i in range(len(df3['club_id'])):
    if(df3['club_id'][i][0]=='C'):
        df3 = df3.replace(df3['club_id'][i],'C')
    elif(df3['club_id'][i][0]=='A'):
        df3 = df3.replace(df3['club_id'][i],'A')
    elif(df3['club_id'][i][0]=='B'):
        df3 = df3.replace(df3['club_id'][i],'B')
    elif(df3['club_id'][i][0]=='D'):
        df3 = df3.replace(df3['club_id'][i],'D')
    else:
        df3 = df3.replace(df3['club_id'][i],'E')

A_average = [None]*len(semester)
B_average = [None]*len(semester)
C_average = [None]*len(semester)
D_average = [None]*len(semester)
E_average = [None]*len(semester)

for i in range(len(semester)):
    A_score = df3.loc[(df3['semester']==semester[i])&(df3['club_id']=='A'),'average']
    A_total = 0
    for score in A_score:
        A_total+=score
    A_average[i] = A_total/len(A_score)

    B_score = df3.loc[(df3['semester']==semester[i])&(df3['club_id']=='B'),'average']
    B_total = 0
    for score in B_score:
        B_total+=score
    B_average[i] = B_total/len(B_score)

    C_score = df3.loc[(df3['semester']==semester[i])&(df3['club_id']=='C'),'average']
    C_total = 0
    for score in C_score:
        C_total+=score
    C_average[i] = C_total/len(C_score)

    D_score = df3.loc[(df3['semester']==semester[i])&(df3['club_id']=='D'),'average']
    D_total = 0
    for score in D_score:
        D_total+=score
    D_average[i] = D_total/len(D_score)

    E_score = df3.loc[(df3['semester']==semester[i])&(df3['club_id']=='E'),'average']
    E_total = 0
    for score in E_score:
        E_total+=score
    E_average[i] = E_total/len(E_score)



plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x, A_average, color = 'g', linestyle = 'solid',marker='o', label = "系學會")
plt.plot(x, B_average, color = 'b', linestyle = 'solid',marker='o', label = "學術性社團")
plt.plot(x, C_average, color = 'c', linestyle = 'solid',marker='o', label = "聯誼性社團")
plt.plot(x, D_average, color = 'r', linestyle = 'solid', marker='o',label = "服務性社團")
plt.plot(x, E_average, color = 'm', linestyle = 'solid', marker='o',label = "康樂性社團")
plt.xticks(x,semester,rotation='vertical')
plt.xlabel('學期')
plt.ylabel('總體平均成績')
plt.title('不同屬性社團對總體學生平均')
plt.tight_layout()
plt.legend()
plt.show()