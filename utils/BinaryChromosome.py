import math
import random


class BinaryChromosome:
    def __init__(self, a, b, precision, num_variables=1):
        self.a = a
        self.b = b
        self.precision = precision
        self.num_variables = num_variables
        self.total_length = num_variables * precision
        self.bits = [random.choice([0, 1]) for _ in range(self.total_length)]

    def get_real_value(self):
        real_values = []
        if self.num_variables == 1:
            binary_str = ''.join(str(bit) for bit in self.bits)
            decimal_value = int(binary_str, 2)
            real_value = self.a + ((self.b - self.a) / (2 ** self.precision - 1)) * decimal_value
            return real_value
        else:
            for i in range(self.num_variables):
                start_index = i * self.precision
                end_index = start_index + self.precision
                binary_str = ''.join(str(bit) for bit in self.bits[start_index:end_index])
                decimal_value = int(binary_str, 2)
                real_value = self.a + ((self.b - self.a) / (2 ** self.precision - 1)) * decimal_value
                real_values.append(real_value)
            return real_values
