# coding=utf-8
filename = 'learning_python.txt'

'''读取整个文件'''
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

'''遍历文件对象'''
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

'''存储列表中'''
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())