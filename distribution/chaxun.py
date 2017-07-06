# coding:utf-8
import csv
import os
import re
import matplotlib.pyplot as plt



def distribution(name,sex,age1=10,age2=100):
    age_list=[]
    with open(os.path.abspath('..')+'/distribution/info.csv','rb') as csvfile:
        reader = csv.DictReader(csvfile)
        #A = raw_input('请输入疾病号')
       # B = raw_input('请输入最小年龄')
        #C = raw_input('请输入最大年龄')
       # D = raw_input('请输入性别')
        count = 0
        for row in reader:
            if row['ICD9_CODE']== str(name) and row['GENDER']== str(sex):
                #for i in range(age1, age2, 5):
                age = int(row['ADMITTIME'][:4]) - int(row['DOB'][:4])

                if age >= int(age1) and age <= int(age2):
                 #   count += 1

                    age_list.append(age)
    fig = plt.figure()
    fig.set_figheight(3.3)
    fig.set_figwidth(4)
    ax = fig.add_subplot(111)
    ax.hist(age_list, bins=10)
    plt.title('Age distribution')
    #plt.xlabel('Age')
    plt.ylabel('num')
                # plt.show()
    plt.savefig('distribution.png')

#distribution(41401,'F')