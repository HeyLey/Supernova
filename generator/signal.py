import numpy as np
import math


# constant number of values in block 1sec
bl_length = 200


# returns an array of length 200 with the signal values
# @param m  minimum signal value
# @param p  signal peak value
def block_peak(m, p):
    mod = np.zeros(bl_length)
    diff = p - m
    for l in range(bl_length):
        shift = (l - 4) * 0.01
        mod[l] = np.random.poisson(m + diff * math.exp(-shift ** 2), 1)
    return mod
