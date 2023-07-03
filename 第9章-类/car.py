'''一个表示汽车的类'''

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