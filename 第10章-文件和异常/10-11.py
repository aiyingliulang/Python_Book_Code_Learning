# coding=utf-8
import json

filename = 'love_number.json'
love_number = input("What's your favorite number? ")

with open(filename,'w') as f:
    json.dump(love_number,f)
    print("We have remembered your favorite number!")