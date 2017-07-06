#coding:utf-8

import pandas as pd
from pandas import DataFrame
import os
def get_symptom(name):
    data=pd.read_csv(os.path.abspath('..')+'/Symptom/{}.csv'.format(name))
    print data.columns
    #data=DataFrame(data,columns=['symptom','count','percent'])
    data_list= data.head(10).get_values()
    for item in data_list:
        item[1]=str(name)
    return data_list
#data=get_symptom(25000)
#print data