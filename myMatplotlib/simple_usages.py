#!/usr/bin/python
# by sfzhang 2017.1.17
from matplotlib import pyplot as ppt
from matplotlib import style
import random


def show_plot():
    x_data = [i for i in range(10)]
    y_data = random.sample(range(0, 10), 10)
    ppt.plot(x_data, y_data, label="first sample", linewidth=2, color="y")
    ppt.legend(loc="upper right")
    style.use(random.sample(ppt.style.available(), 1))
    ppt.show()


def show_pie():
    labels = ["Asia", "America", "South America", "Africa", "Arctic", "Antarctic"]
    xdata = random.sample(range(100), len(labels))
    ppt.pie(xdata, labels=labels, shadow=True, autopct="%1.1f%%")
    ppt.show()


def show_scatter():
    pass


def show_dynamic_plot():
    pass


def show_histogram():
    pass


def show_3dimension():
    pass


if __name__ == "__main__":
    show_pie()

