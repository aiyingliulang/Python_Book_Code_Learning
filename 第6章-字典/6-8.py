#coding=utf-8
pets=[]
pet={'name':'beibei',
    'type':'cat',
    'owner':'lu xiaojun'}
pets.append(pet)

pet={'name':'baishatang',
    'type':'dog',
    'owner':'zhang yucheng'}
pets.append(pet)

for pet in pets:
    print('\nHere are what I know about '+pet['name'].title()+':\n\t'+
          'It is a '+pet['type']+'.\n\tThe owner is '+pet['owner'].title()+'.')

