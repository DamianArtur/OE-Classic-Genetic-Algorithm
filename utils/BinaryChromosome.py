import math
import random


class BinaryChromosome:
    def __init__(self, a, b, precision):
        self.a = a
        self.b = b
        self.precision = precision
        self.interval_length = (b - a) * (10 ** precision)
        self.total_length = math.ceil(math.log2(self.interval_length) + math.log2(1))
        self.bits = [random.choice([0, 1]) for _ in range(self.total_length)]

    def get_real_value(self):
        binary_str = ''.join(str(bit) for bit in self.bits)
        decimal_value = int(binary_str, 2)
        real_value = self.a + ((self.b - self.a) / (2**self.total_length - 1)) * decimal_value
        return real_value