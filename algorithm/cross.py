import random


# Cross function (score of best kernel -> 0)
def cross(kern1, kern2):
    a = random.random()
    new_kern = kern1 * a + (1-a) * kern2
    return new_kern

