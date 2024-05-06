import numpy as np

class Rosenbrock:

    def compute(self, x):

        x_values = [chromosome for chromosome in x]
        x_values = np.array(x_values)

        return np.sum(100.0*(x_values[1:] - x_values[:-1]**2.0)**2.0 + (1 - x_values[:-1])**2.0)
