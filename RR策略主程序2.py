# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:02:34 2022

@author: wytheY
"""
from iFinDPy import *
#from tick_trade_api import DatafeedHqGenerator
#from tick_trade_api import MindgoHqGenerator
import pandas as pd
import openpyxl as op
import numpy as np
import dateutil.relativedelta
import time
import datetime
import csv
from openpyxl import load_workbook
import calendar
import os
global null
import re

with open("results.csv",'w+',newline='') as t3:
    title=["日期","做空","做多","主力空","主力多"]
    writer3=csv.writer(t3)#这一步是创建一个csv的写入器
    writer3.writerow(title)#写入标签
    for p in range(1,5):    
        for k in range(1, calendar.mdays[p]+1): 
            shift_date = p,'月',k,'日',
            shift_date = str(shift_date)
            shift_date = shift_date.replace("'","")
            shift_date = shift_date.replace(",","")
            shift_date = shift_date.replace("(","")
            shift_date = shift_date.replace(")","")
            shift_date = shift_date.replace(" ","")
            print(p,'月',k,'日',)
            df = pd.read_csv("历史数据2.csv",)
            timechange3 = str(p).rjust(2,'0')
            timechange4 = str(k).rjust(2,'0')
            timechange1 = "2015"+timechange3+timechange4+"230000"
            #print(timechange1)  # <class 'int'> 
            timechange2 = str(timechange1)
            #print(timechange2)  # <class 'str'>
            from datetime import datetime
            shift_datetime = datetime.strptime(timechange2, '%Y%m%d%H%M%S')  # 字符串 -> 时间
            shift_date1 = shift_datetime.strftime("%Y-%m-%d %H:%M:%S")
            shift_date3 = shift_date1[0:10]
        #   print(shift_date1)
        #   timechange3 = str(p).rjust(2,'0')
        #   timechange4 = str(k).rjust(2,'0')
            timechange1 = "2015"+timechange3+timechange4+"235959"
            #print(timechange1)  # <class 'int'> 
        #   timechange2 = str(timechange1)
            timechange2 = timechange1[0:8]
            timechange2 = int(timechange2)
        #   print(timechange2)
            #print(timechange2)  # <class 'str'>
            df = df[df['TRADE_DT'].isin([timechange2])] #找出数值对应行#df = pd.read_csv("RBdata.csv",)
            df4 = pd.read_csv('S_INFO_WINDCODE2.csv',header=0)
 #          df4 = df4.to_csv('S_INFO_WINDCODE2.csv', header=False)
            k = 0
            arr = list
            if df.empty:
                print("空日")
            else:
               #print(p,'月',k,'日',)
                df = pd.read_csv("report.csv",encoding='gb2312')
                print(df)
                dd = df[df['DAY'].isin([shift_date])]
                print(dd)
                dd = dd.DATA
                dd = list(dd)
                print(dd)
                
                def bubbleSort(dd):
                       n = len(dd)
                       # 遍历所有数组元素
                       for i in range(n):
                           # Last i elements are already in place
                               for j in range(0, n-i-1):
                                   if dd[j] > dd[j+1] :
                                      dd[j], dd[j+1] = dd[j+1], dd[j]   
                bubbleSort(dd)   
                print(dd)
                arr3 =[]  
                arr4 =[]                        
                l = 0
                for pp in dd:                           
                       if l <= int(0.2*(len(dd))):
                #                               df = df.loc[df['S_INFO_WINDCODE'].str.contains(line2)] #筛选（包含）
                #                               df.reset_index(inplace=True)
                #                               pp = str(pp)
                           #print(pp)
                            df = pd.read_csv("report.csv",encoding='GB2312')
                           #print(df)
                            df = df[df['DAY'].isin([shift_date])]
                           #print(df)
                            df = df[df['DATA'] == pp]
                           #print(df)
                            df = df.ID.tolist()
                           #print(df)
                            df = str(df)
                           #print(df)
                            df = df.replace("[","")
                            df = df.replace("]","")
                            df = df.replace("'","")
                            df = df.replace(" ","")
                            print(df)
                            arr3.append(df) 
                       if  l >= int(0.8*(len(dd))) and l <= len(dd):
                #                               df = df.loc[df['DATA'].str.contains(str(pp))] 
                #                               dd = str(pp)
                            print(pp)
                            df = pd.read_csv("report.csv",encoding='GB2312')
                            df = df[df['DAY'].isin([shift_date])]
                            df = df[df['DATA'] == pp]
                            df = df.ID.tolist() 
                            df = str(df)                                          
                            df = df.replace("[","")
                            df = df.replace("]","")
                            df = df.replace("'","")
                            df = df.replace(" ","")
                            print(df)
                            arr4.append(df) 
                       l = l+1
                thscode1 = arr3
                thscode2 = arr4 
                
                arr5 = [] 
                arr6 = []
                arr2 = []
                   
                for OIO in arr3:                    
                       print(OIO)
                       df = pd.read_csv("report.csv",encoding='GB2312')
                       df = df[df['DAY'].isin([shift_date])]
                       for IOI in df.ID:
                           if OIO == IOI:#不够严谨
                               print(IOI)
                               df = pd.read_csv("report.csv",encoding='GB2312')
                               df = df[df['DAY'].isin([shift_date])]
                               df = df[df['ID'] == IOI]
                               df = str(df.Submaincontract.values)
                               df = df.replace("[","")
                               df = df.replace("]","")
                               df = df.replace("'","")
                               df = df.replace(" ","")
                               print(df)
                               arr5.append(df) 
                  #print(arr5)
                for OIO in arr4:
                       df = pd.read_csv("report.csv",encoding='GB2312')
                       df = df[df['DAY'].isin([shift_date])]
                       for IOI in df.ID:
                           if OIO == IOI:
                               df = pd.read_csv("report.csv",encoding='GB2312')
                               df = df[df['DAY'].isin([shift_date])]
                               df = df[df['ID'] == IOI]
                               df = str(df.Submaincontract.values)
                               df = df.replace("[","")
                               df = df.replace("]","")
                               df = df.replace("'","")
                               df = df.replace(" ","")
                               arr6.append(df)  
                  
                arr2 = shift_date,thscode1,thscode2,arr5,arr6
                writer3.writerows([arr2])#写入标签 
                #                      df = pd.read_csv("report.csv",encoding='ISO-8859-1')
                #                      df = df.drop(columns=["DAY","ID","DATA","Maincontract","Submaincontract"])
                #                      df.to_csv("report.csv",index=False,encoding='ISO-8859-1')