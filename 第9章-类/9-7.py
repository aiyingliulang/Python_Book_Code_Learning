# coding=utf-8
class User():
    '''记录用户信息并问候用户'''
    def __init__(self,first_name,last_name,age):
        '''初始化属性'''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age

    def describe_user(self):
        '''描述用户'''
        print(f"\nThe name is {self.first_name} {self.last_name}.")
        print(f"The age is {str(self.age)} years old.")

    def greet(self):
        '''问候用户'''
        print(f"Hello {self.first_name} {self.last_name}！")


class Admin(User):
    '''管理员的独特之处'''

    def __init__(self,first_name,last_name,age):
        '''初始化父类属性'''
        super().__init__(first_name,last_name,age)
        self.privileges = []

    def show_privileges(self):
        '''显示管理员特权'''
        print('You have these privileges:')
        for privilege in self.privileges:
            print('\t'+privilege)


#调用看看
laozhu = Admin('zhu','yiji',45)
laozhu.describe_user()
laozhu.greet()
laozhu.privileges = ['can add post','can delete post','can ban user']
laozhu.show_privileges()

