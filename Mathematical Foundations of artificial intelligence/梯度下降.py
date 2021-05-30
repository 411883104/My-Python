import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sympy import*
from sympy.abc import x,y,z,f
#定义函数
f=x-y+2*x**2+2*x*y+y**2
def Fun(x_,y_):
    return f.evalf(subs={x:x_,y:y_})
#对函数求偏导
def Fx(x_,y_):
    return diff(f,x).evalf(subs={x:x_,y:y_})
def Fy(x_,y_):
    return diff(f,y).evalf(subs={x:x_,y:y_})

#梯度下降
step=0.00008#取步长
x_=0
y_=0
new_x=x_
new_y=y_
over=false
while over==false:
    new_x-=step*Fx(x_,y_)
    new_y-=step*Fy(x_,y_)
    if Fun(x_,y_)-Fun(new_x,new_y)<7e-9:
        over=true
    x_=new_x
    y_=new_y
print(Fun(x_,y_))
print(x_,y_)