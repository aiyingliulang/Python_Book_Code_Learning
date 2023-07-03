#coding=utf-8
active = True
while active:
    age=int(input('输入quit退出，请输入你的年龄： '))
    if age < 3:
        print('免费')
    elif age > 12:
        print('15刀')
    else:
        print('10刀')
    if age =='quit':
        break
