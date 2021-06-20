import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#一、系列Series
#系列是具有均匀数据的一维数组结构
#方法pandas.Series(data,index,dtype=None,copy=False)
#data:传入的数据参数，数据类型支持数组列表等
#index:索引，与数据的长度相同,没有的话就是从零开始的数列
#dtype:数据的类型，默认为float
#copy:复制一份数据
data=np.array(['a','b','c','d'])
index=[100,200,300,400]
obj=pd.Series(data,index)
print(obj)
obj=pd.Series(data)
print(obj)

#二、数据帧DataFrame
#数据帧是一个具有异构数据的二维数组
#方法pandas.DataFrame(data,index,columns,dtype,copy=False)
#columns:列参数
data={'name':['tom','jack','steve','ricky'],'age':[28,19,22,20]}
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)

#三、面板Panel
#面板是具有异构数据的三维数据结构，一个面板可以说明为DataFrame的容器
#方法pandas.Panel(data,items,major_axis,minjor_axis,dtype,copy=False)
#items:axis0,每个项目对应于内部包含的数据帧
#major_axis:axis1,表示每个数据帧的行
#minjor_axis:axis2,表示每个数据帧的列
data={'item1':pd.DataFrame(np.random.randn(4,3)),
      'item2':pd.DataFrame(np.random.randn(4,3))}
#p=pd.Panel(data)
#print(p['item1'])

#数据统计
d={'name':pd.Series(['tom','james','ricky','vin','steve','minsu','jack','lee','david','gasper','betina','andres']),
   'age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df=pd.DataFrame(d)
print(df)
#统计数据
print('数据之和:\n',df.sum())
#数据之和:
#name      tomjamesrickyvinsteveminsujackleedavidgasperbe...
#age                                                     382
#rating                                                44.92
#dtype: object

print('数据均值:\n',df.mean())
#数据均值:
#age       31.833333
#rating     3.743333
#dtype: float64

print('标准偏差:\n',df.std())
#标准偏差:
#age       9.232682
#rating    0.661628
#dtype: float64

#其他统计方法
#count():非空观测数量
#median():中位数
#mode():值的模值
#min():所有值中的最小值
#max():所有值中的最大值
#abs():绝对值
#prod():数组元素的乘积
#cumsum():数组元素的累加和
#cumprod():累计乘积


#pandas处理丢失值
df=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])
df=df.reindex(['a','b','c','d','e','f','g','h'])#reindex重构索引
print(df)

#isnull()和notnull()函数处理缺失值
print(df['one'].isnull())
print(df.isnull())
print(df.notnull())

#清理/填充缺少数据
#1、用标量0替代缺失值
print(df.fillna(0))
#2、用缺失值的前一行替代缺失值
print(df.fillna(method='pad'))
#3、剔除缺失值
print(df.dropna(axis=0))#axis为0表示作用在行上，1表示作用在列上
print(df.dropna(axis=1))
#4、忽略缺失值
print(df.dropna())
#5、设置任意值替换
df=pd.DataFrame({'one':[10,20,30,40,50,2000],
                'two':[1000,0,30,40,50,60]})
print(df)
print(df.replace({1000:10,2000:60}))


#pandas处理稀疏数据
df=pd.DataFrame(np.random.randn(10000,4))
df[:9998]=np.nan
#sdf=df.to_sparse()
#调用to_dense标准密集进行稀疏数据处理
#print('稀疏数据集:\n',sdf.to_dense())
#稀疏率
#print('稀疏率:\n',sdf.density)


#pandas文件操作
#读取Excel文件
#file=pd.read_excel("D:\\Users\\LWZ\\Wechat\\WeChat Files\\wxid_9mh6wr6ojg8122\\FileStorage\\File\\2021-06\\图像算法组暑期集训安排表.xlsx")
file=pd.read_csv("D:\\Dataset\\Data.csv")
print(file)


#pandas可视化
#1、绘制折线图
df=pd.DataFrame(np.random.randn(10,4),
                index=pd.date_range('2020/6/20',periods=10),
                columns=list('ABCD'))
df.plot()
plt.show()

#2、绘制条形图
df=pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
df.plot.bar()
plt.show()

#3、绘制堆积条形图
df.plot.bar(stacked=True)
plt.show()

#4、绘制水平条形图
df.plot.barh(stacked=True)
plt.show()

#5、绘制直方图
df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000)-1},columns=['a','b','c'])
df.plot.hist(bins=20)
plt.show()

#6、绘制多个直方图
df.hist(bins=20)
plt.show()

#7、绘制箱型图
df=pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
df.plot.box()
plt.show()

#8、绘制区域块图形
df=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.area()
plt.show()

#9、绘制散点图
df=pd.DataFrame(np.random.rand(50,4),columns=['a','b','c','d'])
df.plot.scatter(x='a',y='b')
plt.show()

#10、绘制饼状图
df=pd.DataFrame(3*np.random.rand(4),index=['A','B','C','D'])
df.plot.pie(subplots=True)
plt.show()