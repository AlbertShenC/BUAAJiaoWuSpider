# Author    :Albert Shen
# -*- coding: utf-8 -*-
import re
import requests
from lxml import etree

class Course:
    def __init__(self, number, course_number, course_name,
                 department, property, classification, credit, hours, teacher_name):
        self.number = number
        self.course_number = course_number
        self.course_name = course_name
        self.department = department
        self.property = property
        self.classification = classification
        self.credit = credit
        self.hours = hours
        self.teacher_name = teacher_name


def to_json(array):
    with open("result.json", "w", encoding="utf-8") as f:
        f.write('[\n')
        for i in range(0, len(array)):
            f.write('{')
            f.write('"序号":' + str(array[i].number))
            f.write(',"课程代码":"' + array[i].course_number + '"')
            f.write(',"课程名称":"' + array[i].course_name + '"')
            f.write(',"开课院系":"' + array[i].department + '"')
            f.write(',"课程性质":"' + array[i].property + '"')
            f.write(',"课程类别":"' + array[i].classification + '"')
            f.write(',"学分":"' + array[i].credit + '"')
            f.write(',"总学时":' + str(array[i].hours))
            f.write(',"教师姓名":"' + array[i].teacher_name + '"')
            if i != len(array) - 1:
                f.write('},\n')
            else:
                f.write('}\n')
        f.write(']')
        f.close()


if __name__ == "__main__":
    course_array = []
    course_csv = ""
    with open("result.csv", "r", encoding="utf-8") as f:
        course_csv = f.readline()
        course_csv = f.readline()
        while course_csv != "":
            course_csv_array = course_csv.replace('\n', '').split(",")
            print(course_csv_array)
            course_array.append(Course(0, course_csv_array[0], course_csv_array[1],
                                       course_csv_array[2], course_csv_array[3],
                                       course_csv_array[4], course_csv_array[5],
                                       float(course_csv_array[6]), course_csv_array[7],
                                       ))
            course_csv = f.readline()
        f.close()
    print("end")
    to_json(course_array)
    # tree = etree.parse("D:/GitHubFile/getCourse/courseSpider/courseSpider/test.html", etree.HTMLParser())
    # result = etree.tostring(tree, encoding = "utf-8", pretty_print = True, method = "html")
    # print(result.decode('utf-8'))