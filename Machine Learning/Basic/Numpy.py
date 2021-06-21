import numpy
import numpy as np

#Numpy的数组类称为ndarry

a=np.random.random(4)#生成一个浮点数组
# print(a)
print(a.T)#返回ndarry的转置，如果维度小于2，放回self.与transpose()相同
a.transpose()#与T相同
print(a.shape)
print(a.size)#size返回数组中元素的个数，相当与shape元素的乘积
print(a.itemsize)#等价于3ndarry.dtype.itemsize
print(a.dtype)#返回数组中元素的数据类型
print(a.ndim)#返回数组的轴（维度）的数量，维度的数量通常被称为rank
print(a.shape)#数组的维度，（行，列）
print(a.data)#data中包含了数组的实际元素
for i in a.data:
    print(i)

print(a.flat)#返回数组的一维迭代器
for i in a.flat:
    print(i)

print(a.imag)#返回数组的虚部
print(a.real)#返回数组的实部
print(a.nbytes)#数组中所有元素的字节长度

print(set(np.typeDict.values()))#查看Numpy数据类型

#numpy将列表或数组转换为ndarray方法numpy.array(object,dtype=None,copy=True,order=None,sunok=False,ndmin=0)
#object:输入对象列表数组等
#dtype:数据类型，不说明默认类型为保存对象所需的最小类型
#copy:表示是否复制对象
#order:顺序
#subok:表示子类是否被传递

#arange函数生成数组
#arange(start=None,stop=None,step=None,dtype=None)，生成一个ndarry
#与range不同的是arange中的step可以是小数，dtype为可选参数
b=np.arange(1,2,0.1)
print(b)

#linspace生成等差数列
#numpy.linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)
#num:生成的样本数
#endpoint:为True时最后一个样本包含在序列中
#retstep:为True时返回间距

c=np.linspace(1,5,num=10)
print(c)

#生成等比数列
#numpy.logspace(start,stop,num=50,endpoint=True,base=10.0,dtype=None)
#base:基底

d=np.logspace(0,2,num=10)#生成首位是10的0次方，末位是10的2次方，含10个数的等比数列
print(d)

#创建一个全为1的数组
#numpy.ones(shape,dtype=None,order='C')
#order:规定返回数组元素在内存中的存储顺序，C为C语言，F为Fortran语言
e=np.ones((2,3))
print(e)
f=np.ones(2)
print(f)

#生成全为0的数组
g=np.zeros((3,2))
print(g)

#返回一个空数组
h=np.empty((3,3))
print(h)
i=np.empty_like(h)#生成一个像h的空数组
print(i)

#生成对角线元素为1，，其他元素为0的数组
#numpy.eye(N.M=None,k=0,dtype=float)
#N:整数，数组的行数
#M:整数，数组的列数。默认等于N
#k:整数，对角线的序号，0对应主对角线，正为上三角，负为下三角
j=np.eye(3,6,1)
print(j)
j=np.eye(4,k=-2)
print(j)

#创建n为单位方阵
#numpy.identity(n,dtype=None)
#dtype:默认float
k=np.identity(5,int)
print(k)


#索引机制
print(k[2])
print(k[2][2])#与k[2,2]相同
print(k[[2,3,4]])#同时选择多个元素，在这相当于选3，4，5行
#切片机制
#在Numpy中，尤其是在做数组运算或数组操作时，返回结果不是数组的副本就是视图。
#在Numpy中，所有赋值运算不会为数组和数组中的任何元素创建副本。数组切片操作返回的对象只是原数组的视图。
#numpy.ndarray.copy()函数创建一个副本。对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置。
#对python列表进行切片操作得到的数组是原数组的副本，而对Numpy数据进行切片操作得到的数组则是指向相同缓冲区的视图。

#[开始索引:结束索引:步长值]
print(k[1:])#选择下标为一的元素到最后一个元素
print(k[1:2,2:3],k[2,3])#前者返回列表，后者返回一个值
#利用负数下标翻转数组
print("k=\n{}\nk-=\n{}\n".format(k,k[::-1]))

