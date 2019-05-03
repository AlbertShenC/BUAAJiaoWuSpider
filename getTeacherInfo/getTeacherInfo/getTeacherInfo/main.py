# Author    :Albert Shen
# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
import sys
import os

if __name__ == '__main__':
    with open('teacher.csv', 'w', encoding='utf-8') as f:
        f.write('姓名,学校,学院,职位,性别,个人主页,个人照片\n')
        f.close()

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(["scrapy", "crawl", "getInfo"])
