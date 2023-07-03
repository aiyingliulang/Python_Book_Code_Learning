#coding=utf-8
fr1 = {'first_name':'zhang',
      'last_name':'yucheng',
      'age':22,
      'city':'wuhan'}
fr2 = {'first_name':'wu',
      'last_name':'shilong',
      'age':22,
      'city':'beijin'}
fr3 = {'first_name':'lu',
      'last_name':'xiaojun',
      'age':22,
      'city':'weihai'}
people=[fr1,fr2,fr3]
for i in people:
    full_name=i['first_name']+' '+i['last_name']
    print('My name is '+full_name.title()+'.'+
          'I am '+str(i['age'])+' years old.'+
          'I live in '+i['city'].title()+'.')