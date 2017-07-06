#coding:utf-8

import pandas as pd
import numpy as numpy
import os

'''
codeinfoc
author:zhangzhen
author:zhangzhen
author:zhangzhen
create-time:2017-5-15

'''

def get_data(dataset):
     same_data={}
     list=set()
     for data in dataset:
         list.add(data[0])
         #num_set=set(list)
     return list

data = pd.read_csv(os.path.abspath('..')+'/Common_disease/D_ICD_DIAGNOSES_DATA_TABLE.csv')
patient_data = data[[1, 4]]
#获取subject_id列表
list=list(get_data(patient_data.values))
print list
print patient_data.values

apriori_list=[]
value_list=[]
for i in list:
    for j in patient_data.values:
        if j[0] ==i:
            value_list.append(j[1])

    if not len(value_list)==0:
        file=open('opriori.txt','a')
        print u'正在写入集合项:',i
        file.write(str(i)+':')
        for value in value_list:
            file.write(str(value)+'\t')
        file.write('\n')
            #file.write(value+'\t')

        file.close()
        for i in value_list:
            value_list.remove(i)
print u'集合项写入完毕，请打开文件查看-----'














