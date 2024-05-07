import numpy as np
import benchmark_functions as bf

class StyblinskiTang():

    def compute(self, x):
        x = np.array([chromosome for chromosome in x])

        return bf.StyblinskiTang(len(x))(x)
