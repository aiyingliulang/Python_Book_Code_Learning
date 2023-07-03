# coding=utf-8
class User():
    '''记录用户信息并问候用户'''
    def __init__(self,first_name,last_name,age):
        '''初始化属性'''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        '''描述用户'''
        print(f"\nThe name is {self.first_name} {self.last_name}.")
        print(f"The age is {str(self.age)} years old.")

    def greet(self):
        '''问候用户'''
        print(f"Hello {self.first_name} {self.last_name}！")

    def increment_login_attempts(self):
        '''将登陆尝试加一'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''重置登陆尝试为0'''
        self.login_attempts = 0

#调用
wo = User('zhang','yucheng',22)
wo.describe_user()
wo.greet()
print('\n做三次登陆尝试···')
wo.increment_login_attempts()
wo.increment_login_attempts()
wo.increment_login_attempts()
print(f'The number of login_attempts is {wo.login_attempts}.')
print('\n重置次数···')
wo.reset_login_attempts()
print(f'It has been restored.The rest times of login_attempts is {wo.login_attempts}.')