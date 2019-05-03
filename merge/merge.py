# Author    :Albert Shen
# -*- coding: utf-8 -*-

class Course:
    def __init__(self, number, course_number, course_name,
                 department, property, classification, credit, hours):
        self.number = number
        self.course_number = course_number
        self.course_name = course_name
        self.department = department
        self.property = property
        self.classification = classification
        self.credit = credit
        self.hours = hours
        self.teacher_array = []

    def add_teacher(self, teacher):
        if teacher == "Null":
            return

        for i in self.teacher_array:
            if i == teacher:
                return
        self.teacher_array.append(teacher)

    def __str__(self):
        result_str = self.course_number + "," + self.course_name + "," + self.department + "," + self.property + "," + self.classification + "," + self.credit + "," + str(self.hours)

        if len(self.teacher_array) == 0:
            result_str = result_str + ",N/A"
        elif len(self.teacher_array) >= 1:
            result_str = result_str + "," + self.teacher_array[0]

        for i in range(1, len(self.teacher_array)):
            result_str = result_str + "+" + self.teacher_array[i]

        return result_str


def exist(course_array_para, course_id):
    for i in range(0, len(course_array_para)):
        if course_array_para[i].course_number == course_id:
            return i
    return -1


if __name__ == "__main__":
    course_array = []
    not_exist_course = 0
    with open("course.csv", "r", encoding="utf-8") as f:
        f.readline()
        course_csv = f.readline()
        while course_csv != "":
            course_csv_array = course_csv.replace('\n', '').split(",")
            if exist(course_array, course_csv_array[1]) == -1:
                course_array.append(Course(int(course_csv_array[0]), course_csv_array[1],
                                          course_csv_array[2], course_csv_array[3],
                                          course_csv_array[4], course_csv_array[5],
                                          course_csv_array[6], float(course_csv_array[7])))
            course_csv = f.readline()
        f.close()

    with open("teacher.csv", "r", encoding="utf-8") as f:
        teacher_csv = f.readline()
        while teacher_csv != "":
            teacher_csv_array = teacher_csv.replace('\n', '').replace('+', ',').split(",")
            position = exist(course_array, teacher_csv_array[0])
            if position == -1:
                not_exist_course = not_exist_course + 1
                # print(teacher_csv_array[0])
                course_array.append(Course(-1, teacher_csv_array[0], teacher_csv_array[1],
                                           teacher_csv_array[2], teacher_csv_array[3],
                                           teacher_csv_array[4], teacher_csv_array[5],
                                           -1.0))
                for j in range(6, len(teacher_csv_array)):
                    course_array[len(course_array) - 1].add_teacher(teacher_csv_array[j])
            else:
                for j in range(6, len(teacher_csv_array)):
                    course_array[position].add_teacher(teacher_csv_array[j])

            teacher_csv = f.readline()
        f.close()


    # for i in course_array:
    #     print(i)
    # print("Not exist course number = " + str(not_exist_course))
    # course_exist_teacher = 0
    # for i in course_array:
    #     if len(i.teacher_array) == 0:
    #         course_exist_teacher = course_exist_teacher + 1
    # print("Course exist teacher number = " + str(course_exist_teacher))
    # print(len(course_array))

    with open("result.csv", "w", encoding="utf-8") as f:
        for i in course_array:
            print(i)
            f.write(i.__str__() + "\n")
    print(len(course_array))
