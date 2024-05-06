import random
from mutation.Mutation import Mutation

class UniformMutation(Mutation):
    def mutate(self):
        for individual in self.population:
            min_value = min(chromosome.get_real_value() for chromosome in individual)
            max_value = max(chromosome.get_real_value() for chromosome in individual)
            for i in range(len(individual)):
                if random.random() < self.probability:

                    individual[i].value = random.uniform(min_value, max_value)
