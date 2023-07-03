# coding=utf-8
import random

num = []
for i in range(10):
    num.append(i)
num.extend(['b','m','o','a','q'])
award = []
#让我们康康中奖的号码
while len(award) < 4:
    pulled_item = random.choice(num)
    if pulled_item not in award:
        print(f"We pulled a {pulled_item}!")
        award.append(pulled_item)

print('\nThe finall award_number are:',award)