import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.linspace(0.5,3.5,100)#生成0.5到3.5，100个数的等差数列
y=np.sin(x)
y1=np.random.randn(100)#从标准正态分布中取100个数

#1、函数plot()展现变量的趋势变化
#plt.plot(x,y,ls="-",lw=2,label="plot figure")
#x:x轴上的数值
#y:y轴上的数值
#ls:折线图的线条风格
#lw:折线图的线条宽度
#label:标记图形内容的标签文本
x=np.linspace(0.05,10,100)
y=np.cos(x)
plt.plot(x,y,ls="-",lw=2,label="plot figure")
plt.legend()#显示标签label
plt.show()

#2、函数scatter()寻找变量之间的关系
#plt.scatter(x,y,c="b",label="scatter figure")
plt.scatter(x,y,c="b",label="scatter figure")
#c:散点图中标记的颜色
plt.show()

#3、函数xlim()设置x轴的数值显示范围,ylim()设置y轴数值显示范围
#plt.xlim(xmin,xmax)
plt.scatter(x,y,c="b",label="scatter figure")
plt.xlim(2,8)
plt.ylim(-2,2)
plt.show()

#4、函数xlabel()设置x轴的标签文本，ylabel()设置y轴的标签文本
#plt.xlabel(string)
plt.scatter(x,y,c="b",label="scatter figure")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#5、函数grid()绘制刻度线的网格线
plt.grid(linestyle=":",color="r")
plt.scatter(x,y,c="b",label="scatter figure")
plt.show()

#6、函数axhline()绘制平行于x轴的水平参考线,axvline()绘制平行于y轴的竖直参考线
#plt.axhline(y=0.0,c="r",ls="--",lw=2)
#plt.axvline(x=0.0,c="r",ls="--",lw=2)
plt.scatter(x,y,c="b",label="scatter figure")
plt.axhline(y=0.0,c="r",ls="--",lw=2)
plt.axvline(x=0.0,c="r",ls="--",lw=2)
plt.show()

#7、函数axvspan()绘制垂直于x轴的参考区域,axhspan()绘制垂直于y轴的参考区域
plt.axvspan(xmin=1.0,xmax=2.0,facecolor="y",alpha=0.3)
plt.axhspan(ymin=1.0,ymax=2.0,facecolor="y",alpha=0.3)
#alpha:参考区域颜色的透明度
plt.scatter(x,y,c="b",label="scatter figure")
plt.show()

#8、函数annotate()添加图形内容细节的指向型注释文本
#plt.annotate(string,xy=(np.pi/2,1.0),xytext=((np.pi/2)+0.15,1.5),weight="bold",color="b",arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="b"))
#string:图形内容的注释文本
#xy:被注释图形内容的位置坐标
#xytext:注释文本的位置坐标
#weight:注释文本的字体粗细风格
#color:注释文本的字体颜色
#arrowprops:指示被注释内容的箭头的属性坐标
plt.annotate("maximum",
             xy=(np.pi/2,1.0),
             xytext=((np.pi/2)+0.15,1.5),
             weight="bold",
             color="b",
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="b"))
plt.scatter(x,y,c="b",label="scatter figure")
plt.show()

#9、函数text()添加图形内容细节的无指向型注释文本
#plt.text(x,y,string,weight="bold",color="b")
#x,y:注释文本的坐标
plt.text(3,0,"y=sin(x)",weight="bold",color="y")
plt.scatter(x,y,c="b",label="scatter figure")
plt.show()

#10、函数title()添加图形内容的标题
#plt.title(string)
plt.title("y=sin(x)")
plt.scatter(x,y,c="b",label="scatter figure")
plt.show()

#11、寒素legend()标示不同图形的文本标签图例
#要先有标签才能使用legend函数
plt.scatter(x,y,c="b",label="scatter figure")
plt.legend(loc="lower left")
plt.show()



#使用统计函数
x=[1,2,3,4,5,6,7,8]
y=[3,1,4,5,8,9,7,2]
#1、函数bar()绘制柱状图
# def bar(x: Any,
#         height: Any,
#         width: float = 0.8,
#         bottom: Any = None,
#         *,
#         align: str = 'center',
#         data: Any = None,
#         **kwargs: Any) -> Any
plt.bar(x,y,align="center",color="c",tick_label=["q","a","c","e","r","j","b","p"],hatch="/")
#x:标示在x轴上的定性数据的类别
#y:每种定性数据的类别的数量
plt.show()

#2、函数barh()用于绘制条形图
# def barh(y: Any,
#          width: Any,
#          height: float = 0.8,
#          left: Any = None,
#          *,
#          align: str = 'center',
#          **kwargs: Any) -> Any
plt.barh(x,y,align="center",color="c",tick_label=["q","a","c","e","r","j","b","p"],hatch="/")
plt.show()

#3、函数hist()绘制直方图
# def hist(x: Any,
#          bins: Any = None,
#          range: Any = None,
#          density: bool = False,
#          weights: Any = None,
#          cumulative: bool = False,
#          bottom: Any = None,
#          histtype: str = 'bar',
#          align: str = 'mid',
#          orientation: str = 'vertical',
#          rwidth: Any = None,
#          log: bool = False,
#          color: Any = None,
#          label: Any = None,
#          stacked: bool = False,
#          *,
#          data: Any = None,
#          **kwargs: Any) -> Any