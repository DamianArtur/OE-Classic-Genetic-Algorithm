from Selection import Selection 

class BestSelection(Selection):

    def select(self, percentage=0.1):
        if self.minimization:
            sorted_population = sorted(self.population)
        else:
            sorted_population = sorted(self.population, reverse=True)
        num_best = int(len(sorted_population) * percentage)
        return sorted_population[:num_best]