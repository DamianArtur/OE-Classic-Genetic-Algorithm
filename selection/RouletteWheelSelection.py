import random

from selection.Selection import Selection

class RouletteWheelSelection(Selection):

    def select(self):
        
        fitness = [self.function.compute(individual) for individual in self.population.get_population_value()]
        min_fitness = min(fitness)
        adjusted_population = [individual - min_fitness for individual in fitness]
        
        if self.minimization:
            adjusted_population = [1/fitness for fitness in adjusted_population]

        total_fitness = sum(adjusted_population)
        
        selected_individuals = []
        pop = self.population.get_population()
        for _ in range(len(pop)):
        
            pick = random.uniform(0, total_fitness)
            
            current = 0
            for index, individual in enumerate(fitness):
                current += adjusted_population[index]
                if current > pick:
                    selected_individuals.append(pop[index])
                    break

        return selected_individuals
