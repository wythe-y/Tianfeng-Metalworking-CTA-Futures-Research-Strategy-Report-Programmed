# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:30:38 2022

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
from dateutil.relativedelta import relativedelta
null=''  
#此程序仅仅只有完成做空内容，做多内容暂未处理，但其实就是copy程序而已。
#THS_iFinDLogin('ztzgsx002','609226')
today_str = datetime.datetime.now()

ccrange = [10,20,30]#持仓周期 #目前问题还在于，只做了两次判断，并且有遇到无数据情况（已经解决）
seerange = [20,30,40]  #观察周期
zp = 30 #暂未用到，if函数内用来限制的变数，例如只有30笔资料
isAnim = 1;
for day in ccrange:
    print('持仓周期',day)
    for see in seerange:
           time = 0
           arr4 = []
           print('观察周期',see)
        # if zp <= 52:
        #    zp = zp+day
           for p in range(2,4):                
               if isAnim == 1:
                  k =1
                  isAnim = 2
               else:
                  if k+day <= calendar.mdays[p]+1:      
                       k = k+day
                  else:
                       k = k+day-calendar.mdays[p]+1                       
               for k in range(1, calendar.mdays[p]+1,day): #pk变化存在冲突,已经解决
                   time = time+1
                   shift_date = p,'月',k,'日',
                   shift_date = str(shift_date)
                   shift_date = shift_date.replace("'","")
                   shift_date = shift_date.replace(",","")
                   shift_date = shift_date.replace("(","")
                   shift_date = shift_date.replace(")","")
                   shift_date = shift_date.replace(" ","")
                   shift_date1 = p,'月',k,'日',
            #      print(p,'月',k,'日',)
                   df = pd.read_csv("历史数据2.csv",)
                   timechange3 = str(p).rjust(2,'0')
                   timechange4 = str(k).rjust(2,'0')
                   timechange1 = "2015"+timechange3+timechange4
                   #print(timechange1)  # <class 'int'> 
                   timechange2 = str(timechange1)
                   timechange5 = int(timechange2)
                   df2 = pd.read_csv("results.csv",encoding = 'gb2312')
            #      print(df2)
                       
                   from datetime import datetime
                   timechange6 = datetime(2015,p,k,)
                   import datetime
    #              now = datetime.datetime.now()
                   date = timechange6 + datetime.timedelta(days = day)
                   datet = date
                   datee = timechange6 - datetime.timedelta(days = see)
                   dateet = datee
                   from datetime import datetime
                   date = datetime.strptime(str(date)[0:10], "%Y-%m-%d")
                   datee = datetime.strptime(str(datee)[0:10], "%Y-%m-%d")
                   datenew = str(date)[0:10]
                   dateenew = str(datee)[0:10]
                   date3 = datenew.replace("-","")
                   datee3 = dateenew.replace("-","")
                   dateJ = int(date3[4:6])
                   datek = int(date3[6:8])
                   date5 = int(date3[0:4]+str(dateJ)+str(datek))
                   date3 = int(date3)
                   datee3 = int(datee3)
                   date1 = datenew[5:7]
                   date1 = int(date1)
                   date2 = datenew[8:]
                   date = str(date1)+"月"+date2+"日"
                   datee1 = dateenew[5:7]
                   datee1 = int(datee1)
                   datee2 = dateenew[8:]
                   datee = str(datee1)+"月"+datee2+"日"
                   from datetime import datetime                
                   import datetime
                   bulen = 'false'
                   while bulen == 'false':
                       for check3 in df2.日期:
                           if shift_date in check3:
            #                 print(shift_date)
                              bulen = 'ture'
                       if bulen == 'false':    
                           import datetime
                           timechange6 = timechange6 - datetime.timedelta(days = 1)
                           from datetime import datetime
                           dateex = datetime.strptime(str(timechange6)[0:10], "%Y-%m-%d")
                           dateexnew = str(dateex)[0:10]
                           dateex3 = dateexnew.replace("-","")
                           dateex3 = int(dateex3)
                           dateex1 = dateexnew[5:7]
                           dateex1 = int(dateex1)
                           dateex2 = dateexnew[8:]
                           shift_date = str(dateex1)+"月"+dateex2+"日"                           
                           continue
            #              now = datetime.datetime.now()  
                       break
            #      if bulen == 'ture':  
                   bulen = 'false'
                   while bulen == 'false':
                       for check in df2.日期:
                           if date in check:
            #                 print(date)
                              bulen = 'ture'
                       if bulen == 'false':   
                            import datetime
                            datet = datet - datetime.timedelta(days = 1)
                            from datetime import datetime
                            date = datetime.strptime(str(datet)[0:10], "%Y-%m-%d")
                           #datee = datetime.strptime(str(datee)[0:10], "%Y-%m-%d")
                            datenew = str(date)[0:10]
                           #dateenew = str(datee)[0:10]
                            date3 = datenew.replace("-","")
                           #datee3 = dateenew.replace("-","")
                            dateJ = int(date3[4:6])
                            datek = int(date3[6:8])
                            date5 = int(date3[0:4]+str(dateJ)+str(datek))
                            date3 = int(date3)
                           #datee3 = int(datee3)
                            date1 = datenew[5:7]
                            date1 = int(date1)
                            date2 = datenew[8:]
                            date = str(date1)+"月"+date2+"日"
              #             print(date)
                           #datee1 = dateenew[5:7]
                           #datee1 = int(datee1)
                           #datee2 = dateenew[8:]
                           #datee = str(datee1)+"月"+datee2+"日"
                            continue
                       break
                   bulen = 'false'
                   while bulen == 'false':
                       for check2 in df2.日期:
                           if datee in check2:
            #               print(datee)
                              bulen = 'ture'
                       if bulen == 'false':
                             import datetime
                             dateet = dateet - datetime.timedelta(days = 1)
                             from datetime import datetime
                             datee = datetime.strptime(str(dateet)[0:10], "%Y-%m-%d")
                             dateenew = str(datee)[0:10]
                             datee3 = dateenew.replace("-","")
                             datee3 = int(datee3)
                             datee1 = dateenew[5:7]
                             datee1 = int(datee1)
                             datee2 = dateenew[8:]
                             datee = str(datee1)+"月"+datee2+"日"
            #                print(datee)
                             continue
                       break

                   print(date,'交易持仓到期日',shift_date,'交易发生日',datee,'观察日')
                   
                   for line3 in df2.日期:                   
                       if line3 in datee:  
                           df2 = df2[df2['日期'].isin([line3])]
                           df2 = df2.主力空.values
                           df2 = str(df2)
                           df2 = df2.replace("[","")
                           df2 = df2.replace("]","")
                           df2 = df2.replace('"',"")
                           df2 = df2.replace("'","")
                           df2 = df2.replace(" ","")
            #              df2_array = np.array(df2)
                           #7777777777 然后转化为list形式
            #              df2_list = df2_array.tolist()
                           df2_list = df2.split(",") #or list2 = str2.split(" ")
            #              print(df2_list)
                           #主力多
                           df = pd.read_csv(r"历史数据2.csv",)
            #              conversion_date(line3)
            #              print(timechange1)
                           df = df[df['TRADE_DT'].isin([datee3])]
                           db = df.S_INFO_WINDCODE
                           db_array = np.array(db)
                           db_list = db_array.tolist()
            #              print(db_list) #当天所有有交易的期货名称list
            #              db = str(db.values)
            #              print(db_list)
                           df = pd.read_csv(r"历史数据2.csv",)
            #              conversion_date(line3)
            #              print(timechange1)
                           df = df[df['TRADE_DT'].isin([date3])]
                           db = df.S_INFO_WINDCODE
                           db_array = np.array(db)
                           db_list2 = db_array.tolist()
            #              print(db_list2) #当天所有有交易的期货名称list
                           """
                           db = df2.replace("[","")
                           db = df2.replace("]","")
                           db = df2.replace('"',"")
                           print(db)
                           db_list = db.split(" ")
                           print(db_list)               
                           """               
                           #在datetime模块中有timedelta类，这个类的对象用于表示一个时间间隔，比如两个日#期或者时间的差别。
                           #计算两个日期的间隔
    
                           # for cc in range(30,52):
                               #shu = ((close-close)*((10000000/len(df2_list)/close)) #收益计算
                               #shu = sum(shu)
                               # cc = cc+10
            #              def closetime(df2_list):
                           arr = []
                           arr1 = []
                           for line2 in iter(df2_list):
                               for line4 in db_list:#观察日
                                   if line2 in line4:
                                       df = pd.read_csv(r"历史数据2.csv",)
                        #              conversion_date(line3)
                        #              print(timechange1)
                                       df = df[df['TRADE_DT'].isin([dateex3])]#当日
                                       df = df[df['S_INFO_WINDCODE'].isin([line4])]
                        #              print(line4)
                                       close = df.S_DQ_CLOSE.values
                                       # if df.S_DQ_CLOSE.empty == 'Ture':
                                       #    df = df[df['TRADE_DT'].isin([timechange5])]
                                       arr.append(close) 
                        #              print(arr)
                           for line2 in iter(df2_list):
                               for line4 in db_list:#持仓到期日,已经改成观察日#（未經過嚴謹判斷）
                                   if line2 in line4:
                                       df = pd.read_csv(r"历史数据2.csv",)
                        #              conversion_date(line3)
                        #              print(timechange1)
                                       df = df[df['TRADE_DT'].isin([date3])]#持仓到期日
                        #              print(date3)
                                       df = df[df['S_INFO_WINDCODE'].isin([line4])]
                        #              print(line4)
                                       close = df.S_DQ_CLOSE.values
                        #              print(df.S_DQ_CLOSE.empty)
                                       arr1.append(close) 
                        #              print(arr1)            
    #                      for line5 in arr:
                                #shu = ((close-close)*((10000000/len(df2_list)/close)) #收益计算
                                #shu = sum(shu)
                           print(arr,arr1)
                           arr2 = []
                           pk,kp = 0,0
                           bulen1 = 'false'
                           for arrline3 in arr:
                               if len(arrline3) == 0:
                                   pk = pk+1
                           for arrline4 in arr1:
                               if len(arrline4) == 0:
                                   kp = kp+1
                           pkk = 0
                           """ 
                           for arrline in arr:
                                pkk = pkk+1  
                                bulen1 == 'false'
                                for arrline2 in arr1:
                                    if bulen1 == 'false':
                                       if len(arrline) != 0 or len(arrline2) != 0:
                                            if len(arr) >= len(arr1):
                                                shouy = (arrline2-arrline)*(10000000/(len(arr1)-kp))
                                                bulen1 == 'ture'
                                            else:
                                                shouy = (arrline2-arrline)*(10000000/(len(arr)-pk))
                                                bulen1 == 'ture'
                                            arr2.append(shouy) 
                           """                                                           
                                                   
                           for arrline in arr:                              
                               arrline2 = arr1[pkk] 
                               pkk = pkk+1
                               if len(arrline) != 0 and len(arrline2) != 0:
                                    if len(arr) >= len(arr1):
                                        shouy = (arrline2-arrline)*(10000000/(len(arr1)-kp))#kp数量是当日close为空值的值的数量
                           #            bulen1 == 'ture'
                                    else:
                                        shouy = (arrline2-arrline)*(10000000/(len(arr)-pk))
                           #            bulen1 == 'ture'
                                    arr2.append(shouy) 
                           print(arr2)
                           arr4.append(sum(arr2))
           nh = ((sum(arr4)/10000000)/(day*time))*365*0.01           
           print(nh,'%')
                                       #默认资金设置为10000000
                                       #在特定的日子里，有些期货单位无法找到close值
                                         
                   
           # 有些close没有具值
                      
                               
                        
                        
                    