import numpy as np

class StyblinskiTang():

    def compute(self, x):
        x_values = [chromosome.get_real_value() for chromosome in x]
        x = np.array(x_values)
        return np.sum(x**4 - 16*x**2 + 5*x) / 2.0
