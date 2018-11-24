#coding:utf-8
import csv
#path = ''文件地址
path = ''
#读取某一列
with open(path,'r') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[0] for row in reader]
print(column)
#读取某一行
with open(path,'r') as csvfile:
    reader = csv.reader(csvfile)
    for i,rows in enumerate(reader):
        if i == 0:
            row = rows
