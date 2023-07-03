#coding=utf-8
sandwich_orders=['tuna','apple','milk']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print('I made you '+sandwich+' sandwich.')
print('\nAll ready!The sandwiches are:')
for i in finished_sandwiches:
    print('\t'+i)
print(sandwich_orders)
print(finished_sandwiches)