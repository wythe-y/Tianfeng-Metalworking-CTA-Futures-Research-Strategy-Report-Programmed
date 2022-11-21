# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:46:16 2022

@author: wytheY
"""
import pandas as pd
import pandas
import csv

scores = pandas.read_csv("S_INFO_WINDCODE.csv",)
print('------ 当前表格：')
print(scores)

print('------ 开始筛选重复数据：')

# 新建个 DataFrame 用来保存过滤后的数据
new_scores = pandas.DataFrame()
# 用来标记是否已存在
existed_name = {}
for index, row in scores.iterrows():
    if row['WINDCODE'] in existed_name:
        print('发现重复项：', row['WINDCODE'])
        continue
    existed_name[row['WINDCODE']] = True
    new_scores = new_scores.append(row, ignore_index=True)

print('------ 筛选后的表格：')
print(new_scores)

print('------ 正在保存到新表格中')
new_scores.to_csv('S_INFO_WINDCODE2.csv', index=False)