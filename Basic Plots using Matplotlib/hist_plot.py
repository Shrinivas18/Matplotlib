# -*- coding: utf-8 -*-
"""Hist_Plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fIEtZSyCTGi5Ev8R3975BFWNrlwBFmI
"""

import numpy as np
import matplotlib.pyplot as plt

"""**HIST PLOT**"""

import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(1,100,50)
l=(10,20,30,40,100)
plt.hist(x,bins=l,edgecolor='r')
plt.xlabel("X-Axis",fontsize=10)
plt.ylabel("Y-Axis",fontsize=10)
plt.title("Hist Plot",fontsize=20)
plt.show()