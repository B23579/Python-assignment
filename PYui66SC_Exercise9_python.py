""" plot the sum of function"""
import numpy as np
import pylab as pl
x = np.linspace(-2,2,40)
k=np.arange(1,6,2)
y=0
tab = list()
for  i in x :
    y=0
    for j in k:
        y = y + 4/(j*np.pi)*np.sin(j*np.pi*i/2)
    tab.append(y)
pl.show()
pl.plot(x,tab,'red', )
pl.title('Graphe pour kmax = 6')

""" Graphe for kmax= 26"""
tab = list()
k=np.arange(1,26,2)
for  i in x :
    y=0
    for j in k:
        y = y + 4/(j*np.pi)*np.sin(j*np.pi*i/2)
    tab.append(y)
pl.show()
pl.plot(x,tab,'green')
pl.title('Graphe pour kmax = 26')
