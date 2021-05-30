import sympy
from sympy import oo   #无穷符号用两个小写字母oo表示

#计算sin(x)/x在x->oo的极限
x=sympy.Symbol('x')
f=sympy.sin(x)/x
print(sympy.limit(f,x,oo))
#计算sin(x)/x在x->0的极限
print(sympy.limit(f,x,0))

from sympy import*
#求导
#diff求导函数，arcsin数学函数表示形式为asin
from sympy.abc import x,y,z,f
print(diff(asin(sqrt(sin(x)))))

#求偏导
f=x**2+3*x*y+y**2
print(diff(f,x))#对x求偏导
print(diff(f,y))#对y求偏导
fx=diff(f,x)
print(fx.evalf(subs={x:1,y:2}))#以字典的形式传入多个变量的值，求函数值
