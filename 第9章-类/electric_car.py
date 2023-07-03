'''一个电动车的类'''

from car import Car

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

class ElectricCar(Car):
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
