import numpy as np
import sympy
#单定积分计算使用scipy库中的quad函数
#形式为scipy.integrate.quad(f,a,b)，f为被积函数，a和b为积分下限和上限
from scipy.integrate import quad

x=sympy.Symbol('x')
def f(x):#定义函数
    return np.cos(np.exp(x))**2
#也可用lambda定义函数
f=lambda x:np.cos(np.exp(x))**2
print(quad(f,0,3))

#二重积分dblquad
from scipy.integrate import dblquad
'''
形式为scipy.integrate.dblquad(func,a,b,gfun,hfun)
func为被积函数，a,b为变量x的下限和上限
gfun和hfun是定义变量y的下限和上限
即使gfun和hfun为常数也要定义为函数
'''
def integrand(x,y):
    return np.exp(-x**2-y**2)
x_a=0
x_b=10
y_a=0
y_b=10
print(dblquad(integrand,x_a,x_b,lambda x:y_a,lambda x:y_b))

#quad和dblquad函数返回积分值和误差两个值
