from tequan import Admin
laozhu = Admin('zhu','yiji',45)
laozhu.describe_user()
laozhu.greet()
laozhu.privileges.show_privileges()

print('\nAdding privileges...')
laozhu_privileges = ['can add post','can delete post','can ban user']
laozhu.privileges.privileges = laozhu_privileges
laozhu.privileges.show_privileges()