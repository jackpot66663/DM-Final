import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

df1 = pd.read_csv('個別學生資料.csv',encoding='big5')
df2 = pd.read_csv('學生成績資料.csv')

df3 = pd.merge(df1,df2,
                left_on='S_ID',
                right_on='s_id',
                how='inner')

# rows = (df3['科系'] == '資訊工程學系')
# cols = ['s_id','semester','dept_no']

font = FontProperties(fname=r'NotoSansTC-Medium.otf')

semester = [1021,1022,1031,1032,1041,1042,1051,1052]
x1 = [0.8,1.8,2.8,3.8,4.8,5.8,6.8,7.8]
x=[1,2,3,4,5,6,7,8]
rank_yes = [None]*len(semester)
rank_no =[None]*len(semester)
for i in range(len(semester)):
    dept_yes = df3.loc[(df3.semester==semester[i])&(df3.科系=='地球科學學系')&(df3.參加社團=='Y'),'dept_no']
    dept_no = df3.loc[(df3.semester==semester[i])&(df3.科系=='地球科學學系')&(df3.參加社團=='N'),'dept_no']
    
    total_yes = 0
    total_no = 0
    for j in range(len(dept_yes)):
        total_yes = total_yes + dept_yes.values[j]
    for j in range(len(dept_no)): 
        total_no = total_no + dept_no.values[j]
    
    average_yes = total_yes/len(dept_yes)
    average_no = total_no/len(dept_no)

    rank_yes[i] = average_yes
    rank_no[i] = average_no

plt.bar(x,rank_yes,color='b',tick_label=semester,width=0.4,align='edge')
plt.bar(x1,rank_no,color='yellow',width=0.4)
plt.title('地科系有無參加社團平均系排比較',fontProperties=font)
plt.xlabel('學期',fontProperties=font)
plt.ylabel('平均系排名',fontProperties=font)
colors = {'有參加過社團':'blue','沒參加過社團':'yellow'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels,prop=font)
plt.show()
