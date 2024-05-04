from utils.BinaryChromosome import BinaryChromosome
from utils.RealChromosome import RealChromosome


class Population:
    def __init__(self, population_size, a, b, precision):
        self.population_size = population_size
        self.a = a
        self.b = b
        self.precision = precision
        self.population = [BinaryChromosome(a, b, precision) for _ in range(population_size)]
        # self.population = [RealChromosome(a, b, precision) for _ in range(population_size)]

    def get_population(self):
        return self.population

    def get_population_value(self):
        return [chromosome.get_real_value() for chromosome in self.population]
