from cv2 import *
import matplotlib.pyplot as  plt

#读取图片函数imread()
'''接收两个参数
1.图片的路径。加载的路径错误不会报错，而是返回None值
2.读取方式(可选)，默认彩色模式加载
'''
image=imread("D:\\Dataset\\BMP\\1.bmp")

#显示图像:cv或matplotlib

#cv显示图像imshow()
'''接受两个参数
1.显示图像的窗口的名称
2.要显示的图像'''
imshow("CV",image)

#matplotlib显示图像
#opencv读取的图像默认以BGR读取数组为n*m*3,n为图像的行，m为图像的列，3为BGR值
'''plt.imshow()接受多个参数
1.图像的数据
2.其它参数可选'''
plt.imshow(image[:,:,::-1])#读取整个图像，并将BGR转为RGB，-1表示步长即反转
#plt.show()

#保存图像imwrite()函数
'''接受两个参数
1.保存的文件名
2.要保存的图像'''
#imwrite("test.png",image)

waitKey()

#显示灰度图
greyImage=imread("D:\\Dataset\\BMP\\1.bmp",0)
#cv显示
imshow("Grey",greyImage)
#matploylib显示
plt.imshow(greyImage,cmap=plt.cm.gray)
plt.show()

#imwrite("test.png",greyImage)

waitKey()