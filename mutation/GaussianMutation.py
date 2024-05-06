import numpy as np
from mutation.Mutation import Mutation
import random

class GaussianMutation(Mutation):
    def mutate(self):
        for individual in self.population:
            for chromosome in individual:
                if random.random() < self.probability:
                    gene_value = chromosome.get_real_value()
                    mutated_gene = gene_value + np.random.normal(0, 1)
                    chromosome.value = mutated_gene