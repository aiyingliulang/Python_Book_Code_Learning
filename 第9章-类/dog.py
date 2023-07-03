# coding=utf-8
class Dog:
    '''小狗的第一次尝试'''

    def __init__(self,name,age):
        '''初始化名字和年龄'''
        self.name = name.title()
        self.age = int(age)

    def sit(self):
        '''小狗下蹲'''
        print(f"{self.name} is sitting now.")

    def roll_over(self):
        '''小狗打滚'''
        print(f"{self.name} rolled over.")

#调用
my_dog = Dog('beibei',3)
your_dog = Dog('lucy',6)

print(f"My dog is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
print('\n这是三个空行\n')
print(f"Your dog is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

