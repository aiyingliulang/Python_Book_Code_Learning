'''管理员特权的类'''

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

        #初始化权限
        self.privileges = Privileges()


class Privileges():
    '''管理员权限'''

    def __init__(self,privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        '''显示管理员特权'''
        print('\nPrivileges:')
        if self.privileges:
            for privilege in self.privileges:
                print(f'-{privilege}')
        else:
            print("You don't have any privileges.")