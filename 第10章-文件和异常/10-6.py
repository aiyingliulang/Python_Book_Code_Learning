# coding=utf-8

print("告诉我两个数字，我给出它们的和。")

try:
    first_number = input('请输入第一个数字：')
    first_number = int(first_number)

    second_number = input('请输入第二个数字: ')
    second_number = int(second_number)

except ValueError:
    print('请输入数字或者字母q!')

else:
    answer = int(first_number) + int(second_number)
    print(f"{first_number} + {second_number} = {answer}")
