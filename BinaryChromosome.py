import random
import math
class BinaryChromosome:
    def __init__(self, a, b, precision):
        self.a = a
        self.b = b
        self.precision = precision
        self.interval_length = (b - a) * (10 ** precision)
        self.total_length = math.ceil(math.log2(self.interval_length) + math.log2(1))
        print(self.total_length)
        self.bits = [random.choice([0, 1]) for _ in range(self.total_length)]

class GeneticAlgorithm:
    def __init__(self, population_size, a, b, precision, num_epochs):
        self.population_size = population_size
        self.a = a
        self.b = b
        self.precision = precision
        self.num_epochs = num_epochs
        self.population = [BinaryChromosome(a, b, precision) for _ in range(population_size)]
    def run(self):
            for epoch in range(self.num_epochs):
                pass

# population_size = 100
# a = -10
# b = 10
# precision = 6
# num_epochs = 50
#
# genetic_algo = GeneticAlgorithm(population_size, a, b, precision, num_epochs)
# print("Populacja")
# for i in range(population_size):
#     print(genetic_algo.population[i].bits)
#
# print("Liczba epok:", genetic_algo.num_epochs)