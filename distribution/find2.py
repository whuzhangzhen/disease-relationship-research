# -*- coding:utf-8 -*-
import csv as csv
import numpy as np
import codecs
# -------------
# csv读取表格数据
# -------------

csv_file_object = csv.reader(codecs.open('data.csv', 'rb'))
header = csv_file_object.next()
print header
print type(header)
print header[1]

data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)

print data[0::, 0]
# -------------
# pandas读取表格数据
# -------------
import pandas as pd

df = pd.read_csv('data.csv')  # 读者借阅信息表
print df.head()
print '----------------'
print df[['SUBJECT_ID', 'HADM_ID', 'ADMITTIME', 'GENDER','DOB']]  # 选取其中的四列
print '------------------------------------------------------------------'
print

dd = pd.read_csv('DIAGNOSES_ICD_DATA_TABLE.csv')

print dd.head()
print '----------------'
print dd[['SUBJECT_ID', 'HADM_ID', 'ICD9_CODE', ]]
print '------------------------------------------------------------------'
print

data = pd.merge(df, dd, on=['SUBJECT_ID','HADM_ID'], how='left')  # pandas csv表左连接
data = data[['SUBJECT_ID', 'HADM_ID', 'ADMITTIME', 'GENDER', 'DOB','ICD9_CODE' ]]
print data
print '------------------------------------------------------------------'
print

# -------------
# pandas写入表格数据
# -------------
data.to_csv(r'data2.csv', encoding='gbk')