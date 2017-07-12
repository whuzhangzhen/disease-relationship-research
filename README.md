# 基于mimiciii数据集的疾病共病分布系统（linux unix下only）


配置安装：

1）下载整个软件包：

下载地址：https://github.com/whuzhangzhen/xinxixitongshiyan

2）安装包管理器pip
终端输入
```
wget https://bootstrap.pypa.io/get-pip.py  --no-check-certificate
```
3）安装各种第三方库
pandas:
```
sudo pip install pandas
```
matplotlib:
```
sudo pip install matplotlib
```
networkx
```
sudo pip install networkx
```
numpy
```
sudo pip install networkx
```

pyqt4

参考博客：http://www.cnblogs.com/jackge/archive/2013/06/05/3119130.html

4）运行：
本地IDE打开整个软件包：

运行ui子文件夹下面的test_login.py文件即可

终端在ui文件夹路径下：

输入  python  test_login.py 即可

1.开发环境：

硬件环境：dell inspriation 7447 

软件环境：ubuntu 16.04系统

开发工具：pycharm社区版+vim+git

开发语言：python2.7

开发第三方库：pip包管理器+matplotlib+networkx+pandas+pyqt4

2.开发过程：


1.数据预处理 
1)共病
首先利用pandas读取如下图所示的MIMICIII数据集中的病人确诊信息表的病人id和患病确诊的ICD9国际疾病编码信息。

代码片段：

```python
def get_data(dataset):
     same_data={}
     list=set()
     for data in dataset:
         list.add(data[0])
         #num_set=set(list)
     return list

data = pd.read_csv('/home/zz/Documents/MIMIC III/DIAGNOSES_ICD_DATA_TABLE.csv')
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
```
在读取完所有病人的患病信息后，将病人的subject_id字段和患病信息存到文档中，最终得到数据集中四万个病人的患病信息。如下图所示：

2:V3001 V053   V290   
3:V053 0389   78559  5849   4275   41071  4280   6826   4254   2639   
4:0389 5849   41071  6826   2639   042    1363   7994   2763   7907   5715   04111  V090   E9317  
5:5849 6826   042    7994   7907   04111  E9317  V3000  V053   V290   
6:6826 7994   04111  V3000  V290   40391  4440   9972   2766   2767   2859   2753   V1582  
7:7994 V3000  40391  9972   2767   2753   V3001  V053   V290   
8:V3000    9972   2753   V053   V3001  7706   7746   V290   V502   V053   
9:9972 V053   7706   V290   V053   431    5070   4280   5849   2765   4019   
10:V290    V053   431    4280   2765   V3000  7742   76525  76515  V290   



2)症状分布

从csv文件DIAGNOSES_ICD_DATA_TABLE中以ICD9_CODE为索引数字匹配相应的疾病编码SUBJECT_ID。再根据匹配得到SUBJECT_ID在另一个csv文件NOTEEVENTS_DATA_TABLE中匹配相应的疾病病症。因为文件NOTEEVENTS_DATA_TABLE无法直接打开，且只知道病症位于该文件的TEXT列中，于是先对TEXT列进行抽取观察疾病病症所处位置。
得到疾病病症位于TEXT中关键词Chief Complaint:后，于是根据所处位置进行单独疾病病症的数据抽取。得到每个所需抽取的疾病号对应的病症
因为部分Chief Complaint:后为空，导致抽取到了一些非疾病病症的词，且这些词出现的比较集中，于是通过直接在结果TXT中进行特定高频词的匹配删除，将非疾病病症词去除，部分极少出现的非疾病病症词频率极小，不影响最后结果所以不进行考虑。
得到删除后的纯疾病病症TXT表。

```python
file = open("/home/xu/下载/NewBZ42731")
r = re.compile(r"\,\s+")

dwords = {}
for line in file:
    w = str.strip(line)
    if w:
        w = str.lower(w)
        lws = r.split(w)
        for word in lws:
            if word in dwords:
                dwords[word] += 1
            else:
                dwords[word] = 1
s = pd.Series(dwords)
s.sort_values(inplace=True,ascending=False)
df = pd.DataFrame(s,columns=['count'])
df['percent'] = df['count']/df['count'].max()

# 保存为csv文件
df.to_csv("42731.csv")
# 打印前5
print(df.head(5))
```
3)时间年龄分布
在进行分布规律的预处理时，首先确定分布规律的包含范围：性别分布和年龄分布。再根据mimic数据库的说明找到所需要使用的csv表格，根据主键进行合并，得到最后的表格。


