import numpy as np

class StyblinskiTang():

    def compute(self, x):
        return np.sum(x**4 - 16*x**2 + 5*x) / 2.0