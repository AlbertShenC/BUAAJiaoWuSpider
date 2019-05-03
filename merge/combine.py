# Author    :Albert Shen
# -*- coding: utf-8 -*-

import os


if __name__ == "__main__":
    path = "D:\GitHubFile\GetCourseFromJiaoWu\merge\origin" #文件夹目录
    files = os.listdir(path) #得到文件夹下的所有文件名称
    line_number = 0
    print(files)
    for file in files: #遍历文件夹
         if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
             with open(path+"/"+file, "r", encoding="utf-8") as f:
                 str = f.readline()
                 while str != "":
                     print(str)
                     line_number = line_number + 1
                     str = f.readline()
                 f.close()
    print(line_number)