2.核心算法 
1）共病  章震
常见的频繁项集挖掘算法有两类，一类是Apriori算法，另一类是FPGrowth。Apriori通过不断的构造候选集、筛选候选集挖掘出频繁项集，需要多次扫描原始数据，当原始数据较大时，磁盘I/O次数太多，效率比较低下。FPGrowth算法则只需扫描原始数据两遍，通过FP-tree数据结构对原始数据进行压缩，效率较高。
 FPGrowth算法主要分为两个步骤：FP-tree构建、递归挖掘FP-tree。FP-tree构建通过两次数据扫描，将原始数据中的事务压缩到一个FP-tree树，该FP-tree类似于前缀树，相同前缀的路径可以共用，从而达到压缩数据的目的。接着通过FP-tree找出每个item的条件模式基、条件FP-tree，递归的挖掘条件FP-tree得到所有的频繁项集。
本次实验采用的是改进的opriori算法，也就是生成树的算法，参考《机器学习实战》的关联分析章节部分的算法，其基本思想是构建频繁项集的生成树来表示数据集中的关联规则关系和关联关系的强度。

生成树算法代码片段：
```python
# 定义一个树，保存树的每一个结点
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.parent = parentNode
        self.children = {}  # 用于存放节点的子节点
        self.nodeLink = None  # 用于连接相似的元素项

    # 对count变量增加给定值
    def inc(self, numOccur):
        self.count += numOccur

    # 用于将树以文本形式显示，对于构建树来说并不是需要的
    def disp(self, ind=1):
        print "  " * ind, self.name, "  ", self.count
        for child in self.children.values():
            child.disp(ind + 1)


# FP树的构建函数
def createTree(dataSet, minSup=1):
    ''' 创建FP树 '''
    # 第一次遍历数据集，创建头指针表
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    # 移除不满足最小支持度的元素项
    for k in headerTable.keys():
        if headerTable[k] < minSup:
            #print headerTable[k]
            del (headerTable[k])
    # 空元素集，返回空
    freqItemSet = set(headerTable.keys())
    #print headerTable
    if len(freqItemSet) == 0:
        return None, None
    # 增加一个数据项，用于存放指向相似元素项指针
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]
    retTree = treeNode('Null Set', 1, None)  # 根节点
    # 第二次遍历数据集，创建FP树
    for tranSet, count in dataSet.items():
        localD = {}  # 对一个项集tranSet，记录其中每个元素项的全局频率，用于排序
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]  # 注意这个[0]，因为之前加过一个数据项
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]  # 排序
            updateTree(orderedItems, retTree, headerTable, count)  # 更新FP树
    return retTree, headerTable


def updateTree(items, inTree, headerTable, count):
    # 判断事务中的第一个元素项是否作为子节点存在，如果存在则更新该元素项的计数
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    # 如果不存在，则创建一个新的treeeNode并将其作为子节点添加到树中
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        # 更新头指针表或前一个相似元素项节点的指针指向新节点
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
            # 对剩下的元素项迭代调用updateTree函数
    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)

        # 获取头指针表中该元素项对应的单链表的尾节点，然后将其指向新节点targetNode


def updateHeader(nodeToTest, targetNode):
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict


# =========================================================

# 给定元素项生成一个条件模式基（前缀路径）
# basePat表示输入的频繁项，treeNode为当前FP树中对应的第一个节点（可在函数外部通过headerTable[basePat][1]获取）
def findPrefixPath(basePat, treeNode):
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    # 返回函数的条件模式基
    return condPats


# 辅助函数，直接修改prefixPath的值，将当前节点leafNode添加到prefixPath的末尾，然后递归添加其父节点
def ascendTree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)

        # 递归查找频繁项集


# 参数：inTree和headerTable是由createTree()函数生成的数据集的FP树
#    : minSup表示最小支持度
#    ：preFix请传入一个空集合（set([])），将在函数中用于保存当前前缀
#    ：freqItemList请传入一个空列表（[]），将用来储存生成的频繁项集
def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1])]
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        myConTree, myHead = createTree(condPattBases, minSup)

        if myHead != None:
            # 用于测试
            print 'conditional tree for :', newFreqSet
            myConTree.disp()

            mineTree(myConTree, myHead, minSup, newFreqSet, freqItemList)


# 封装算法
def fpGrowth(dataSet, minSup=3):
    initSet = createInitSet(dataSet)
    myFPtree, myHeaderTab = createTree(initSet, minSup)
    freqItems = []
    mineTree(myFPtree, myHeaderTab, minSup, set([]), freqItems)
    return freqItems

```
测试：
测试算法主要是将存有病人患病信息的数据部分作为测试集，生成FP-growth生成树：
```python
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

```
文字表示的生成树：
conditional tree for : set(['2724'])
   Null Set    1
     4019    9217
