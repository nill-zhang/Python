#!/usr/bin/python
# by sfzhang 2016.11.26
from collections import namedtuple
import os


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

# Now, imagine your requirements change again. You also want to track the weight of each
# score toward the overall grade in the class so midterms and finals are more important than
# pop quizzes


class WeightedGradeBookbySubjects(object):
    """ a class use dict and dict to store student grades info from
        different subjects.
        {name1:{subject1:[(grade1,weight1),(grade2,weight2),...], subject2:[,,,,,]},
         name2:{subject1:[(grade1,weight1),(grade2,weight2),...], subject2:[,,,,,],
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
        total, count = 0, len(self.students[name])
        # I use .items() instead of .values(), because I want to get each subject_name and
        # print subject_average
        for subject_name, subject_grades in self.students[name].items():
            subject_total, subject_weight_total = 0, 0
            for weighted_grade in subject_grades:
                subject_total += weighted_grade.score * weighted_grade.weight
                subject_weight_total += weighted_grade.weight
            subject_average = subject_total/subject_weight_total
            print(("%s average: %f " % (subject_name, subject_average)).center(term_size))
            total += subject_average
        return total/count

# the previous class is too complicated, it use nested dict
# and list of namedtuples, the average_grade function is has too
# loops, I am now disassemble it into 3 simpler classes
# a class with student info
# a class with student's subject info
# a class with subject info


class Subject(object):
    """ Subject class has grades about subjects"""
    def __init__(self):
        self.grades = []

    def report_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        """ average grade for a subject"""
        grade_total, weight_total = 0, 0
        for score, weight in self.grades:
            grade_total += score * weight
            weight_total += weight
        average = grade_total/weight_total
        return average


class Student(object):
    """ Student class has subjects about students"""
    def __init__(self):
        self.subjects = {}

    def add_subject(self, name):
        self.subjects[name] = Subject()
        return self.subjects[name]

    def average_grade(self):
        """ overall average grade for a student based on all subjects"""
        total, subject_count = 0, len(self.subjects)
        for j in self.subjects.values():
            total += j.average_grade()
        return total/subject_count


class Program(object):
    """Grade class has students in one program"""
    def __init__(self):
        self.students = []

    def add_student(self, name):
        if name not in self.students:
            self.students.append(name)
        return Student()


if __name__ == "__main__":
    term_size = 120  # os.get_terminal_size().columns
    print("-" * term_size)
    math_grade_book = GradeBook()
    math_grade_book.add_student("shaofeng zhang")
    math_grade_book.report_grade("shaofeng zhang", 90)
    math_grade_book.report_grade("shaofeng zhang", 87)
    print(("math average: %f" % math_grade_book.average_grade("shaofeng zhang")).center(term_size))

    print("-" * term_size)
    subjects_grade_book = GradeBookbySubjects()
    subjects_grade_book.add_student("shaofeng zhang")
    subjects_grade_book.report_grade("shaofeng zhang", "Math", 78)
    subjects_grade_book.report_grade("shaofeng zhang", "English", 86)
    subjects_grade_book.report_grade("shaofeng zhang", "Math", 82)
    subjects_grade_book.report_grade("shaofeng zhang", "English", 83)
    subjects_grade_book.report_grade("shaofeng zhang", "C ++", 94)
    print(("all average: %f" % subjects_grade_book.average_grade("shaofeng zhang")).center(term_size))

    print("-" * term_size)
    subjects_weighted_book = WeightedGradeBookbySubjects()
    my_grade = namedtuple("my_grade", "score, weight")
    subjects_weighted_book.add_student("shaofeng zhang")
    subjects_weighted_book.report_grade("shaofeng zhang", "Math", my_grade(85, 0.2))
    subjects_weighted_book.report_grade("shaofeng zhang", "Math", my_grade(90, 0.3))
    subjects_weighted_book.report_grade("shaofeng zhang", "Math", my_grade(87, 0.4))
    subjects_weighted_book.report_grade("shaofeng zhang", "English", my_grade(30, 3))
    subjects_weighted_book.report_grade("shaofeng zhang", "English", my_grade(50, 9))
    subjects_weighted_book.report_grade("shaofeng zhang", "English", my_grade(45, 2))
    subjects_weighted_book.report_grade("shaofeng zhang", "C ++", my_grade(58, 2))
    print(("all weighted average: %f" %
          subjects_weighted_book.average_grade("shaofeng zhang")).center(term_size))
    print("-" * term_size)

    grade = Program()
    sfzhang = grade.add_student("shaofeng zhang")
    math = sfzhang.add_subject("math")
    english = sfzhang.add_subject("english")
    history = sfzhang.add_subject("history")
    math.report_grade((56, 4))
    math.report_grade((75, 4))
    math.report_grade((86, 4))
    math.report_grade((97, 4))

    english.report_grade((85, 0.3))
    english.report_grade((77, 0.2))
    english.report_grade((80, 0.4))
    english.report_grade((94, 0.1))

    history.report_grade((88, 8))
    history.report_grade((79, 6))
    history.report_grade((81, 7))
    history.report_grade((91, 4))
    print(("math: %f" % math.average_grade()).center(term_size))
    print(("english: %f" % english.average_grade()).center(term_size))
    print(("history: %f" % history.average_grade()).center(term_size))
    print(("overall: %f" % sfzhang.average_grade()).center(term_size))


