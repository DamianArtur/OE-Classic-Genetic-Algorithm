import numpy as np
import benchmark_functions as bf

class Rosenbrock:

    def compute(self, x):

        x = np.array([chromosome for chromosome in x])
        return bf.Rosenbrock(len(x))(x)