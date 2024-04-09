import random

from Selection import Selection

class RouletteWheelSelection(Selection):

    def __init__(self, population):
        super().__init__(population)

    def select(self):
        min_fitness = min(individual.fitness for individual in self.population.get_population_values())
        adjusted_population = [individual.fitness - min_fitness for individual in self.population.get_population_values()]
        
        if self.minimization:
            adjusted_population = [1/fitness for fitness in adjusted_population]

        total_fitness = sum(adjusted_population)
        
        selected_individuals = []
        for _ in range(len(self.population.get_population_values())):
        
            pick = random.uniform(0, total_fitness)
            
            current = 0
            for index, individual in enumerate(self.population.get_population_values()):
                current += adjusted_population[index]
                if current > pick:
                    selected_individuals.append(individual)
                    break

        return selected_individuals
