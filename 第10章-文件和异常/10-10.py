# coding=utf-8

def count_target(filename,target):
    """计算一个文件大致包含多少个目标词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'Sorry,the file {filename} does not exist.')
    else:
        # 统计小说大致有多少个目标单词
        num_words = contents.lower().count(target)
        print(f"The file {filename} has about {num_words} '{target}'.")

name = 'alice.txt'
count_target(name,'the')


