
class Setting:
    '''游戏参数的设定'''

    def __init__(self):
        #窗口大小
        self.WIDTH=800
        self.HIGH=600

        #颜色的设定
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BACKGROUND=(230,230,230)

        #蛇的初始长度
        self.LONG=80
        #蛇的移动速度
        self.SPEED =10

        #食物大小
        self.SIZE=10

        #更新屏幕的是速度
        self.FPS=30
