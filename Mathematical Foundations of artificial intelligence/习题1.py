#(1)
import numpy as np
import sympy
import math,cmath

# #函数ln(x)表示math.log(),默认以e为底
# #函数loga(x)以a为底表示math.log(x,a)
# print(math.log(math.e))
# print(math.log(2,2))

x=sympy.Symbol('x')
f=sympy.sin(sympy.log(x))
print(sympy.limit(f,x,1))


#(2)
f=(x**(1/3)-2)/(x-8)
print(sympy.limit(f,x,8))

#(3)
f=x**4-2*x**3+5*sympy.sin(x)+sympy.log(3)
print(sympy.diff(f,x))

#(4)
from sympy.abc import x,y,z,f
z=(3*x**2+y**2)**(4*x+2*y)
fx=sympy.diff(z,x)
fy=sympy.diff(z,y)
print(fx)
print(fy)
print(fx.evalf(subs={x:1,y:2}))
print(fy.evalf(subs={x:1,y:2}))

#(5)
z=x**2+y**2