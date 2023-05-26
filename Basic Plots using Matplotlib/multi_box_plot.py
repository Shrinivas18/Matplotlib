# -*- coding: utf-8 -*-
"""Multi_Box_Plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fIEtZSyCTGi5Ev8R3975BFWNrlwBFmI
"""

import numpy as np
import matplotlib.pyplot as plt

"""**Multi Box Plot**"""

x=[10,20,30,40,50,60,70]
x1=[10,30,40,50,70,80,90]
x2=x=[20,30,50,60,70,60]

y=[x,x1,x2]  # make a list comprises of different data inputs of a box plot 

plt.boxplot(y, labels=["python","C++","Java"], showmeans=True, boxprops=dict(color="r") ,
            capprops=dict(color="b") , whiskerprops=dict(color="y"))

plt.title("Multi-Box Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")  

plt.show()