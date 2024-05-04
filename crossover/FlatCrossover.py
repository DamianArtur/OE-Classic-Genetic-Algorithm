import random

class FlatCrossover:
    def crossover(self, parent_1, parent_2):
        assert len(parent_1) == len(parent_2) == 2, "Each parent must have two genes"

        print("Interval for x new:", (parent_1[0], parent_2[0]))
        print("Interval for y new:", (parent_1[1], parent_2[1]))

        x_new = random.uniform(parent_1[0], parent_2[0])
        y_new = random.uniform(parent_1[1], parent_2[1])

        child = [x_new, y_new]

        return child


# Przykład do testowania
if __name__ == "__main__":
    flat_crossover_operator = FlatCrossover()

    # Osobniki rodzicielskie
    parent_1 = [2, 3]
    parent_2 = [4, 8]

    print("Parent 1:", parent_1)
    print("Parent 2:", parent_2)

    # Krzyżowanie płaskie
    child = flat_crossover_operator.crossover(parent_1, parent_2)

    print("Child:", child)