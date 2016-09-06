import random
import numpy as np
from algorithm.score import calculate_loss, calculate_grad
from algorithm.score2 import train_data_bkg, train_data_sgn, calculate
from generator.generate import generate_signal, generate_background, seconds
from graphics import drawing
from config import files_num, n, eps, population_size, pos

kernels = []


def init_ver2():
    for l in range(files_num):
        train_data_bkg.append(generate_background())

    for l in range(files_num):
        train_data_sgn.append(generate_signal())

init_ver2()

kernel = np.ones(201) / 50000

step = 1e-8

for i in range(10000):
    print("epoch: {}".format(i))
    mean_loss = 0

    for j in range(100):
        train_data_bkg.clear()
        train_data_sgn.clear()
        init_ver2()

        loss = calculate_loss(kernel)

        grad = calculate_grad(kernel)
        kernel += grad * step

        mean_loss += calculate_loss(kernel) / 100

    print("mean loss: {}".format(mean_loss))

    print(kernel.tolist())
    print()


best_kernel = kernel[:-1]

err1 = 0.0

for k in range(10000):
    filtered = np.convolve(generate_background(), best_kernel, mode='valid') + kernel[-1] * 100
    if max(filtered) > 0.75:
        err1 += 1.0 / 10000

print("Err1: {}".format(err1))

err2 = 0.0

for k in range(10000):
    filtered = np.convolve(generate_signal(), best_kernel, mode='valid') + kernel[-1] * 100
    if max(filtered) < 0.75:
        err2 += 1.0 / 10000

print("Err2: {}".format(err2))

np.savetxt("best_kernel.txt", best_kernel)

filtered_bg = np.convolve(generate_background(), best_kernel, mode='valid') + kernel[-1] * 100
filtered_sg = np.convolve(generate_signal(), best_kernel, mode='valid') + + kernel[-1] * 100

drawing.show_conv(filtered_bg, seconds, 'filtered_background')
drawing.show_conv(filtered_sg, seconds, 'filtered_signal')
drawing.show_conv(best_kernel, 200, 'kernel')

