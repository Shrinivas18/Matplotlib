# -*- coding: utf-8 -*-
"""Multi_Bar_Plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fIEtZSyCTGi5Ev8R3975BFWNrlwBFmI
"""

import numpy as np
import matplotlib.pyplot as plt

"""**Multi-Bar Graph**"""

x=["Python","C","C++","Java"]
y=[95,70,60,92]
z=[80,40,50,70]

width=0.2
p=np.arange(len(x))
p1=[j+width for j in p ]

plt.xlabel("Languages",fontsize=15)
plt.ylabel("Percentage",fontsize=10)
plt.title("Multi Bar Graph",fontsize=20)

plt.bar(p,y,width,color='m',label="popularity")
plt.bar(p1,z,width,color='y',label="popularity1")
plt.xticks(p+width/2,x)

plt.legend(loc="upper center")
plt.show()