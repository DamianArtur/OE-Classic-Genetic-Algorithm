import random

class FlatCrossover:
    def crossover(self, parent_1, parent_2):
        assert len(parent_1) == len(parent_2) == 2
        x_new = random.uniform(parent_1[0], parent_2[0])
        y_new = random.uniform(parent_1[1], parent_2[1])
        child = [x_new, y_new]
        return child