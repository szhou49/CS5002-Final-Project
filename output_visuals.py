
import matplotlib.pyplot as plt
import numpy as np



def get_values(result):

    value_tiles = []
    for i in range(len(result)):
        if i % 10 == 0:
            continue
        else:
            value_tiles.append(result[i]["value"])
    show_result(value_tiles)


def show_result(list):

    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    non_zero_x = []
    x_label = []  
    x = 0 + np.arange(38)

    for i in range(len(list)):
        if list[i] == 0:
            continue
        non_zero_x.append(x[i])
        if 0 <= i <= 8:
            x_label.append(str(i + 1) + "m")
        elif 9 <= i <= 17:
            x_label.append(str(i - 8) + "s")
        elif 18 <= i <= 26:
            x_label.append(str(i - 17) + "p")
        elif i == 27:
            x_label.append("East")
        elif i == 28:
            x_label.append("South")
        elif i == 29:
            x_label.append("West")
        elif i == 30:
            x_label.append("North")
        elif i == 31:
            x_label.append("Red")
        elif i == 32:
            x_label.append("White")
        elif i == 33:
            x_label.append("Green")

    for i in range(len(list)):
        if list[i] != 0:
            markerline, stemlines, baseline = ax.stem([x[i]], [list[i]])
            plt.setp(stemlines, 'linewidth', 15)
            plt.setp(markerline, markersize=25)

    ax.set_ylim(bottom=0)
    ax.set_xticks(non_zero_x)
    ax.set_yticks(list)
    ax.set_xticklabels(x_label)
    ax.set_yticklabels(list)
    plt.show()
