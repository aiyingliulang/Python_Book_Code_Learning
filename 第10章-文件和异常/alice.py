# coding=utf-8

filename = 'alice.txt'

try:
    with open(filename,encoding='utf-8') as f:
        contexts = f.read()
except FileNotFoundError:
    print(f'Sorry,the file {filename} does not exist.')
else:
    #统计小说大致有多少单词
    words = contexts.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
