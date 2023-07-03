# coding=utf-8
'''Do a research to know why people love program.'''

filename = 'reasons.txt'
responses = []

while True:
    response = input('\nWhy do you love program? ')
    responses.append(response)

    continue_roll = input('Would you like to let someone else respond? (y/n)')
    if continue_roll != 'y':
        break

with open(filename,'a') as file_object:
    for response in responses:
        file_object.write(f"{response}\n")
