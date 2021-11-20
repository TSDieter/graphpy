import matplotlib.pyplot as plt
import numpy as np
################################################################################
def k(x):
    y = -0,145 * x * x * x + 5,43 * x * x - 52,43 * x + 156
    return y

def wertetabelle(funk, xvon, xbis):
    print("x\ty")
    for x in range(xvon, xbis+1):
        print(x, "\t", funk(x))

def nullstelle(funk, xvon, xbis):
    x = xvon
    y = funk(x)
    vorzeichen = y > 0

def zeichne(funk, xvon, xbis):
    xs = range(xvon, xbis+1)
    ys = []
    for x in xs:
        y = funk(x)
        ys.append(y)
    plt.plot(xs, ys)
    plt.show()
    
wertetabelle(k, -3, 8)
zeichne(k, -3, 8)
#Code by DK 
