import sympy

#自然对数e
print(sympy.E)
print(sympy.log(sympy.E))
#无穷大的表示方法
print(1/sympy.oo)
#圆周率表示方法
print(sympy.pi)
print(sympy.sin(sympy.pi))
#n次方根
print(sympy.root(2,3))
#阶乘
print(sympy.factorial(5))
#表达式和表达式求值
x=sympy.Symbol('x')#定义x为一个符号，表示一个变量
fx=2*x+1
print(fx.evalf(subs={x:5}))#用evalf函数求值
x,y=sympy.symbols('x y')#注意为symbols
f=2*x+y
print(f.evalf(subs={x:4,y:5}))#只传入一个会输出原来的表达式
print(f.evalf(subs={y:4}))
#求极限
print(sympy.limit(fx,x,5))
#求导
print(sympy.diff(f,x))