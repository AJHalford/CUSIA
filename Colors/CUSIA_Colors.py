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

#cmaps = [('Primary colors', [CUSIAred, CUSIAdarkred, CUSIALightred]),
             #('Secondary color maps', [CUSIAblue, CUSIAgreen, CUSIAyellow, CUSIAneutral, CUSIAgrey]),
             #('multi-color', [CUSIAHot, CUSIACool, CUSIAdivergent, CUSIAredgrey, CUSIAneutralwgreymap, CUSIAJet, CUSIAredyellow, CUSIAbpr, CUSIAplasma, CUSIAviridis, CUSIAcividis, CUSIAxmass, CUSIAaurora])]

def namecolors():
    print('Here are the names of all the primary color maps ')
    print(['reds', 'lightreds', 'darkreds'])
    print('')
    print('Here are the names of the secondary color maps')
    print([ 'blues', 'yellows', 'greens', 'greys'])
    print('')
    print('Here are the neutral color maps')
    print(['neutral', 'CUSIAneutralwgreymap,'])
    print('')
    print('Here are the multi color bars')
    print(['CUSIAHot', 'CUSIACool', 'hotcold', 'CUSIAredgrey',  'CUSIAJet', 'CUSIAredyellow', 'CUSIAbpr', 'CUSIAplasma', 'CUSIAviridis', 'CUSIAcividis', 'CUSIAxmass', 'CUSIAaurora'])
    print('')
    print('')
    print('')
    print('Here are the list of the individual color names')
    print([' darkred', 'red', 'lightred', 'darkblue', 'blue', 'lightblue', 'darkpurple', 'purple', 'lightpurple','darkgreen', 'green', 'lightgreen','darkyellow', 'yellow', 'lightyellow','darkpink', 'pink', 'lightpink', 'darkgrey', 'grey', 'lightgrey'])
    print('')
    print('')
    print('')
    print('To use -')
    print('$import CUSIA_Colors as ccm')
    print('$import matplotlib.pyplot as plt')
    print('$import numpy as np')
    print('$cmap = ccm.mycmap(colors = \'CUSIAredgrey\')')
    print('$x = np.arange(1000)')
    print('$y = np.sin(x/(2.*np.pi*10))')
    print('$plt.scatter(x, y, c=y, cmap = cmap)')
    print('$plt.show()')
    print('')
    print('')
    print('')
    print('Hope you enjoy these fun colorbars :) ')

