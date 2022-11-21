# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:47:25 2022

@author: wytheY
"""

import pandas as pd
import numpy as np

df = pd.read_excel("橡胶2208.xlsx",)
#print(df)

list1 = df.close
#print(list1)
list2 = [x for x in list1 if np.isnan(x) == False]#去除nan
#print(list2)

a = sum(list2)
print("近月合约")
print(a/len(list2))
b = a/len(list2)

df = pd.read_excel("橡胶2307.xlsx",)
#print(df)

list3 = df.close
#print(list3)
list4 = [x for x in list3 if np.isnan(x) == False]#去除nan
#print(list4)

c = sum(list4)
print("远月合约")
print(c/len(list4))
d = c/len(list4)

"""roll returnT"""
RU = ((b-d)/d)*(365%(2307-2208))
print("橡胶展期收益")
print(RU)

df = pd.read_excel("纸浆2208.xlsx",)
#print(df)

list1 = df.close
#print(list1)
list2 = [x for x in list1 if np.isnan(x) == False]#去除nan
#print(list2)

a = sum(list2)
print("近月合约")
print(a/len(list2))
b = a/len(list2)

df = pd.read_excel("纸浆2307.xlsx",)
#print(df)

list3 = df.close
#print(list3)
list4 = [x for x in list3 if np.isnan(x) == False]#去除nan
#print(list4)

c = sum(list4)
print("远月合约")
print(c/len(list4))
d = c/len(list4)

"""roll returnT"""
SP = ((b-d)/d)*(365%(2307-2208))
print("纸浆展期收益")
print(SP)

df = pd.read_excel("沪铝2208.xlsx",)
#print(df)

list1 = df.close
#print(list1)
list2 = [x for x in list1 if np.isnan(x) == False]#去除nan
#print(list2)

a = sum(list2)
print("近月合约")
print(a/len(list2))
b = a/len(list2)

df = pd.read_excel("沪铝2307.xlsx",)
#print(df)

list3 = df.close
#print(list3)
list4 = [x for x in list3 if np.isnan(x) == False]#去除nan
#print(list4)

c = sum(list4)
print("远月合约")
print(c/len(list4))
d = c/len(list4)

"""roll returnT"""
AL = ((b-d)/d)*(365%(2307-2208))
print("沪铝展期收益")
print(AL)



if RU>SP:    #两个比大小，两种情况，所以if一种，else一种
    max_num = RU  #得出大值是RU
    if max_num>AL:  #大值与第三个数字比较
        print('最大为RU',max_num)
    else:
        print('最大为AL',AL)
else:
    max_num = SP
    if max_num>AL:
        print('最大为SP',max_num)
    else:
        print('最大为AL',AL)
    



"""database_connection = create_engine('sqlite:') 
dataframe = pd.read_sql_query('SELECT*FROM DATA')
dataframe.head(2)"""
#a = pd.read_excel("FU01.xlsx",
#index_col='close')

#print(a)