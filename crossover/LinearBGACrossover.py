import random

class LinearBGACrossover:
    def __init__(self, lower_bounds, upper_bounds):
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds

    def crossover(self, parent_x, parent_y, alpha, k):
        assert len(parent_x) == len(parent_y) == len(self.lower_bounds) == len(self.upper_bounds)
        child = []

        for i in range(len(parent_x)):
            x_lower = self.lower_bounds[i]
            x_upper = self.upper_bounds[i]
            x = parent_x[i]
            y = parent_y[i]
            rnd = random.uniform(0, 1)
            if rnd <= 0.9:
                child_i = x - 0.5 * (x_upper - x_lower) * 2**(-k*alpha) * (y - x) / (parent_x[i] - parent_y[i])
            else:
                child_i = x + 0.5 * (x_upper - x_lower) * 2**(-k*alpha) * (y - x) / (parent_x[i] - parent_y[i])

            child_i = max(x_lower, min(x_upper, child_i))
            child.append(child_i)
        return child