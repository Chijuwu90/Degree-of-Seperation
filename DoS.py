# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:43:33 2019

visualization of degree of seperation

@author: ChiJuWu
"""

import numpy
import seaborn 
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


N = numpy.linspace(5, 10, 21) # population
K = numpy.linspace(10, 110, 21) # acquaintances per node

sp = numpy.zeros(shape=(21,21))

for i in range(len(N)):
    for j in range(len(K)):
        sp[j,i] = ( numpy.log(10**N[i])/numpy.log(K[j]) )

pop = [r'$10^5$', ' ', ' ', ' ', r'$10^6$', ' ', ' ', ' ', r'$10^7$', ' ', ' ', ' ', r'$10^8$', ' ', ' ', ' ', r'$10^9$', ' ', ' ', ' ', r'$10^{10}$']
acq = ['10', ' ', ' ', ' ', ' ', ' ', ' ', '40', ' ', ' ', ' ', ' ', ' ', ' ', '70', ' ', ' ', ' ', ' ', ' ', '100']

seaborn.set(font_scale=2.5)
plt.figure(figsize=(20,15))
ax = seaborn.heatmap(sp, xticklabels=pop, yticklabels=acq, cbar_kws={'label': 'Separation'})
ax.invert_yaxis()
plt.xlabel('Population')
plt.ylabel('Acquaintance per person (node)')

ax2 = ax.twiny()
ax2.set_xlabel("Countries")
ax2.set_xlim(5, 10)
ax2.set_xticks([6.99, 7.82, 8.15, 8.52, 9.15, 9.88])
ax2.set_xticklabels(['UAE', 'UK', 'RU', 'US','Ch & In','World'])