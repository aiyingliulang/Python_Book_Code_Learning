#coding=utf-8
fr = ['张三','李四','王五']
for i in fr:
    print(i+',来吃饭。')

absent = fr.pop()
print(absent +'来不了了。')
fr.append('赵六')
for i in fr:
    print(i + ',来吃饭。')

print('我找到了更大的桌子。')
fr.insert(0,'高七')
fr.insert(3,'张玉城')
fr.append('王八蛋')
for i in fr:
    print(i + ',来吃饭。')

print('只能来两个人了。')
while len(fr) > 2:
    a = fr.pop()
    print(a+'抱歉啦！')
for i in fr:
    print(i+'你还在名单中。')
del fr[:]
print(fr)