# coding=utf-8
class Car:
    '''模拟汽车的尝试。'''

    def __init__(self,make,model,year):
        '''初始化汽车属性。'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''返回整洁的信息。'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        '''输出里程数。'''
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        '''
        直接将里程设置为指定的数值。
        禁止参数回调。
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        '''里程增加指定值。'''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

class Battery:
    '''一次模拟电动汽车电瓶的简单尝试。'''

    def __init__(self,battery_size=75):
        '''初始化电瓶属性。'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''输出电动汽车电池大小。'''
        print(f"The car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        '''打印一条消息，指出电动汽车的续航距离。'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"The car can run about {range} miles on a full charge.")

    def upgrade_battery(self):
        '''检查电池容量'''
        if self.battery_size != 100:
            self.battery_size = 100


class Electriccar(Car):
    '''电动车的独特之处。'''

    def __init__(self,make,model,year):
        '''
        初始化父类属性，
        再初始化电动汽车的特有属性。
        '''
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        '''电动汽车没有油箱。'''
        print("This car doesn't need a gas tank!")

#调用
my_tesla = Electriccar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('\n电池升级中···')
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
