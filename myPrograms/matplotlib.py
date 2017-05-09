#!/usr/bin/python
# by sfzhang 2017.1.17
from matplotlib import pyplot as ppt
from matplotlib import style
import itertools
import random
import numpy as np


def show_plot():
    x_data = [i for i in range(12)]
    y_data = random.sample(range(0, 100), 12)
    ppt.plot(x_data, y_data, label="first sample", linewidth=2, color="y")
    ppt.legend(loc="upper right")
    style.use(random.sample(ppt.style.available, 1))
    ppt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="off")
    ppt.xticks(np.arange(12),
               ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Agst", "Sep", "Oct", "Nov", "Dec"],
               rotation=15)
    ppt.xlabel("x axis", fontdict={"size": 10, "color": "red"})
    ppt.ylabel("y axis")
    # ppt.axis("off")  # axes no show
    ppt.show()


def show_pie():
    continents = ["Asia", "America", "South America", "Africa", "Arctic", "Antarctic"]
    data = random.sample(range(100), len(continents))
    explode = list(itertools.repeat(0, len(continents) - 1))  # construct n-1 0s
    explode.append(random.uniform(0.05, 0.2))  # a random explode scale
    random.shuffle(explode)
    colors = ["#d1b379", "#316799", "#613653", "#c268d8",  "#333382", "lightskyblue"]
    ppt.pie(data,
            labels=continents,
            explode=explode,
            autopct="%1.1f%%",
            colors=colors,
            shadow=True)
    ppt.legend(fancybox=True, loc="upper left")
    ppt.title("World Population Composition")
    ppt.show()


def show_bar():
    weights = [75, 52, 3]
    names = ["sfzhang", "xlyang", "nazhang"]
    ppt.figure(figsize=(6, 1))
    ppt.tick_params()
    ppt.xticks(range(3), names)
    ppt.bar(range(3), height=weights, color=["y", "c", "b"], width=0.6)
    ppt.ylabel("weight/kg")
    ppt.xlabel("name")
    ppt.title("Family Member's weight")
    ppt.show()


def show_scatter():
    xdata = random.sample(range(700), 20)
    ydata = random.sample(range(700), 20)
    ppt.scatter(xdata, ydata, marker="*", edgecolors="y")
    for x, y in zip(xdata, ydata):
        ppt.annotate('(%s, %s)' % (x, y),
                     xy=(x, y),  # where to put annotation
                     xytext=(0, -5),  # where to place text
                     textcoords='offset points',  # indicate the xytext is offset points
                     ha='center',  # horizontal alignment
                     va='top',  # vertical alignment
                     alpha=0.5,   # transparency
                     fontsize=5)
    ppt.text(0, 700, "random text", alpha=0.1, weight="bold", rotation=45)
    ppt.text(80, 200, "random text", alpha=0.1, weight="bold", rotation=190)
    ppt.text(300, 200, "random text", alpha=0.1, weight="bold", rotation=135)
    ppt.text(210, 490, "random text", alpha=0.1, weight="bold", rotation=55)
    ppt.text(550, 600, "random text", alpha=0.1, weight="bold", rotation=15)
    ppt.text(660, 30, "random text", alpha=0.1, weight="bold", rotation=15)
    ppt.grid()
    ppt.title("random scatter figure")
    ppt.axis("off")
    ppt.show()


def show_dynamic_plot():
    pass


def show_histogram():
    pass


def show_3dimension():
    pass


def show_word_cloud(file_directory):
    from wordcloud import WordCloud
    texts = open(file_directory, "r", encoding="utf-8").read()
    word_cloud = WordCloud(background_color="grey", min_font_size=8).generate(texts)
    ppt.figure(figsize=(1024/144, 768/144), dpi=144)
    ppt.imshow(word_cloud)
    ppt.axis("off")
    ppt.show()


if __name__ == "__main__":
    #show_plot()
    #show_pie()
    #show_bar()
    #show_scatter()
    show_word_cloud("wordcloud.txt")

