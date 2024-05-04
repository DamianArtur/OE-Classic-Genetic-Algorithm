import random

class RealChromosome:
    def __init__(self, a, b, precision):
        self.a = a
        self.b = b
        self.precision = precision
        self.bits = [random.uniform(a, b) for _ in range(precision)]

    def get_real_value(self):
        return self.bits