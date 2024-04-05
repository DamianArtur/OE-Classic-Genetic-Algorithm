import random
import math
class BinaryChromosome:
    def __init__(self, a, b, precision):
        self.a = a
        self.b = b
        self.precision = precision
        self.interval_length = (b - a) * (10 ** precision)
        self.total_length = math.ceil(math.log2(self.interval_length) + math.log2(1))
        self.bits = [random.choice([0, 1]) for _ in range(self.total_length)]