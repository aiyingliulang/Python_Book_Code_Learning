'''一组描述餐厅的类'''

class Restaurant():
    '''餐馆的描述与是否营业'''
    def __init__(self, restaurant_name, cuisine_type):
        '''初始化餐厅门和菜名'''
        self.name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''描述餐厅'''
        print(f"The name of the restaurant is {self.name}.")
        print(f"The food in it is {self.cuisine_type}.")

    def open_restaurant(self):
        '''餐厅营业'''
        print('The restaurant is opening.')