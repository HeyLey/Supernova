import numpy as np
from graphics.drawing import show_gr
from generator import datafile


s = 3          # length the number of seconds in the file
m = 3            # rough minimum signal value
p = 8           # rough signal peak value
l = 3            # lambda of poisson distribution
f = 0            # occurrence probability of the signal in the file (0 <= f <= 1)
n = 1            # the number of signals (n > 0 && n <= s)
pos = [2] # start positions (pos is from 1 to s)


# Set value 1 for random file of signal
# Set value 2 for random file for *n* signals
# Set value 3 for file for *n* signals in start positions *pos*
met = 3


# -----------------------------

if met == 1:
    data = datafile.generate_random(f, s, m, p, l)
if met == 2:
    data = datafile.generate_n_random(n, s, m, p, l)
if met == 3:
    data = datafile.generate_n_pos(pos, n, s, m, p, l)


np.savetxt("out.txt", data, fmt='%d')


# graph
show_gr(data, s, 'data')