import matplotlib.pyplot as plt
import numpy as np


def show_gr(g, sec, name):
    x = np.linspace(1, sec + 1, sec * 200)
    plt.step(x, g)
    plt.title(name)
    plt.show()


def show_conv(g, sec, name):
    x = np.linspace(1, sec + 1, len(g))
    plt.plot(x, g)
    plt.title(name)
    plt.show()
