# coding=utf-8
import json

def get_stored_username():
    '''如果存储了用户名，就获取它。'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''提示用户输入用户名。'''
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user1():
    '''问候用户，并指出其名字'''
    username = get_stored_username()
    if username:
        response = input(f"Are you {username}?(y/n) ")
        if response == 'y':
            print(f"Welcome back,{username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back,{username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back,{username}!")

def greet_user2():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    # Let's prompt for a new username.
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")

# 该return语句表示函数中的代码在打印欢迎返回消息后停止运行。
# 当用户名不存在或用户名不正确时，return永远不会到达该语句。
# 函数的第二部分只会在if语句失败时运行，所以我们不需要else块。
# 现在，当任一if语句失败时，该函数会提示输入新用户名。
# 唯一需要解决的是嵌套if语句。
# 这可以通过将检查用户名是否正确的代码移动到单独的函数来清除。
# 如果你喜欢这个练习，你可以尝试创建一个新的函数check_username()，看看你是否可以if从greet_user().

greet_user2()