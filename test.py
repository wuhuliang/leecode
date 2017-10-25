#--coding:utf-8--

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

class battery(object):
    """模拟电动汽车电瓶"""
    def __init__(self,battery_size = 70):
        self.ubattery_size = battery_size

    def describe_battery(self):
        print ("This car has a " + str(self.ubattery_size) + "-KWh battery.")

class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self,make,model,year):
        """
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super(ElectricCar,self).__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        print ("This car has a " + str(self.battery_size) + "-KWh battery.")

    def increment_odometer(self,miles):
        """重写父类方法"""
        print "The electricCar doesn't need increment miles."



my_tesla = ElectricCar('tesla','model S','2016')
print (my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.increment_odometer(1000)
my_tesla.read_odometer()