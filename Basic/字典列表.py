#字典列表
stu1={"id":121,"sex":"m"}
stu2={"id":122,"sex":"w"}
list=[stu1,stu2]
print(list)
for i in list[:1]:
    print(i)
#在字典中存列表
stu={"id":123,"sex":"m","grade":[95,100,98]}
for i in stu["grade"]:
    print(i)
for k,v in stu.items():
    print(k)
    if k=="grade":
        for i in v:
            print(i)

#字典中存字典
stu1={"id":123,"sex":"m"}
stu={"one":stu1}
print(stu)