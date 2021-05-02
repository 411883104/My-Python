import math #使用math库
a=math.sqrt(9)
b=math.sqrt(8)
print(a,b)

print(math.ceil(b))#往上取整
print(math.floor(b))#往下取整
print(math.exp(2))#e的次方
print(math.asin(1))#计算arcsin
print(math.pi)#圆周率近似值
print(math.e)#e的近似值

#函数ln(x)表示math.log(),默认以e为底
#函数loga(x)以a为底表示math.log(x,a)
print(math.log(math.e))
print(math.log(2,2))

ans=1
for i in range(1,16):
    ans*=i
print(ans)