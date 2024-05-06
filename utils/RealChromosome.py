import random

class RealChromosome:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.value = random.uniform(a, b)

    def get_real_value(self):
        return self.value