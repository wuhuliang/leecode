#--coding:utf-8--

class Dog(object):
    """模拟小狗"""

    def __init__(self,name,age):  #初始化属性
        self.dogname = name  #以self为前缀的变量可供类中所有方法使用
        self.dogage = age
        """
        1、获取存储在形参中name的值
        2、把该值存储到变量dogname中
        3、变量被关联到当前创建的实例
        """

    def sit(self):  #模拟小狗坐下
        print (self.dogname + " is now sitting.")

    def roll_over(self):  #模拟小狗翻滚
        print (self.dogname + " is now rolled over!")

my_dog = Dog('xiaohei',6)

my_dog.sit()
my_dog.roll_over()







