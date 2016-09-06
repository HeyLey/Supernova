import numpy as np


train_data_sgn = []
train_data_bkg = []


#  Loss function (score of best kernel -> 0)
def calculate(kern):
    score = 0
    all_max = []

    for track in train_data_sgn:
        fs = np.convolve(track, kern, mode='valid')
        all_max.append(fs.max())

    for track in train_data_bkg:
        bg_conv = np.convolve(track, kern, mode='valid')

        bg_max = bg_conv.max()

        for fs_max in all_max:
            if bg_max > fs_max:
                score += sum(bg_conv > fs_max)

    return score
