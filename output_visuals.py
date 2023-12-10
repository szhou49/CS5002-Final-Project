
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = 0 + np.arange(38)
y = [0, 0, 0, 33, 33, 0, 0, 0, 0, 0, 37, 0, 22, 15, 15, 0, 37, 0, 20, 0, 0, 0, 0, 0, 0, 0, 24, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0]

fig, ax = plt.subplots()
non_zero_x = []

for i in range(len(y)):
    if y[i] != 0:
        ax.plot(i, y[i])
        non_zero_x.append(x[i])

for i in range(len(y)):
    if y[i] != 0:
        markerline, stemlines, baseline = ax.stem([x[i]], [y[i]])
        plt.setp(stemlines, 'linewidth', 15)
        plt.setp(markerline, markersize=25)

ax.set_ylim(bottom=0)
ax.set_xticks(non_zero_x)
ax.set_yticks(y)
ax.set_xticklabels(non_zero_x)
ax.set_yticklabels(y)
plt.show()
