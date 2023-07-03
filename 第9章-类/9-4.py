# coding=utf-8
class Restaurant():
    '''餐馆的描述与是否营业'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化餐厅门和菜名'''
        self.name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''描述餐厅'''
        print(f"The name of the restaurant is {self.name}.")
        print(f"The food in it is {self.cuisine_type}.")

    def open_restaurant(self):
        '''餐厅营业'''
        print(f'The restaurant named {self.name} is open.')

    def set_number_served(self,number):
        '''可以设置就餐人数'''
        self.number_served = number

    def increment_number_served(self,increment):
        '''将就餐人数递增'''
        self.number_served += increment

#调用
rt_1 = Restaurant('chunhai','beefnoodles')
rt_1.describe_restaurant()

rt_1.number_served = 60
print(f'The number of passenger is {rt_1.number_served}.')

rt_1.set_number_served(40)
print(f'The number of passenger is {rt_1.number_served}.')

rt_1.increment_number_served(10)
print(f'The number of passenger is {rt_1.number_served}.')