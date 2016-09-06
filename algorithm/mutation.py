import random
import numpy as np

# Mutation function


def mutation(kernel):
    new_kernel = np.copy(kernel)
    index = random.randint(0, len(new_kernel) - 1)
    new_kernel[index] += random.gauss(0, 0.0001)
    return new_kernel

