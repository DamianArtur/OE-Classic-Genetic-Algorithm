from utils.BinaryChromosome import BinaryChromosome

class Population:
    def __init__(self, population_size, a, b, precision, num_variables=1):
        self.population_size = population_size
        self.a = a
        self.b = b
        self.precision = precision
        self.num_variables = num_variables
        self.population = [BinaryChromosome(a, b, precision, num_variables) for _ in range(population_size)]

    def get_population(self):
        return self.population

    def get_population_value(self):
        if self.population[0].num_variables == 1:
            # For single-variable chromosomes
            return [chromosome.get_real_value() for chromosome in self.population]
        else:
            # For multi-variable chromosomes
            return [[chromosome.get_real_value() for chromosome in individual] for individual in self.population]
