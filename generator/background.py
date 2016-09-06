import numpy as np

# constant number of values in block 1sec
bl_length = 200

# returns an array of length 200 with the background values
# @param l  lambda poisson distribution
def block_norm(l):
    return np.random.poisson(l, bl_length)

