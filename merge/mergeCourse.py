# Author    :Albert Shen
# -*- coding: utf-8 -*-
# 2019.5.3 创建，beta版本，需求变更，只需要将教务爬取下来的课程合并即可
import os

class Course:
    def __init__(self, course_number, course_name,
                 department, property, classification, credit):
        self.course_number = course_number # 课程编号
        self.course_name = course_name # 课程名
        self.department = department # 课程开设院系
        self.property = property # 课程属性——选修/必修
        self.classification = classification # 课程分类——一般通识等
        self.credit = credit # 课程学分
        self.teacher_array = [] # 授课教师列表

    def add_teacher(self, teacher):
        if teacher == "N/A":
            return

        for i in self.teacher_array:
            if i == teacher:
                return
        self.teacher_array.append(teacher)

    def __str__(self):
        result_str = self.course_number + "," + self.course_name + "," + self.department + "," + self.property + "," + self.classification + "," + self.credit

        if len(self.teacher_array) == 0:
            result_str = result_str + ",N/A"
        else:
            result_str = result_str + "," + self.teacher_array[0]

        for i in range(1, len(self.teacher_array)):
            result_str = result_str + "+" + self.teacher_array[i]

        return result_str


def exist(course_array_para, course_id):
    for i in range(0, len(course_array_para)):
        if course_array_para[i].course_number == course_id:
            return i
    return -1


if __name__ == '__main__':
    path = "D:\GitHubFile\GetCourseFromJiaoWu\merge\origin"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    line_number = 0
    print(files)
    origin_courses = [] # 内存形式储存原始课程
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            with open(path + "/" + file, "r", encoding="utf-8") as f:
                str = f.readline()
                while str != "":
                    if str != "\n":
                        origin_courses.append(str)
                        line_number = line_number + 1
                    str = f.readline()
                f.close()

    # for i in origin_courses:
    #     print(i, end='')
    print(line_number)

    # 合并
    course_array = []

    for origin_course in origin_courses:
        origin_course_array = origin_course.replace('\n', '').split(",")
        exist_pos = exist(course_array, origin_course_array[0])
        # print(origin_course_array[0] + ',' + origin_course_array[1] + ',' + origin_course_array[4])
        if exist_pos == -1:
            course_array.append(Course(origin_course_array[0], origin_course_array[1],
                                       origin_course_array[2], origin_course_array[3],
                                       origin_course_array[4], origin_course_array[5]))
            for i in range(6, len(origin_course_array)):
                course_array[len(course_array) - 1].add_teacher(origin_course_array[i])
        else:
            for i in range(6, len(origin_course_array)):
                course_array[exist_pos].add_teacher(origin_course_array[i])

    print(len(course_array))


    with open("course_data.csv", "w", encoding="utf-8") as f:
        for final_course in course_array:
            f.write(final_course.__str__() + '\n')