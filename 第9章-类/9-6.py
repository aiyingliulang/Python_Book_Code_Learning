# coding=utf-8
class Restaurant():
    '''餐馆的描述与是否营业'''

    def __init__(self,restaurant_name,cuisine_type):
        '''初始化餐厅名和菜名'''
        self.name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''描述餐厅'''
        print(f"The name of the restaurant is {self.name}.")
        print(f"The food in it is {self.cuisine_type}.")

    def open_restaurant(self):
        '''餐厅营业'''
        print('The restaurant is opening.')

class IceCreamStand(Restaurant):
    '''冰淇淋店的特殊之处。'''

    def __init__(self,restaurant_name,cuisine_type='ice_cream'):
        '''先初始化父类属性，再初始化冰淇淋店的专属属性。'''
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def tastes(self):
        '''展示冰淇淋口味。'''
        print('\nWe have the following ice cream flavors.')
        for flavor in self.flavors:
            print(f"-{flavor.title()}")

#调用
my_ice_cream_store = IceCreamStand('xiaolu')
my_ice_cream_store.flavors = ['巧克力','抹茶','奶油']

my_ice_cream_store.describe_restaurant()
my_ice_cream_store.open_restaurant()
my_ice_cream_store.tastes()

