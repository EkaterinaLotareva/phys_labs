import numpy as np
from matplotlib import pyplot as plt
from math import pi
#import main

def ellips(a, b):
    plt.figure(figsize=(4, 6))
    plt.axes(xlim=(-0.4, 0.4), ylim=(-0.6, 0.6))

    t = np.linspace(0, 2*pi, 100)
    plt.plot( a*np.cos(t) , b*np.sin(t) )
    plt.grid(color='lightgray',linestyle='--')
    plt.minorticks_on()
    plt.show()

ellips(0.2, 0.3)