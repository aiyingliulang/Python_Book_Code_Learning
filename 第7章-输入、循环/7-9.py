# coding=utf-8
sandwich_orders=['tuna','pastrami','apple','pastrami','milk','pastrami']
print(sandwich_orders)
print('本店的pastrami已经卖完了。')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
