#coding=utf-8
favorite_places={'张三':['北京','上海'],
                 '李四':['武汉'],
                 '王五':['北京','西安']}
for people,places in favorite_places.items():
    if len(places) == 1:
        print('\n' + people + '喜欢的城市只有：')
        for place in places:
            print('\n\t' + place)
    else:
        print('\n'+people+'喜欢的城市有：')
        for place in places:
            print('\n\t'+place)

