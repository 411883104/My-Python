
stu={"id":123,"sex":"m"}
#获取值
print(stu["id"])
print(stu)
#使用get()获取键值
#第一个参数指定键（必不可少），第二个键不存在时返回的值（可选的）
print(stu.get(abs,"no"))
print(stu.get("id","no"))
print(stu.get("abc"))

#添加键值
stu["grade"]=100
print(stu)

#删除键值
del stu["sex"]
print(stu)

#遍历字典 items()函数
for k,v in stu.items():
    print(k,v)

#遍历字典中所有的键 keys()
for k in stu.keys():
    print(k)
for k in stu:#与keys()等价
    print(k)


#遍历字典中所有的值用values()
for v in stu.values():
    print(v)


#set()用于去除重复元素
list=[1,2,1,3,2,2,4,1,2]
print(list)
print(set(list))
