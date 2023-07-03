# coding=utf-8

print("Give me two numbers,and I'll divide them.")
print('Enter q to over the game.')

while True:
    first_number = input('The first number: ')
    if first_number == 'q':
        break
    second_number = input('The second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero！")
    else:
        print("The answer is ",str(answer),'.')