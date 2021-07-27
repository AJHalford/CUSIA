##############################################################################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from colorspacious import cspace_converter
from collections import OrderedDict
# these are colorblind friendly on their own and many colormaps work well. But be sure to test on 
#https://www.color-blindness.com/coblis-color-blindness-simulator/
"""     
This program creates dictionaries of colors and colormaps which use the CUISA brand colors. 

Funtion: namecolors():
inputs: none
returns: prints out a list of the colors and colormaps along with how to run an example usage. 

example: 
   ln[]:import CUSIA_Colors as ccm
   ln[]:ccm.namecolors()

Function: mycmap(colors = 'all'):
inputs: colorname, colormap name, all (returns dictionary of all colormaps and colors), or individual (returns dictionary of only the individual colors)
returns: Colormap, color, or dicitionary of all colors and/or colormaps. 

example: 
   ln[]:import CUSIA_Colors as ccm
   ln[]:ccmap = ccm.mycmap(colors ='rwg')
   ln[]:x = np.arange(1000)
   ln[]:y = np.sin(x/(2.*np.pi*10))
   ln[]:plt.scatter(x, y, c=y, cmap = ccmap)
   ln[]:plt.show() 

"""
__version__ = 1.0
__author__ = 'R. Cornell, A.J. Halford and D. Welling'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                               



#First we are defining the primary colors used for these maps
cred = '#BA0C2F'
clred = '#EE2737'
cdred = '#8A1538'

#Secondary Colors
clblue = '#00A3E0'
cblue  = '#0057B7'
cdblue = '#06038D'
clpurple = '#C5299B'
cpurple  = '#9B26B6'
cdpurple = '#5C068C'
clgreen = '#97D700'
cgreen  = '#6CC24A'
cdgreen = '#00965E'
clyellow = '#FFE900'
cyellow  = '#FFC72C'
cdyellow = '#EAAA00'

#Neutral Colors 
clpink = '#ECC3B2'
cpink  = '#EAA794'
cdpink = '#E8927C'
clgrey = '#F3F4F6'# Using this lighter grey to make the most out of the color range '#B6ADA5'
cgrey  = '#696158'
cdgrey = '#2D2926'

#Now we are putting the ones together that we want to go from one to another


#finally we make the actual maps
#Primay
redcolors = [clgrey,  cred]
blackredcolors = [clgrey,  cdred]
whiteredcolors = [clgrey, clred]
CUSIAred = mpl.colors.LinearSegmentedColormap.from_list("", redcolors)
CUSIAdarkred = mpl.colors.LinearSegmentedColormap.from_list("", blackredcolors)
CUSIALightred = mpl.colors.LinearSegmentedColormap.from_list("", whiteredcolors)


#Secondary
bluecolors = [clgrey, cdblue]#[clgrey, clblue, cblue, cdblue, 'k']
greencolors = [clgrey, cdgreen] #[clgrey, clgreen, cdgreen, cdgrey]
yellowcolors = [clyellow, cdgrey]#[clgrey, cdyellow] #[clgrey, clyellow, cdyellow, cdgrey]
greycolors = [clgrey, cdgrey] #[clgrey,cgrey, cdgrey]                                          
CUSIAblue = mpl.colors.LinearSegmentedColormap.from_list("", bluecolors)
CUSIAgreen = mpl.colors.LinearSegmentedColormap.from_list("", greencolors)
CUSIAyellow = mpl.colors.LinearSegmentedColormap.from_list("", yellowcolors)
CUSIAgrey =   mpl.colors.LinearSegmentedColormap.from_list("", greycolors)


#Neutral
neutralcolors = [ clpink, cdgrey]#clgrey, cdpink ]
#neutralwgrey = [clgrey,  cdpink, cdgrey]
CUSIAneutral = mpl.colors.LinearSegmentedColormap.from_list("", neutralcolors)
#CUSIAneutralwgreymap = mpl.colors.LinearSegmentedColormap.from_list("", neutralwgrey)

#Multicolor [CUSIAHot, CUSIACool, CUSIAdivergent, CUSIAneutralwgreymap, CUSIAJet, CUSIAredyellow, CUSIAbpr, CUSIAplasma, CUSIAviridis, CUSIAcividis, CUSIAxmass, CUSIAaurora]
hotcolors = [ clyellow, cdred, cdgrey]
CUSIAHot = mpl.colors.LinearSegmentedColormap.from_list("", hotcolors)

coolcolors = [clpink, cdpink, cdblue]
CUSIACool = mpl.colors.LinearSegmentedColormap.from_list("", coolcolors)

diver = [cdred, clgrey, cdblue]
CUSIAdivergent = mpl.colors.LinearSegmentedColormap.from_list("", diver)

redgrey = [cdred, clgrey, cdgrey]
CUSIAredgrey = mpl.colors.LinearSegmentedColormap.from_list("", redgrey)

neutralwgrey = [clpink, cdpink, cdgrey]
CUSIAneutralwgreymap = mpl.colors.LinearSegmentedColormap.from_list("", neutralwgrey)

cusiajet = [cdblue, cblue, cdgreen, clyellow, cyellow,  cdred]
CUSIAJet =  mpl.colors.LinearSegmentedColormap.from_list("", cusiajet)

redyellow = [cdgrey, cred, clyellow]
CUSIAredyellow =  mpl.colors.LinearSegmentedColormap.from_list("", redyellow)

