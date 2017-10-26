#--coding:utf-8--

"""
9-6:冰激凌小店
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


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super(IceCreamStand,self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple','banana','strawberry','orange']

    def describe_flavors(self):
        print ('The icecream has flavors:' + str(self.flavors))

iceQueen = IceCreamStand('IceQueen', 'icecream')
iceQueen.describe_flavors()

"""
9-7-8:管理员权限
"""
class User(object):
    def __init__(self,first_name,last_name):
        self.FN = first_name
        self.LN= last_name

    def describe(self):
        print ('The username is: ' + str(self.FN) + str(self.LN))

class Privileges(object):
    def __init__(self,privileges = ['can add post','can delete post','can ban user']):
        self.uprivileges = privileges


    def show_privileges(self):
        print ('The privileges include:' + str(self.uprivileges) + '.')

class Admin(User):
    def __init__(self,first_name,last_name):
        super(Admin, self).__init__(first_name,last_name)
        self.admin_privileges = Privileges()  #实例用作属性

admin = Admin('Wu','Huliang')
admin.describe()
admin.admin_privileges.show_privileges()

"""
9-9:电瓶升级
"""
class Car(object):
    def __init__(self,make,model,year):
        self.umake = make
        self.umodel = model
        self.uyear = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.uyear) + ' ' + self.umake + ' ' + self.umodel
        return long_name.title()

    def read_odometer(self):
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

class Battery(object):
    """模拟电动汽车电瓶"""
    def __init__(self,battery_size = 70):
        self.ubattery_size = battery_size

    def describe_battery(self):
        print ("This car has a " + str(self.ubattery_size) + "-KWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.ubattery_size == 70:
            range = 240
        elif self.ubattery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print message

    def upgrade_battery(self):
        if self.ubattery_size != 85:
            self.ubattery_size = 85
        else:
            print ('The battery has upgraded!')

class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self,make,model,year):
        """
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super(ElectricCar,self).__init__(make,model,year)
        self.battery_size = Battery()    #将实例用作属性！

    def increment_odometer(self,miles):
        """重写父类方法"""
        print "The electricCar doesn't need increment miles."

my_tesla = ElectricCar('tesla','model S','2016')
print (my_tesla.get_descriptive_name())

my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()
my_tesla.battery_size.upgrade_battery()
my_tesla.battery_size.get_range()