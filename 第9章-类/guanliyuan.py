'''一组描述管理员信息及其权限的类'''

from user import User

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