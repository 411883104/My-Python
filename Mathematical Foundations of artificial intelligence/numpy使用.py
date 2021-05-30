import numpy as np

a=np.array([1,2,3])#创建一个秩为1的数组
print(a)
print(a[0],a[1],a[2])
b=np.array([[1,2,3],[4,5,6]])#创建一个秩为2的数组
print(b)
print(b[1,1],b[0,2])
print(np.mgrid[1:3:1])#区间为左闭右开

#mgrid函数（返回一个密集的多为网格）
#np.mgrid[start:end:step] 中括号
print(np.mgrid[-1:4:2])
c=np.mgrid[-1:4:2,-3:1:1]#左边按列展开，右边按行展开
print(c)