bpr = [cdblue, cred, clgrey]
CUSIAbpr =  mpl.colors.LinearSegmentedColormap.from_list("", bpr)

cusiaplasma = ['k', cdblue, cpurple, clred, clyellow]
CUSIAplasma =  mpl.colors.LinearSegmentedColormap.from_list("", cusiaplasma)

cusiaviridis = ['k',cpurple, clblue, clyellow]
CUSIAviridis =  mpl.colors.LinearSegmentedColormap.from_list("", cusiaviridis)

cusiacividis = [cdblue, cgrey, clyellow]
CUSIAcividis =  mpl.colors.LinearSegmentedColormap.from_list("", cusiacividis)

xmass = [cdred, clgrey, cdgreen]
CUSIAxmass =  mpl.colors.LinearSegmentedColormap.from_list("", xmass)

cusiaaurora = [clyellow, clpurple, cdblue, cdgreen, clgreen, clred, cdred]
CUSIAaurora =  mpl.colors.LinearSegmentedColormap.from_list("", cusiaaurora)

#We chose trymap for this set of figures

#Here we are setting the text size for the figures. 
txtsize = 12
mpl.rcParams['font.size'] = txtsize
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

cmaps = [('Primary colors', [CUSIAred, CUSIAdarkred, CUSIALightred]),
             ('Secondary color maps', [CUSIAblue, CUSIAgreen, CUSIAyellow, CUSIAneutral, CUSIAgrey]),
             ('multi-color', [CUSIAHot, CUSIACool, CUSIAdivergent, CUSIAredgrey, CUSIAneutralwgreymap, CUSIAJet, CUSIAredyellow, CUSIAbpr, CUSIAplasma, CUSIAviridis, CUSIAcividis, CUSIAxmass, CUSIAaurora])]


nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_category, cmap_list, nrows):
    fig, axes = plt.subplots(nrows=nrows)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        #pos = list(ax.get_position().bounds)
        #x_text = pos[0] - 0.01
        #y_text = pos[1] + pos[3]/2.
        #fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()


for cmap_category, cmap_list in cmaps:
    plot_color_gradients(cmap_category, cmap_list, nrows)

plt.show()
#plt.close()





mpl.rcParams.update({'font.size': 12})

# Number of colormap per subplot for particular cmap categories
_DSUBS = {'Primary colors': 3, 'Secondary color maps': 5,
          'multi-color': 13}

# Spacing between the colormaps of a subplot
_DC = {'Primary colors': 1.4, 'Secondary color maps': 1.4,
       'multi-color': 1.4}

# Indices to step through colormap
x = np.linspace(0.0, 1.0, 100)

# Do plot
for cmap_category, cmap_list in cmaps:

    # Do subplots so that colormaps have enough space.
    # Default is 6 colormaps per subplot.
    dsub = _DSUBS.get(cmap_category, 6)
    nsubplots = int(np.ceil(len(cmap_list) / dsub))

    # squeeze=False to handle similarly the case of a single subplot
    fig, axs = plt.subplots(nrows=nsubplots, squeeze=False,
                            figsize=(7, 2.6*nsubplots))

    for i, ax in enumerate(axs.flat):

        locs = []  # locations for text labels

        for j, cmap in enumerate(cmap_list[i*dsub:(i+1)*dsub]):

            # Get RGB values for colormap and convert the colormap in
            # CAM02-UCS colorspace.  lab[0, :, 0] is the lightness.
            rgb = cm.get_cmap(cmap)(x)[np.newaxis, :, :3]
            lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)

            # Plot colormap L values.  Do separately for each category
            # so each plot can be pretty.  To make scatter markers change
            # color along plot:
            # http://stackoverflow.com/questions/8202605/

            if cmap_category == 'Sequential':
                # These colormaps all start at high lightness but we want them
                # reversed to look nice in the plot, so reverse the order.
                y_ = lab[0, ::-1, 0]
                c_ = x[::-1]
            else:
                y_ = lab[0, :, 0]
                c_ = x

            dc = _DC.get(cmap_category, 1.4)  # cmaps horizontal spacing
            ax.scatter(x + j*dc, y_, c=c_, cmap=cmap, s=300, linewidths=0.0)

            # Store locations for colormap labels
            if cmap_category in ('Perceptually Uniform Sequential',
                                 'Sequential'):
                locs.append(x[-1] + j*dc)
            elif cmap_category in ('Diverging', 'Qualitative', 'Cyclic',
                                   'Miscellaneous', 'Sequential (2)'):
                locs.append(x[int(x.size/2.)] + j*dc)

        # Set up the axis limits:
        #   * the 1st subplot is used as a reference for the x-axis limits
        #   * lightness values goes from 0 to 100 (y-axis limits)
        ax.set_xlim(axs[0, 0].get_xlim())
        ax.set_ylim(0.0, 100.0)

        # Set up labels for colormaps
        ax.xaxis.set_ticks_position('top')
        ticker = mpl.ticker.FixedLocator(locs)
        ax.xaxis.set_major_locator(ticker)
        formatter = mpl.ticker.FixedFormatter(cmap_list[i*dsub:(i+1)*dsub])
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_tick_params(rotation=50)
        ax.set_ylabel('Lightness $L^*$', fontsize=12)

    ax.set_xlabel(cmap_category + ' colormaps', fontsize=14)

    fig.tight_layout(h_pad=0.0, pad=1.5)
    plt.show()