def mycmap(colors = 'all'):
    if colors == 'all':
        dic_color = {'blues':CUSIAblue, 'yellows':CUSIAyellow, 'greens':CUSIAgreen, 'reds':CUSIAred,'darkreds':CUSIAdarkred,'lightreds':CUSIALightred, 'greys':CUSIAgrey, 'neutral':CUSIAneutral, 'hot':CUSIAHot, 'cool':CUSIACool, 'divergent':CUSIAdivergent, 'CUSIAredgrey':CUSIAredgrey, 'NeutralGrey':CUSIAneutralwgreymap, 'jet':CUSIAJet, 'redyellow':CUSIAredyellow, 'bpr':CUSIAbpr, 'plasma':CUSIAplasma, 'CUSIAviridis':CUSIAviridis, 'CUSIAcividis':CUSIAcividis, 'Xmass':CUSIAxmass, 'Aurora':CUSIAaurora, 'darkred':cdred, 'red':cred, 'lightred':clred, 'darkblue':cdblue, 'blue':cblue, 'lightblue':clblue, 'darkpurple':cdpurple, 'purple':cpurple, 'lightpurple':clpurple,'darkgreen':cdgreen, 'green':cgreen, 'lightgreen':clgreen,'darkyellow':cdyellow, 'yellow':cyellow, 'lightyellow':clyellow,'darkpink':cdpink, 'pink':cpink, 'lightpink':clpink, 'darkgrey':cdgrey, 'grey':cgrey, 'lightgrey':clgrey}

                        
        return dic_color
    #Primary colors
    if colors.lower() in ['light red', 'lightred', 'light_red', 'lr']:
        return CUSIALightred
    if colors.lower() in ['dark red', 'darkred', 'dark_red', 'dr']:
        return CUSIAdarkred
    if colors.lower() in ['red', 'reds', 'r']:
        return CUSIAred

    #Secondary colors
    if colors.lower() in ['blue', 'blues', 'b']:
        return CUSIAblue
    if colors.lower() in ['yellow', 'yellows', 'y']:
        return CUSIAyellow
    if colors.lower() in ['green', 'greens', 'g']:
        return CUSIAgreen
    if colors.lower() in ['grey', 'greys', 'k']:
        return CUSIAgrey

    #Neutral grey
    if colors.lower() in ['neutral', 'neutrals', 'beige']:
        return CUSIAneutral
    if colors.lower() in ['neutral grey', 'neutral_grey', 'neutralgrey']:
        return CUSIAneutralwgreymap
    
    
    #Multicolor [CUSIAHot, CUSIACool, CUSIAdivergent, CUSIAredgrey, CUSIAneutralwgreymap, CUSIAJet, CUSIAredyellow, CUSIAbpr, CUSIAplasma, CUSIAviridis, CUSIAcividis, CUSIAxmass, CUSIAaurora] 
    if colors.lower() in ['cusiahot', 'hotmap', 'hot', 'yor', 'yellow orange red', 'yelloworangered', 'yellow_orange_red', 'yellowred', 'yellowred', 'yellow_red']:
        return hotmap
    if colors.lower() in ['Cusiacool', 'coolmap', 'cool', 'pinkblue', 'pb']:
        return CUSIACool
    if colors.lower() in ['cusiadivergent', 'hotcold', 'rwb', 'redwhiteblue', 'red white blue', 'red_white_blue', 'redblue', 'red blue', 'red_blue']:
        return CUSIAdivergent
    if colors.lower() in ['cusiaredgrey', 'redgrey', 'rwg', 'redwhitegrey', 'red white grey', 'red_white_grey',  'red grey', 'red_grey']:
        return CUSIAredgrey
    if colors.lower() in ['cusiaJet', 'jet', 'newjet', 'new_jet', 'new jet']:
        return CUSIAJet
    if colors.lower() in ['cusiaredyellow', 'diverge', 'rwy', 'redwhiteyellow', 'red white yellow', 'red_white_yellow', 'redyellow', 'red yellow', 'red_yellow']:
        return CUSIAredyellow   
    if colors.lower() in ['cusiabpr', 'coldhot', 'bpr', 'bluepurplered', 'blue purple red', 'blue_purple_red', 'bluered', 'blue red', 'blue_red']:
        return CUSIAbpr
    if colors.lower() in ['cusiaplasma', 'boy', 'plasma', 'newplasma', 'new_plasma', 'new plasma']:
        return CUSIAplasma
    if colors.lower() in ['cusiaviridis', 'bgy', 'viridis', 'new viridis', 'new_viridis', 'newviridis']:
        return CUSIAviridis
    if colors.lower() in ['cusiacividis', 'cividis','newcividis','new_cividis','new cividis' ]:
        return CUSIAcividis
    if colors.lower() in ['cusiaxmass', 'xmass', 'rwg', 'redwhitegreen', 'red white green', 'red_white_green', 'redgreen', 'red green', 'red_green']:
        return CUSIAxmass   
    if colors.lower() in ['cusiaaurora', 'aurora']:
        return CUSIAaurora         
    if colors in ['individual', 'indi', 'single']:
        dic_color = {'darkred':cdred, 'red':cred, 'lightred':clred, 'darkblue':cdblue, 'blue':cblue, 'lightblue':clblue, 'darkpurple':cdpurple, 'purple':cpurple, 'lightpurple':clpurple,'darkgreen':cdgreen, 'green':cgreen, 'lightgreen':clgreen,'darkyellow':cdyellow, 'yellow':cyellow, 'lightyellow':clyellow,'darkpink':cdpink, 'pink':cpink, 'lightpink':clpink, 'darkgrey':cdgrey, 'grey':cgrey, 'lightgrey':clgrey}
        return dic_color
    
