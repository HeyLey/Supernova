import numpy as np
from algorithm.score2 import train_data_sgn, train_data_bkg


# Signal should be after filtration greater than 1 and noise - less than 0.5
# Else gap = error
def fitness_function(data, is_signal):
    if is_signal:
        return min(0, max(data) - 1)
    else:
        return min(0, 0.5 - max(data))


#  Loss function (score of best kernel -> 0)
def calculate_loss(kern):
    scr = 0

    for track in train_data_sgn:
        fb = np.convolve(track, kern[:-1], mode='valid') + kern[-1] * 100
        scr -= fitness_function(fb, True)

    for track in train_data_bkg:
        fb = np.convolve(track, kern[:-1], mode='valid') + kern[-1] * 100
        scr -= fitness_function(fb, False)

    return scr


def calculate_grad(kern):
    grad = np.zeros(len(kern))
    grad[:-1] -= 0.1 * np.sign(kern[:-1])

    data_num = 0
    bg_num = 0

    for track in train_data_sgn:
        fb = np.convolve(track, kern[:-1], mode='valid') + kern[-1] * 100
        if max(fb) < 1:
            data_num += 1
            i = np.argmax(fb)
            grad[:-1] += track[i:i + 200][::-1]
            grad[-1] += 100

    for track in train_data_bkg:
        fb = np.convolve(track, kern[:-1], mode='valid') + kern[-1] * 100
        if max(fb) > 0.5:
            bg_num += 1
            i = np.argmax(fb)
            grad[:-1] -= track[i:i + 200][::-1]
            grad[-1] -= 100

    #print("data={}, bg={}".format(data_num, bg_num))
    return grad / (len(train_data_bkg) + len(train_data_sgn))
