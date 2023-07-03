#coding=utf-8
cities={'beijin':{'country':'china','population':'2500w','fact':'中国加油'},
        'london':{'country':'U.k','population':'3000w','fact':'好父亲'},
        'tokyo':{'country':'Japan','population':'4000w','fact':'小日本'}}
for city,xi_jie in cities.items():
        country=xi_jie['country'].title()
        population=xi_jie['population']
        fact=xi_jie['fact']
        print('\n'+city.title()+' is in '+country.title()+'.')
        print('The population of it is '+population+'.')
        print('In a word,'+fact+'!')