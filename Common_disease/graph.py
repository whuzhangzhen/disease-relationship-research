#coding:utf-8


import numpy
import matplotlib.pyplot as plt
import networkx as nx
from random import random
from Symptom import symptom
import os

def common_disease(name=4019):
    edges1 = []
    edges2=[]
    label_dict={}
    #print os.path
    #print os.getcwd()
    with open(os.path.abspath('..')+'/Common_disease/freqItem.dat','rb')as file:
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
    #plt.show()

common_disease(2724)