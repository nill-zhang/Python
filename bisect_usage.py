import bisect
import collections


def grade(score, levels, grades):
    assert len(levels) == len(grades), "levels and grades not matched"
    # get the index where score should be inserted in levels
    # levels is a sorted sequence
    index = bisect.bisect(levels, score)
    # map the level in grades
    return grades[index]


def grade_test():
    marks = {"sfzhang": 89, "xlyang": 22, "lyzhang": 13, "qshu": 48, "jchu": 71, "alex": 49}
    levels = range(10, 101, 30)
    grades = "DCBA"
    # build a tuple of (key, value) pair
    sorted_marks = ((key, marks[key]) for key in sorted(marks.keys()))
    # collections.OrderedDict will keep the insertion order of the
    # dict's (key,value) pair, because we already sorted the tuple
    # so when the those pairs are add to the OrderedDict, they will
    # be added in order
    ordered_marks = collections.OrderedDict(sorted_marks)

    sorted_marks = sorted(marks.items())
    ordered_marks = collections.OrderedDict(sorted_marks)

    for name, mark in ordered_marks.items():
        print("{:8s}--> {:3s}".format(name, grade(mark, levels, grades)))


if __name__ == "__main__":
    grade_test()