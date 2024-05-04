import random

class LinearBGACrossover:
    def __init__(self, lower_bounds, upper_bounds):
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds

    def crossover(self, parent_x, parent_y, alpha, k):
        assert len(parent_x) == len(parent_y) == len(self.lower_bounds) == len(self.upper_bounds), "Chromosomes must have the same length as bounds"

        child = []

        for i in range(len(parent_x)):
            x_lower = self.lower_bounds[i]
            x_upper = self.upper_bounds[i]
            x = parent_x[i]
            y = parent_y[i]

            # rnd = random.uniform(0, 1)
            # print(rnd)

            rnd = 0.4

            if rnd <= 0.9:
                child_i = x - 0.5 * (x_upper - x_lower) * 2**(-k*alpha) * (y - x) / (parent_x[i] - parent_y[i])
            else:
                child_i = x + 0.5 * (x_upper - x_lower) * 2**(-k*alpha) * (y - x) / (parent_x[i] - parent_y[i])

            # Ograniczenie wartości potomka do przedziału [x_lower, x_upper]
            child_i = max(x_lower, min(x_upper, child_i))

            child.append(child_i)

        return child


# Przykład do testowania
if __name__ == "__main__":
    lower_bounds = [0, 0]
    upper_bounds = [10, 10]
    bga_crossover_operator = LinearBGACrossover(lower_bounds, upper_bounds)

    # Osobniki rodzicielskie
    parent_x = [2, 3]
    parent_y = [4, 8]

    print("Parent X:", parent_x)
    print("Parent Y:", parent_y)
    alpha = 0.1
    print("Alpha:", alpha)
    k = 1  # Stała precyzji

    # Krzyżowanie LBGAX
    child = bga_crossover_operator.crossover(parent_x, parent_y, alpha, k)

    print("Child:", child)
