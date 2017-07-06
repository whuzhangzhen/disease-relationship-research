#coding:utf-8


import FP_Tree
from pymongo import *
#将数据集加载到列表


#连接到数据库
#client=MongoClient()
#db=client.patientinfo_db
#collections=db.patient_disease
#查找所有疾病
#patient_data=collections.find()

#print patient_data

parsedDat = [line.split(':')[1].split() for line in open('opriori.txt').readlines()]
#print parsedDat

#初始集合格式化
initSet = FP_Tree.createInitSet(parsedDat)

#构建FP树
myFPtree, myHeaderTab = FP_Tree.createTree(initSet, 8000)

#创建空列表，保存频繁项集
myFreqList = []
FP_Tree.mineTree(myFPtree, myHeaderTab, 8000, set([]), myFreqList)

for freqItem in myFreqList:
    #print freqItem
    if len(freqItem)==2:
        file= open ('freqItem1.dat','a')
        for i in freqItem:
            file.write(i+'\t')
        file.write('\n')
        file.close()

for item in myHeaderTab.values():
    item.remove(item[1])
print myHeaderTab
#print len(myFreqList)
#print myFreqList