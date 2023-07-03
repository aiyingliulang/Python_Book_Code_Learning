# coding=utf-8

filename = 'guest.txt'
with open(filename,'w') as file_object:
    file_object.write(input('请输入姓名： '))
