import numpy as np


def get_z(z, x, y):
    return np.array([[z]*len(x), [z]*len(y)])
