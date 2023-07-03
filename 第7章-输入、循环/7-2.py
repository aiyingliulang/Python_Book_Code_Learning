#coding=utf-8
num=int(input('请问几人用餐？ '))
if num <=0:
    if num < 0:
        print('闹鬼！')
    else:
        print('不吃就走人！')
elif num > 8:
    print('没位置啦！')
else:
    print('老板们请坐！')