conditional tree for : set(['25000'])
   Null Set    1
     4019    9408
conditional tree for : set(['5849'])
   Null Set    1
     4019    8785
conditional tree for : set(['4280'])
   Null Set    1
     42731    3080
       41401    1407
     4019    11456
       42731    6064
         41401    3438
       41401    2660
     41401    1339
conditional tree for : set(['42731'])
   Null Set    1
     4019    12137
       41401    6361
     41401    2492
conditional tree for : set(['41401'])
   Null Set    1
     4019    12954

根据本次共病分析的需要，我们只分析二元频繁项集作为结果：

2724    4019   9217
25000  4019   9408
5849   4019   8785
4280   42731  3080
4280   41401  1339
4280   4019   11456
42731  41401  2492
42731  4019   12137
41401  4019   12954

2）疾病症状 徐炳基
根据疾病编码进行单个疾病病症的词频统计以及每个词与最高频率词的比较百分比，只显示出最高频的5个词。
```python
def get_symptom(name):
    data=pd.read_csv('/home/zz/Desktop/PycharmProjects/xinxixitong/Symptom/{}.csv'.format(name))
    print data.columns
    #data=DataFrame(data,columns=['symptom','count','percent'])
    data_list= data.head(10).get_values()
    for item in data_list:
        item[1]=str(name)
    return data_list
```
3）分布规律 陈思凯
分布规律：
分布规律的实质是统计某个限制条件下病人的数量，以得到相应的分布规律。在这种情形下，只需要将之前预处理的表格进行过滤，统计数量即可。
```python
import csv
with open('data2.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    A = raw_input() 
    B = raw_input()
    count = 0
    for row in reader:
        if row['ICD9_CODE']== str(A) and row['GENDER']==str(B):
            count += 1
            
    print count
```
3.可视化界面
1）结果可视化 章震 

