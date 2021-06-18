import pygame,time,sys
from pygame.locals import*
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

#设置字体
#第一个参数是字体的名称，第二个是字体的大小
basicFont=pygame.font.SysFont(None,48)#None为系统默认字体

#生成Font对象（渲染）
#使用Font对象中render()函数，函数返回Surface对象
#render()第一个参数是要绘制的字符串，第二个指定是否想要抗锯齿的一个Boolean值
#第三第四参数是RGB元组，第三个参数是将要用来渲染文本的颜色，第四个参数是文本后的背景颜色
text=basicFont.render("Hello,world!",True,WHITE,BLUE)#将Font对象赋值给变量text

#使用rect属性设置文本位置
#pygame.Rect数据类型表示特定大小和位置的矩阵区域
#调用pygame.rect()来创建一个新的Rect对象。
#pygame.Rect(left,top,width,height)
#函数参数表示左上角的X坐标和Y坐标，接着是宽度和高度，都是以像素为单位
#当我们创建Font对象是已经生成了一个Rect对象，访问使用get_rect()
textRect=text.get_rect()#在text上使用get_rect()
#Rect对象已经存储了Rect的中心的x和y坐标，名为centerx和centery
#使用windowSurface.get_rect()获取
textRect.centerx=windowSurface.get_rect().centerx
textRect.centery=windowSurface.get_rect().centery

#用颜色填充Surface对象
#使用fill()函数
windowSurface.fill(WHITE)
#在pygame中调用fill()或其他任何绘制函数时，屏幕上的窗口都不会改变
#在调用pygame.display.update()函数前不会将对象绘制到屏幕上
pygame.display.update()

#给像素着色
#创建一个pygame.PixelArrary对象（颜色元组的列表的一个列表）
pixArrary=pygame.PixelArray(windowSurface)
pixArrary[480][380]=BLACK#把坐标(480,380)的像素改变为黑色像素
#从一个Durface对象创建PixelArrary对象会锁定这个Surface对象
#锁定意味着该对项不能调用blit()函数
#使用del操作符删除对象
del pixArrary
pygame.display.update()

#将绘制到windoeSurface上
#使用bilt()函数
windowSurface.blit(text,textRect)#第二个参数指定绘制在何处
pygame.display.update()

#获取事件对象
#pygame.event.get()函数检索上次调用该函数生成的pygame.event.Event对象
#这些事件会以Event对象的一个列表的形式返回，所有的Event都有一个type的对象，它表明事件的类型
#使用QUIT类型的事件（用户终止程序时该事件将告诉我们）

while True:
    #使用for循环遍历pygame.event.get()所返回的列表中的每一个对象
    for event in pygame.event.get():
        #QUIT在模块pygame.locals中
        if event.type==QUIT:
            pygame.quit()#该函数是和init()相对应的一种函数
            sys.exit()