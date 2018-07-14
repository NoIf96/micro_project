# -*- coding:utf-8 -*-
import os
import shutil


def autoClassification(path):
    files = os.listdir(path)
    for f in files:
        folder_name = os.path.join(path, f.split('.')[-1])
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        shutil.move(os.path.join(path, f), folder_name)

if __name__ == '__main__':
    path = input("请输入目录路径: ")
    print("开始归类文件")
    autoClassification(path)
    print("归类结束")


