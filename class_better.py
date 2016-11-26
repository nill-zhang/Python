#!/usr/bin/python
# by sfzhang 2016.11.26
from collections import namedtuple


class GradeBook(object):
    """ a simple class use dict and list to store student grades info
        for the Math Course
        {name1:[,,,,,], name2:[,,,,,]...}
    """
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = []

    def report_grade(self, name, grade):
        # you can also define self.students as a defaultdict(list)
        if name not in self.students:
            self.add_student(self, name)
        self.students[name].append(grade)

    def average_grade(self, name):
        if name not in self.students:
            print("Please provide a valid student name")
            exit(1)
        grades = self.students[name]
        return sum(grades)/len(grades)


# now things has gotten a little complicated
# What if a grade book for students on different subjects

class GradeBookbySubjects(object):
    """ a class use dict and dict to store student grades info from
        different subjects.
        {name1:{subject1:[,,,,,,], subject2:[,,,,,]},
         name2:{subject1:[,,,,,,], subject2:[,,,,,],
         ...}
    """
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = {}

    def report_grade(self, name, subject, grade):

        if name not in self.students:
            self.add_student(self, name)
        student = self.students[name]
        student.setdefault(subject, []).append(grade)

    def average_grade(self, name):
        total, count = 0, 0
        for grades in self.students[name].values():
            total += sum(grades)
            count += len(grades)
        return total/count


if __name__ == "__main__":
    math_grade_book = GradeBook()
    math_grade_book.add_student("shaofeng zhang")
    math_grade_book.report_grade("shaofeng zhang", 90)
    math_grade_book.report_grade("shaofeng zhang", 87)
    print(math_grade_book.average_grade("shaofeng zhang"))

    subjects_grade_book = GradeBookbySubjects()
    subjects_grade_book.add_student("shaofeng zhang")
    subjects_grade_book.report_grade("shaofeng zhang", "Math", 78)
    subjects_grade_book.report_grade("shaofeng zhang", "English", 86)
    subjects_grade_book.report_grade("shaofeng zhang", "Math", 82)
    subjects_grade_book.report_grade("shaofeng zhang", "English", 83)
    subjects_grade_book.report_grade("shaofeng zhang", "C ++", 94)
    print(subjects_grade_book.average_grade("shaofeng zhang"))

