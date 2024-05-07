from utils.BinaryChromosome import BinaryChromosome
from utils.RealChromosome import RealChromosome


class Population:
    # def __init__(self, population_size, num_variables, a, b, precision):
    #     self.population_size = population_size
    #     self.num_variables = num_variables
    #     self.a = a
    #     self.b = b
    #     self.precision = precision
    #     self.population = [[BinaryChromosome(a, b, precision) for _ in range(num_variables)] for _ in range(population_size)]
    def __init__(self, population_size, num_variables, a, b):
        self.population_size = population_size
        self.num_variables = num_variables
        self.a = a
        self.b = b
        self.population = [[RealChromosome(a, b) for _ in range(num_variables)] for _ in range(population_size)]

    def get_population(self):
        return self.population

    def get_population_value(self):
        return [[chromosome.get_real_value() for chromosome in individual] for individual in self.population]

    def get_individual(self, index):
        return self.population[index]

    def set_individual(self, index, individual):
        self.population[index] = individual

    def get_individual_value(self, index):
        return [chromosome.get_real_value() for chromosome in self.population[index]]
