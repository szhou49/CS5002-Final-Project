
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

    x = 0 + np.arange(38)

    for i in range(len(list)):
        if list[i] != 0:
            ax.plot(i, list[i])
            non_zero_x.append(x[i])

    for i in range(len(list)):
        if list[i] != 0:
            markerline, stemlines, baseline = ax.stem([x[i]], [list[i]])
            plt.setp(stemlines, 'linewidth', 15)
            plt.setp(markerline, markersize=25)


    ax.set_ylim(bottom=0)
    ax.set_xticks(non_zero_x)
    ax.set_yticks(list)
    ax.set_xticklabels(non_zero_x)
    ax.set_yticklabels(list)
    plt.show()
