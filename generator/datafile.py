import random
import numpy as np

from generator import background, signal


def generate_random(probability, seconds, minimum, peak, lambd):
    data = np.zeros(seconds * 200)
    for i in range(0, seconds * 200, 200):
        if random.random() > probability:
            data[i:(i + 200)] = background.block_norm(lambd)
        else:
            data[i:(i + 200)] = signal.block_peak(minimum, peak)
    return data


def generate_n_random(n, seconds, minimum, peak, lambd):
    data = np.zeros(seconds * 200)
    pos = random.sample(range(1, seconds + 1), n)
    pos = np.sort(pos)
    k = 0
    j = pos[k]
    for i in range(0, seconds * 200, 200):
        if i / 200 == j - 1:
            data[i:(i + 200)] = signal.block_peak(minimum, peak)
            n -= 1
            if n > 0:
                k += 1
                j = pos[k]
        else:
            data[i:(i + 200)] = background.block_norm(lambd)
    return data


def generate_n_pos(pos, n, seconds, minimum, peak, lambd):
    data = np.zeros(seconds * 200)
    np.sort(pos)
    k = 0
    j = pos[k]
    for i in range(0, seconds * 200, 200):
        if i / 200 == j - 1:
            data[i:(i + 200)] = signal.block_peak(minimum, peak)
            n -= 1
            if n > 0:
                k += 1
                j = pos[k]
        else:
            data[i:(i + 200)] = background.block_norm(lambd)
    return data






