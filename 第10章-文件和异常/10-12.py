# coding=utf-8
import json
# 如果已经存在最喜欢的数就加载它。
# 否则，提示用户输入。

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        love_number = json.load(f)
    print(f"I know your favorite number!It's {love_number}.")
except FileNotFoundError:
    love_number = input("What's your favorite number? ")
    with open(filename,'w') as f:
        json.dump(love_number,f)
    print("We have remembered your favorite number!")