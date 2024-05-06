import random

from selection.Selection import Selection

class TournamentSelection(Selection):

    def __init__(self, population, function, tournament_size):
        super().__init__(population, function)
        self.tournament_size = tournament_size

    def select(self):
        selected_individuals = []

        pop = self.population.get_population()
        values = self.population.get_population_value()

        for _ in range(len(pop)):
            tournament = random.sample(values, self.tournament_size)
            
            if self.minimization:
                best_individual = values.index(min(tournament))
            else:
                best_individual = values.index(max(tournament))
                
            selected_individuals.append(pop[best_individual])

        return selected_individuals
