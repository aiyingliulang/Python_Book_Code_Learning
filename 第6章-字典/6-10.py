#coding=utf-8
num = {'a':[2,4],
       'b':[5,7,9],
       'c':[4,6],
       'd':[9,6,3]}
for people,numbers in num.items():
       print('\n'+people+'喜欢的数字有：')
       for number in numbers:
              print('\t'+str(number))

