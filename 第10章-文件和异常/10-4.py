# coding=utf-8

filename = 'guest_book.txt'

print('Enter quit to stop this program.')
while True:
    name = input("What's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()}\n")
            print('Hello '+name.title()+'!Your name has added to the guest book.')