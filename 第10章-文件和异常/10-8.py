# coding=utf-8

def pr_ob(filename):
    """读取文件并打印文件内容"""
    try:
        with open(filename,encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file {filename} doesn't exist.")
    else:
        print(contents)

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    pr_ob(filename)