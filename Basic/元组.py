'''
list=[1,2,3,4]
print(list)
print(list[2])
print(list[-1])#-1表示列表最后的元素
print(list[-2])#-2表示倒数第二的元素,以此类推

#在列表末尾增加元素用append()函数
list.append(5)
print(list)

#从列表中插入元素用insert()函数
list.insert(3,8) #表示在下标3的位置插入元素8
print(list)

#删除元素
#用del函数
del list[3]
print(list)

#用pop函数
#(删除列表末尾的元素)
a=list.pop()
print(a)
print(list)
#(删除列表任意处元素)
a=list.pop(1)#删除下标为1的元素
print(a)
print(list)

#根据值删除元素用remove函数
list.remove(3)#删除元素3
print(list)
'''

'''
list=[2,4,5,2,8,6,9,0]
#对列表永久性排序sort
list.sort()
print(list)
#对列表临时性排序sorted
list=[2,4,5,2,8,6,9,0]
print(sorted(list))
print(list)
#反转列表
list.reverse()
print(list)
#确定列表长度
print(len(list))

#遍历列表
list=[2,4,5,2,8,6,9,0]
for i in list:
    print(i)
'''

# #循环
# #使用range函数
# for i in range(1,9):#打印区间左闭右开
#     print(i)


'''
#range函数
#range(start,stop,step)
#将数字转换为一个列表，可使用list()
# list=list(range(1,9))
# print(list)
list=list(range(2,11,2))
print(list)

#计算列表总和
print(sum(list))
#最小值
print(min(list))
#最大值
print(max(list))

#创建列表
list=[i**2 for i in range(1,6)]
print(list)

#使用列表某部分
print(list[1:3])#打印下表为1到3的元素
print(list[1:])#打印下标1后面的所有元素
print(list[:4])#从列表开始处打印
'''

# #遍历切片
# list=list(range(2,11,2))
# for i in list[:2]:
#     print(i)
# num=list
# print(num)  #num和list指向同一个列表
#
# num=list[:] #复制列表,得到两个列表
# print(num)




# #元组中的元素不能修改
# ele=(1,2,3,4,5)
# print(ele)
# print(ele[0])
# print(ele[-1])
# print(ele[:])
# # ele[0]=2#错误，不能修改
# #遍历元组
# for i in ele:
#     print(i)
# ele=(5,4,3,2,1)#给元组重新赋值
# print(ele)
# #判断元素是否在列表或元组中
# print(4 in ele)
# print(100 in ele)