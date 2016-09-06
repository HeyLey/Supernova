import generator.datafile as df
from config import seconds, minimum, peak, lambd, num


def generate_background():
    return df.generate_random(0, seconds, minimum, peak, lambd)


def generate_signal():
    return df.generate_n_pos([2], num, seconds, minimum, peak, lambd)


