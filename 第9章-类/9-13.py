# coding=utf-8
import random
class Die:
    '''创建骰子'''

    def __init__(self,sides):
        '''骰子的属性'''
        self.sides = sides

    def roll_die(self):
        '''定义一个掷骰子的方法'''
        num = random.randint(1,self.sides)
        print('\t'+str(num))


#骰子函数
def hanshu(dian_shu):
    j = 0
    for i in range(1,11):
        tou_zi = Die(dian_shu)
        j += 1
        print('第'+str(j)+'掷出的数为： ')
        tou_zi.roll_die()
    print('\n共掷骰子'+str(j)+'次。')

#掷骰子实战
print('\n这是一个6面的骰子:')
touzi1 = Die(6)
hanshu(6)

print('\n这是一个10面的骰子')
touzi1 = Die(10)
hanshu(10)

print('\n这是一个20面的骰子:')
touzi1 = Die(20)
hanshu(20)