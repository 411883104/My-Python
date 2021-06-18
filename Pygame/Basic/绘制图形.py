import pygame,sys

pygame.init()#初始化pygame
#创建500像素宽和400像素高的窗口
#set_model()函数返回一个pygame.Surface对象
windowSurface=pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('hello world!')#设置标题

#设置颜色变量（pygame中表示颜色的数据结构是三个整型的元组(RGB)）
#创建常量来保存
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#使用pygame.draw.polygon()函数绘制任意的多边形
#函数参数：
#1.要在其上绘制多边形的Surface对象
#2.多边形的颜色
#3.要一次绘制的xy坐标所构成的元组，最后一个元组将自动连接到第一个元组
#4.可选项，表示多边形线条的宽度的整数值，没有的话多边形会自动填充
pygame.draw.polygon(windowSurface,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.display.update()

#使用pygame.draw.line()函数绘制任意的直线
#函数参数：
#1.要在其上绘制多边形的Surface对象
#2.直线的颜色
#3.直线一端的xy坐标所构成的元组
#4.直线另一端的xy坐标所构成的元组
#5.可选项，表示线条的宽度的整数值
pygame.draw.line(windowSurface,BLUE,(60,60),(120,60),5)
pygame.draw.line(windowSurface,GREEN,(120,60),(60,120),5)
pygame.draw.line(windowSurface,RED,(60,120),(120,120),5)
pygame.display.update()

#使用pygame.draw.circle()函数绘制任意的圆形
#函数参数：
#1.要在其上绘制多边形的Surface对象
#2.圆的颜色
#3.圆心的xy坐标所构成的元组
#4.圆的半径的整数值
#5.可选项，表示线条的宽度的整数值，宽度值0表示填充圆
pygame.draw.circle(windowSurface,WHITE,(300,50),20,0)
pygame.display.update()

#使用pygame.draw.ellipse()函数绘制任意的椭圆形
#函数参数：
#1.要在其上绘制多边形的Surface对象
#2.椭圆的颜色
#3.椭圆的左上角的xy坐标以及椭圆的宽和高的四个整数的一个元组
#5.可选项，表示线条的宽度的整数值，宽度值0表示填充椭圆
pygame.draw.ellipse(windowSurface,GREEN,(300,250,40,80),1)
pygame.display.update()

#使用pygame.draw.rect()函数绘制任意的矩阵
#函数参数：
#1.要在其上绘制多边形的Surface对象
#2.矩阵的颜色
#3.矩阵左上角的xy坐标以及矩阵的宽和高所构成的元组，也可以只传递一个Rect对象
basicFont=pygame.font.SysFont(None,48)

text=basicFont.render("Hello,world!",True,WHITE,BLUE)
textRect=text.get_rect()
pygame.draw.rect(windowSurface,RED,(textRect.left-20,textRect.top-20,textRect.width+40,textRect.height+40))
pygame.display.update()

while True:
    pass