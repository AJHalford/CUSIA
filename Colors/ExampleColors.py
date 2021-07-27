import CUSIA_Colors as ccm
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

ccmap = ccm.mycmap(colors ='CUSIAredgrey')

x = np.arange(1000)
y = np.sin(x/(2.*np.pi*10))

plt.scatter(x, y, c=y, cmap = ccmap)
plt.show()
#plt.close()

np.random.seed(19680801)
data = np.random.randn(2, 100)

indicolors = ccm.mycmap(colors = 'individual')
histcolor = indicolors['red']
histedgecolor = indicolors['blue']
cmap1 = ccm.mycmap(colors = 'neutralgrey')
lincolor = indicolors['green']
cmap2 = ccm.mycmap(colors = 'CUSIAxmass')


fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0], color = histcolor, ec=histedgecolor)
axs[1, 0].scatter(data[0], data[1], c = data[1], cmap = cmap1 )
axs[0, 1].plot(data[0], data[1], c = lincolor)
plt.hist2d(data[0], data[1], cmap = cmap2)
plt.colorbar()
plt.show()

cmap3 = ccm.mycmap(colors = 'CUSIAcividis')
x, y = np.mgrid[-5:5:0.05, -5:5:0.05]
z = (np.sqrt(x**2 + y**2) + np.sin(x**2 + y**2))

fig, ax = plt.subplots(1,1)
im = ax.imshow(z, cmap=cmap3)
fig.colorbar(im)

plt.show()


cmap4 = ccm.mycmap(colors = 'CUSIAaurora')
x, y = np.mgrid[-5:5:0.05, -5:5:0.05]
z = (np.sqrt(x**2 + y**2) + np.sin(x**2 + y**2))

fig, ax = plt.subplots(1,1)
im = ax.imshow(z, cmap=cmap4)
fig.colorbar(im)
plt.show()
