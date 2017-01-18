#!/usr/bin/python
# by sfzhang 2017.1.17
from matplotlib import pyplot as ppt
import random
x_data = [random.randint(0, 10) for i in range(10)]
y_data = [random.randint(0, 10) for i in range(10)]
ppt.plot(x_data, y_data)
ppt.show()