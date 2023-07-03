# coding=utf-8

print("告诉我两个数字，我给出它们的和。")
print("随时输入字母'q'退出。")

while True:
    try:
        first_number = input('请输入第一个数字：')
        if first_number == 'q':
            break
        first_number = int(first_number)

        second_number = input('请输入第二个数字: ')
        if second_number == 'q':
            break
        second_number = int(second_number)
    except ValueError:
        print('请输入数字或者字母q!')

    else:
        answer = int(first_number) + int(second_number)
        print(f"{first_number} + {second_number} = {answer}")