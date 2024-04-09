from selection.Selection import Selection 

class BestSelection(Selection):

    def select(self, percentage=0.1):
        if self.minimization:
            sorted_population = sorted(self.population.get_population_values())
        else:
            sorted_population = sorted(self.population.get_population_values(), reverse=True)
        num_best = int(len(sorted_population) * percentage)
        return sorted_population[:num_best]