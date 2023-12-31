"""
======
pie(x)
======

See `~matplotlib.axes.Axes.pie`.
"""
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('_mpl-gallery-nogrid')

def show_result(odd_pon, odd_kong):
       
       # make data
       x = [odd_pon, odd_kong, 1-odd_pon-odd_kong]
       colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

       # plot
       fig, ax = plt.subplots()
       ax.pie(x, colors=colors, radius=3, center=(4, 4),
              wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

       ax.set(xlim=(0, 8),
              ylim=(0, 8))
       ax.set_yticks([])
       ax.set_xticks([])

       pie_wedges, texts, autotexts = ax.pie(x, colors=colors, radius=3, center=(4, 4),
                                          wedgeprops={"linewidth": 1, "edgecolor": "white"}, autopct='%1.1f%%', frame=True)

       labels = ['Pon', 'Kong', "None"]
       for text, autotext, label in zip(texts, autotexts, labels):
              text.set_text(label)
              text.set_fontsize(8)
              autotext.set_fontsize(8)


       plt.show()
