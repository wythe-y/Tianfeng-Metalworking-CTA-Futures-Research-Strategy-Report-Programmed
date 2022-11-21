import pandas as pd
import pandas
import csv

scores = pandas.read_csv("历史数据2.csv",)
print('------ 当前表格：')
print(scores)

print('------ 开始筛选重复数据：')

# 新建个 DataFrame 用来保存过滤后的数据
new_scores = pandas.DataFrame()
# 用来标记是否已存在
existed_name = {}
for index, row in scores.iterrows():
    if row['S_INFO_WINDCODE'] in existed_name:
        print('发现重复项：', row['S_INFO_WINDCODE'])
        continue
    existed_name[row['S_INFO_WINDCODE']] = True
    new_scores = new_scores.append(row, ignore_index=True)

print('------ 筛选后的表格：')
print(new_scores)

print('------ 正在保存到新表格中')
new_scores.to_excel('S_INFO_WINDCODE.xlsx', index=False)

a = 0
print('------ 完成！') 
df = pd.read_excel('S_INFO_WINDCODE.xlsx')
with open("S_INFO_WINDCODE.csv",'w+',newline='') as t2:#numline是来控制空的行数的
    tit=["WINDCODE",]
    writer=csv.writer(t2)#这一步是创建一个csv的写入器
    writer.writerow(tit)#写入标签
    for line in df.S_INFO_WINDCODE:
        line = line[0:2]
        a = ''.join([i for i in line if not i.isdigit()]) #删除数字
        writer.writerow([a])
        t2.close
        

        