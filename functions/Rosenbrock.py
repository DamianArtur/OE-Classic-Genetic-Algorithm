import numpy as np

class Rosenbrock:

    def compute(self, x):
        return np.sum(100.0*(x - x**2.0)**2.0 + (1 - x)**2.0)

    def num_variables(self):
        return "Multi"