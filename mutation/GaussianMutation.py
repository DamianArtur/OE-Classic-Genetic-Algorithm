import numpy as np

class GaussianMutation:
    def __init__(self, population, sigma):
        self.population = population
        self.sigma = sigma
    def mutate(self):
        mutated_population = []
        for individual in self.population:
            mutated_individual = []
            for gene in individual:
                mutated_gene = gene + np.random.normal(0, self.sigma)
                mutated_individual.append(mutated_gene)
            mutated_population.append(mutated_individual)
        return mutated_population