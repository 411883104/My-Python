import pyforest
import pandas as pd
#python 内置读取文件函数open()
data=pd.read_csv("D:\\Wage.csv")
file=open(r'D:\wage.csv')
#文件读取read()，readlines()
#文件关闭close()
print(file.read())
file.close()