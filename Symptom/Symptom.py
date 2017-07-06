 #-*- coding: utf-8 -*-


import re
import pandas as pd

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