共病关系和症状分布可视化代码：
```python
def common_disease(name=4019):
    edges1 = []
    edges2=[]
    label_dict={}
    with open('/home/zz/Desktop/PycharmProjects/xinxixitong/Common_disease/freqItem.dat','rb')as file:
        for line in file.readlines():
            list=line.split()
            #print list
            edges1.append(list)

    G1 = nx.DiGraph()
    #plt.title('common disease')
    fig1 = plt.figure()

    fig1.set_figheight(3.3)
    fig1.set_figwidth(3.3)

    for i in edges1:
        print i
        #i[2]=float(i[2])/12954
        if   str(name) in i :
            #print i
            edges2.append(i)
    #共病关系
    for item in edges2:
        tuple(item)
        G1.add_edge(str(item[0]),str(item[1]))
    edge_colors1 = range(len(edges2))
    fig1 = nx.draw_networkx(G1, with_labels=True, node_size=400, edge_color=edge_colors1, node_color='gray', font_size=6)
    #fig=nx.draw_networkx_edges(G1,pos=nx.spring_layout(G1))
    plt.savefig('disease.png')

    #症状关系
    G2 = nx.DiGraph()
    fig2 = plt.figure()
    fig2.set_figheight(3.3)
    fig2.set_figwidth(3.3)
    data_list=symptom.get_symptom(name)
    for item in data_list:

        #tuple(item)
        G2.add_edge(item[0],item[1])
        
    edge_colors2 = range(len(data_list))
    fig2=nx.draw_networkx(G2,with_labels=True,node_size=200,edge_color=edge_colors2,node_color='blue',font_size=6)
    node_colors = [(random(), random(), random()) for _i in range(5)]

    plt.savefig('symptom.png')

```
共病全关系图
![](https://github.com/whuzhangzhen/xinxixitongshiyan/blob/master/Common_disease/allrelation.png)		

共病关系和症状分布图

![](https://github.com/whuzhangzhen/xinxixitongshiyan/blob/master/ui/disease.png)
![](https://github.com/whuzhangzhen/xinxixitongshiyan/blob/master/ui/symptom.png)

时间年龄分布代码：

```python
def distribution(name,sex,age1=10,age2=100):
    age_list=[]
    with open('/home/zz/Desktop/PycharmProjects/xinxixitong/distribution/info.csv','rb') as csvfile:
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

```
年龄性别分布图：

![](https://github.com/whuzhangzhen/xinxixitongshiyan/blob/master/ui/distribution.png)


2）界面UI设计  王子叶
（1）登录界面
功能：输入正确的用户名和密码，即可进入系统
实现：新建一个QWidget，在其中添加标签QLabel、按钮QPushButton、用户名及密码输入框QLineEdit，将其合理布局，尽量使其美观。并在按钮中添加事件，使得输入正确的用户名和密码可进入系统。

```python
 '''登录界面

        '''
        self.Login = QtGui.QFrame(self.Register)
        self.Login.setGeometry(QtCore.QRect(0, 0, 1150, 650))
        self.Login.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Login.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Login.setFrameShadow(QtGui.QFrame.Raised)
        self.Login.setObjectName(_fromUtf8("Login"))
        #标题
        self.title1 = QtGui.QLabel(self.Login)
        self.title1.setGeometry(QtCore.QRect(0, 0, 1150, 95))
        self.title1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 29pt \"微软雅黑\";\n"
"background-color: rgb(3, 146, 255)\n"
"\n"
""))
        self.title1.setObjectName(_fromUtf8("title1"))
        #系统名
        self.nameLabel = QtGui.QLabel(self.Login)
        self.nameLabel.setGeometry(QtCore.QRect(280, 160, 750, 95))
        self.nameLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 75 25pt \"微软雅黑\";"))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        #用户名
        self.usernameLabel = QtGui.QLabel(self.Login)
        self.usernameLabel.setGeometry(QtCore.QRect(380, 300, 130, 30))
        self.usernameLabel.setStyleSheet(_fromUtf8("font: 75 13pt \"微软雅黑\";\n"
"color: rgb(3, 146, 255);"))
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        # 用户名输入
        self.usernameText = QtGui.QLineEdit(self.Login)
        self.usernameText.setGeometry(QtCore.QRect(500, 300, 250, 35))
        self.usernameText.setStyleSheet(_fromUtf8("font: 13pt \"微软雅黑\";"))
        self.usernameText.setObjectName(_fromUtf8("usernameText"))
        self.usernameText.setText('admin')
        #密码
        self.passwordLabel = QtGui.QLabel(self.Login)
        self.passwordLabel.setGeometry(QtCore.QRect(380, 370, 130, 30))
        self.passwordLabel.setStyleSheet(_fromUtf8("font: 75 13pt \"微软雅黑\";\n"
"color: rgb(3, 146, 255);"))
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        # 密码输入
        self.passwordEdit1 = QtGui.QLineEdit(self.Login)
        self.passwordEdit1.setGeometry(QtCore.QRect(500, 370, 250, 35))
        self.passwordEdit1.setStyleSheet(_fromUtf8("font: 13pt \"微软雅黑\";"))
        self.passwordEdit1.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit1.setObjectName(_fromUtf8("passwordEdit1"))
        self.passwordEdit1.setText('admin')

        #登录按钮
        self.loginButton = QtGui.QPushButton(self.Login)
        self.loginButton.setGeometry(QtCore.QRect(530, 450, 150, 35))
        self.loginButton.setStyleSheet(_fromUtf8("background-color: rgb(3, 146, 255);\n"
"font: 75 13pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
""))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
```



（2）使用说明界面
功能：提供系统的使用说明，方便用户使用
实现：新建一个QWidget，在其中添加标签QLabel、按钮QPushButton，将其合理布局，尽量使其美观。并在按钮中添加事件，使得点击按钮可以进入分布界面。

代码：
```python
疾病界面
        '''
        self.Disease = QtGui.QFrame(self.Distribution)
        self.Disease.setGeometry(QtCore.QRect(0, 0, 1150, 650))
        self.Disease.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Disease.setObjectName(_fromUtf8("Disease"))
        #标题
        self.title3 = QtGui.QLabel(self.Disease)
        self.title3.setGeometry(QtCore.QRect(0, 0, 1150, 95))
        self.title3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 29pt \"微软雅黑\";\n"
"background-color: rgb(3, 146, 255)\n"
"\n"
""))
        self.title3.setObjectName(_fromUtf8("title3"))
        # instruction
        self.instruction = QtGui.QLabel(self.Disease)
        self.instruction.setGeometry(QtCore.QRect(250, 100, 850, 450))
        self.instruction.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.instruction.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                            "font: 75 11pt \"微软雅黑\";\n"
                                            "background-color: rgb(255, 255, 255)\n"
                                            "\n"
                                            ""))
        png = QtGui.QPixmap('instruction.png')
        self.instruction.setPixmap(png)

        #Go
        self.dButton1 = QtGui.QPushButton(self.Disease)
        self.dButton1.setGeometry(QtCore.QRect(800, 580, 80, 30))
        self.dButton1.setStyleSheet(_fromUtf8("background-color: rgb(3, 146, 255);\n"
"font: 11pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);"))
        self.dButton1.setObjectName(_fromUtf8("dButton1"))


        #welcome
        self.welcomeLabel1 = QtGui.QLabel(self.Disease)
        self.welcomeLabel1.setGeometry(QtCore.QRect(950, 40, 80, 30))
        self.welcomeLabel1.setStyleSheet(_fromUtf8("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 146, 255);"))
        self.welcomeLabel1.setObjectName(_fromUtf8("welcomeLabel1"))
        #返回按钮
        self.backButton1 = QtGui.QPushButton(self.Disease)
        self.backButton1.setGeometry(QtCore.QRect(950, 580, 80, 30))
        self.backButton1.setStyleSheet(_fromUtf8("background-color: rgb(3, 146, 255);\n"
"font: 11pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);"))
        self.backButton1.setObjectName(_fromUtf8("backButton1"))
#-----------------------------------------------------------------
```



（3）疾病分布界面
功能：查看疾病的共病、症状以及年龄性别分布等，并提供交互式查询
实现：新建一个QWidget，在其中添加标签QLabel、按钮QPushButton、输入框QLineEdit等，将其合理布局，尽量使其美观。考虑到性别分布无非分男、女和全部，所以采用了单选按钮QRadioButton；年龄分布的选择较多，所以采用了输入查询的形式。性别分布与年龄分布支持交叉查询。
代码：
```python

        '''分布界面
        '''
        #layout = QtGui.QVBoxLayout()
        self.Distribution = QtGui.QWidget(DDAS)
        self.Distribution.setGeometry(QtCore.QRect(0, 0, 1150, 650))
        self.Distribution.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Distribution.setObjectName(_fromUtf8("Distribution"))

        #标题
        self.title4 = QtGui.QLabel(self.Distribution)
        self.title4.setGeometry(QtCore.QRect(0, 0, 1150, 95))
        self.title4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 29pt \"微软雅黑\";\n"
"background-color: rgb(3, 146, 255)\n"
"\n"
""))
        self.title4.setObjectName(_fromUtf8("title4"))
        # 搜索按钮
        self.searchButton = QtGui.QPushButton(self.Distribution)
        self.searchButton.setGeometry(QtCore.QRect(1000, 110, 70, 30))
        self.searchButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                  "font: 11pt \"微软雅黑\";\n"
                                                  "background-color: rgb(3, 146, 255);"))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.searchButton.connect(self.searchButton, QtCore.SIGNAL('clicked()'),
                     self.showgraph1)
        # 搜索框
        self.searchText = QtGui.QLineEdit(self.Distribution)
        self.searchText.setGeometry(QtCore.QRect(800, 110, 180, 30))
        self.searchText.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))
        self.searchText.setObjectName(_fromUtf8("searchText"))
        #年龄标签
        self.ageLabel = QtGui.QLabel(self.Distribution)
        self.ageLabel.setGeometry(QtCore.QRect(650, 160, 30, 30))
        self.ageLabel.setStyleSheet(_fromUtf8("font: 80 10pt \"微软雅黑\";\n"
                                              "color: rgb(0, 0, 0);"))
        self.ageLabel.setObjectName(_fromUtf8("ageLabel"))
        # 年龄分布起始年龄输入
        self.ageEdit = QtGui.QLineEdit(self.Distribution)
        self.ageEdit.setGeometry(QtCore.QRect(680, 160, 30, 30))
        self.ageEdit.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.ageEdit.setObjectName(_fromUtf8("ageEdit"))
        # 年龄之间的横杠
        self.aLabel = QtGui.QLabel(self.Distribution)
        self.aLabel.setGeometry(QtCore.QRect(710, 160, 10, 30))
        self.aLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(255, 255, 255);\n"
                                            "font: 9pt \"微软雅黑\";"))
        self.aLabel.setObjectName(_fromUtf8("aLabel"))
        # 终止年龄
        self.ageEdit2 = QtGui.QLineEdit(self.Distribution)
        self.ageEdit2.setGeometry(QtCore.QRect(720, 160, 30, 30))
        self.ageEdit2.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.ageEdit2.setObjectName(_fromUtf8("ageEdit2"))
        #性别标签
        self.sexLabel = QtGui.QLabel(self.Distribution)
        self.sexLabel.setGeometry(QtCore.QRect(800, 160, 30, 30))
        self.sexLabel.setStyleSheet(_fromUtf8("font: 80 10pt \"微软雅黑\";\n"
                                              "color: rgb(0, 0, 0);"))
        self.sexLabel.setObjectName(_fromUtf8("sexLabel"))
        #性别分布按钮 male、female、all
        self.maleButton = QtGui.QRadioButton(self.Distribution)
        self.maleButton.setGeometry(QtCore.QRect(830, 160, 65, 30))
        self.maleButton.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.maleButton.setObjectName(_fromUtf8("maleButton"))
        self.femaleButton = QtGui.QRadioButton(self.Distribution)
        self.femaleButton.setGeometry(QtCore.QRect(890, 160, 70, 30))
        self.femaleButton.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.femaleButton.setObjectName(_fromUtf8("femaleButton"))
        self.allButton = QtGui.QRadioButton(self.Distribution)
        self.allButton.setGeometry(QtCore.QRect(970, 160, 60, 30))
        self.allButton.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.allButton.setObjectName(_fromUtf8("allButton"))
        # 交叉查询按钮
        self.goButton = QtGui.QPushButton(self.Distribution)
        self.goButton.setGeometry(QtCore.QRect(1050, 160, 30, 30))
        self.goButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                              "font: 11pt \"微软雅黑\";\n"
                                              "background-color: rgb(3, 146, 255);"))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.goButton.connect(self.goButton, QtCore.SIGNAL('clicked()'),
                                  self.showgraph2)


        # 共病显示框
        self.QLabel = QtGui.QLabel(self.Distribution)
        self.QLabel.setGeometry(QtCore.QRect(20, 190, 330, 330))
        self.QLabel.setObjectName(_fromUtf8("graphicsView2"))
        #症状显示框
        self.QLabel2 = QtGui.QLabel(self.Distribution)
        self.QLabel2.setGeometry(QtCore.QRect(350, 190, 330, 330))
        self.QLabel2.setObjectName(_fromUtf8("graphicsView2"))
        # 年龄性别分布显示框
        self.QLabel3 = QtGui.QLabel(self.Distribution)
        self.QLabel3.setGeometry(QtCore.QRect(680, 190, 400,330))
        self.QLabel3.setObjectName(_fromUtf8("graphicsView3"))

        #welcome
        self.welcomeLabel2 = QtGui.QLabel(self.Distribution)
        self.welcomeLabel2.setGeometry(QtCore.QRect(950, 40, 80, 30))
        self.welcomeLabel2.setStyleSheet(_fromUtf8("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 146, 255);"))
        self.welcomeLabel2.setObjectName(_fromUtf8("welcomeLabel2"))
        #返回
        self.backButton2 = QtGui.QPushButton(self.Distribution)
        self.backButton2.setGeometry(QtCore.QRect(950, 580, 80, 30))
        self.backButton2.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 146, 255);"))
        self.backButton2.setObjectName(_fromUtf8("backButton2"))

#----------------------------------------------------------------


