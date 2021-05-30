import scipy
import numpy as np
from scipy.misc import derivative  #scipy.misc模块下的derivative函数求函数的导数值

def f(x):#定义函数
    return x**5
print(derivative(f,2,dx=1e-6))#对函数在x=2处求导

#使用numpy模块poly1d函数构造f(x)  #ploy(数字1)d
#poly1d函数的形参是多项式的系数，最左侧为最高次数的系数

#构建多项式(x**5+2*x**4+3*x**2+5)
p=np.poly1d([1,2,0,3,0,5])
print(p)
#使用polyder函数求导
print(np.polyder(p,1))#一阶导
print(np.polyder(p,2))#二阶导
#求导数值
print(np.polyder(p,2)(1))#二阶导在x=1处的值

#deriv函数和polyder函数使用差不多
print(p.deriv(2)(1))#二阶导在x=1出的值