#coding=utf-8
responses = {}
#设置标志
poll_accitive = True
while poll_accitive:
    name = input('\n你的名字： ')
    response = input('你喜欢哪座城市呢？ ')
    responses[name] = response
    repeat = input('还有人想回答吗？（是/否） ')
    if repeat == '否':
        poll_accitive = False
print('\n所有结果如下：')
for people,city in responses.items():
    print(people+'喜欢的城市是'+city+'。')

