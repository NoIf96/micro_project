# -*- coding:utf-8 -*-
import os


def search(path, name):
    files = os.listdir(path)
    return [f for f in files if name in f]

if __name__ == '__main__':
    path = input("请输入目录路径: ")
    name = input("请输入文件名: ")
    files = search(path, name)
    print(files)

