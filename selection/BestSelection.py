from selection.Selection import Selection 

class BestSelection(Selection):

    def select(self, percentage=0.1):
        population = self.population.get_population()

        function_values = [self.function.compute(individual) for individual in self.population.get_population_value()]
        population_with_function_values = list(zip(population, function_values))
        
        if self.minimization:
            sorted_population = sorted(population_with_function_values, key=lambda x: x[1])
        else:
            sorted_population = sorted(population_with_function_values, key=lambda x: x[1], reverse=True)
        
        num_best = int(len(sorted_population) * percentage)
        best_individuals = [item[0] for item in sorted_population[:num_best]]
        
        while len(best_individuals) < len(population):
            best_individuals.extend(best_individuals)
        
        if len(best_individuals) > len(population):
            best_individuals = best_individuals[:len(population)]
        
        return best_individuals