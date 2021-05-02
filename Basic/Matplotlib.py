import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
data=pd.read_csv("D:\\Wage.csv")
print(data)
# data_x = data['age']
# data_y = data['wage']
# #将数据划分为训练集和验证集
# from sklearn.model_selection import train_test_split
# train_x, valid_x, train_y, valid_y = train_test_split(data_x, data_y, test_size=0.33, random_state = 1)
# #对年龄和工资的关系进行可视化
# plt.scatter(train_x, train_y, facecolor='None', edgecolor='k', alpha=0.3)
# plt.show()

x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.plot(x,y,label="two")  #plot()绘制直线
plt.plot(y,y,label="one")
plt.legend()              #绘制标记
plt.title("hello")          #绘制标题
plt.xlabel('X')             #x
plt.ylabel('Y')
# plt.hist(x,y)
plt.show()