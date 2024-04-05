from BinaryChromosome import BinaryChromosome
class Population:
    def __init__(self, population_size, a, b, precision):
        self.population_size = population_size
        self.a = a
        self.b = b
        self.precision = precision
        self.population = [BinaryChromosome(a, b, precision) for _ in range(population_size)]