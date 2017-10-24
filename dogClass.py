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

"""
餐馆练习
"""
class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.Rname = restaurant_name
        self.Rtype = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print ('The restaurantName is %s,it is good at %s.' % (self.Rname, self.Rtype))

    def open_restaurant(self):
        print 'The Restaurant in bussiness!'

    def count_number_served(self):
        print 'A totle of ' + str(self.number_served) + ' people for dinner.'

    def set_number_served(self, number):
        self.number_served = number

    def increament_number_served(self, incNumber):
        self.number_served += incNumber


restaurant = Restaurant('SevenEleven', 'FastFood')
restaurant.describe_restaurant()

restaurant.set_number_served(10)
restaurant.increament_number_served(50)
restaurant.count_number_served()

"""
汽车类
"""
class Car(object):
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.umake = make
        self.umodel = model
        self.uyear = year
        self.odometer_reading = 0   #给属性指定默认值，就不需要在括号里面提供形参

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.uyear) + ' ' + self.umake + ' ' + self.umodel
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        print ("This car has " + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止里程表读数往回调整
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print "You can't roll back an odometer!"

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_new_car = Car('subaru','outback',2013)
print (my_new_car.get_descriptive_name())

my_new_car.update_odometer(2000)
my_new_car.read_odometer()

my_new_car.increment_odometer(1500)
my_new_car.read_odometer()