#一维数组切片
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(x[0:2])  # [1 2]
#用下标0~5,以2为步长选取数组
print(x[1:5:2])  # [2 4]
print(x[2:])  # [3 4 5 6 7 8]
print(x[:2])  # [1 2]
print(x[-2:])  # [7 8]
print(x[:-2])  # [1 2 3 4 5 6]
print(x[:])  # [1 2 3 4 5 6 7 8]
#利用负数下标翻转数组
print(x[::-1])  # [8 7 6 5 4 3 2 1]

#二维数组切片
x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(x[0:2])#第零行到第3行
# [[11 12 13 14 15]
#  [16 17 18 19 20]]

print(x[1:5:2])#第2行到第5行，步长为2
# [[16 17 18 19 20]
#  [26 27 28 29 30]]

print(x[2:])#第3行到最后一行
# [[21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]

print(x[:2])#第0行到第2行
# [[11 12 13 14 15]
#  [16 17 18 19 20]]

print(x[-2:])#倒数第2行到最后一行
# [[26 27 28 29 30]
#  [31 32 33 34 35]]

print(x[:-2])
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

print(x[:])
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]

print(x[2, :])#第3行全部元素
#[21 22 23 24 25]

print(x[:, 2])#第3列元素
#[13 18 23 28 33]

print(x[0, 1:4])#第一行第2列到第4列元素
#[12 13 14]

print(x[1:4, 0])
#[16 21 26]

print(x[1:3, 2:4])#第1到第3行和第3到第4列的元素
# [[18 19]
#  [23 24]]

print(x[:, :])
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]

print(x[::2, ::2])#行和列的读取步长都为2
# [[11 13 15]
#  [21 23 25]
#  [31 33 35]]

print(x[::-1, :])#将行反转
# [[31 32 33 34 35]
#  [26 27 28 29 30]
#  [21 22 23 24 25]
#  [16 17 18 19 20]
#  [11 12 13 14 15]]

print(x[:, ::-1])#将列反转
# [[15 14 13 12 11]
#  [20 19 18 17 16]
#  [25 24 23 22 21]
#  [30 29 28 27 26]
#  [35 34 33 32 31]]


#矩阵的合并
#numpy.vstack((A,B))将A,B进行上下合并
#numpy.hstack((A,B))将A,B进行左右合并
a=np.identity(3)
b=np.eye(3,3)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
#矩阵的分割
#numpy.column_stack()支持列方向上的合并，处理一维按列方向组合(结果为二维)，二维和hstack一样
#numpy.row_stack()支持行方向上的合并，处理一维按行方向组合，二维和vstack一样
from numpy import newaxis
np.column_stack((a,b))
a=np.array([1,2])
b=np.array([3,4])
c=np.column_stack((a,b))
print(c)
d=np.hstack((a,b))
print("a=\n{}\nb=\n{}\nc=\n{}\nd=\n{}\n".format(a,b,c,d))
#newaxis插入新的维度，有一维变为二维
e=np.column_stack((a[:,newaxis],b[:,newaxis]))
f=np.hstack((a[:,newaxis],b[:,newaxis]))
print("e=\n{}\nf=\n{}\n".format(e,f))




#利用字典来定义结构
personType = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['U30', 'i8', 'f8']})

a = np.array([('Liming', 24, 63.9), ('Mike', 15, 67.), ('Jan', 34, 45.8)],
             dtype=personType)
print(a, type(a))
# [('Liming', 24, 63.9) ('Mike', 15, 67. ) ('Jan', 34, 45.8)]
# <class 'numpy.ndarray'>

#利用包含多个元组的列表来定义结构
personType = np.dtype([('name', 'U30'), ('age', 'i8'), ('weight', 'f8')])
a = np.array([('Liming', 24, 63.9), ('Mike', 15, 67.), ('Jan', 34, 45.8)],
             dtype=personType)
print(a, type(a))
# [('Liming', 24, 63.9) ('Mike', 15, 67. ) ('Jan', 34, 45.8)]
# <class 'numpy.ndarray'>

# 结构数组的取值方式和一般数组差不多，可以通过下标取得元素：
print(a[0])
# ('Liming', 24, 63.9)

print(a[-2:])
# [('Mike', 15, 67. ) ('Jan', 34, 45.8)]

# 我们可以使用字段名作为下标获取对应的值
print(a['name'])
# ['Liming' 'Mike' 'Jan']
print(a['age'])
# [24 15 34]
print(a['weight'])
# [63.9 67.  45.8]