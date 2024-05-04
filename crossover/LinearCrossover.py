class LinearCrossover:
    def crossover(self, parent_1, parent_2):
        assert len(parent_1) == len(parent_2) == 2, "Each parent must have two genes"

        # Tworzenie nowych osobników tymczasowych Z, V i W
        z = [(1/2)*(parent_1[i] + parent_2[i]) for i in range(2)]
        v = [(3/2)*parent_1[i] - (1/2)*parent_2[i] for i in range(2)]
        w = [-(1/2)*parent_1[i] + (3/2)*parent_2[i] for i in range(2)]

        # Wybieranie 2 z 3 najlepszych osobników
        candidates = [z, v, w]
        print(candidates)
        candidates.sort(key=lambda x: sum(x))
        child_1, child_2 = candidates[0], candidates[1]
        return child_1, child_2


# Przykład do testowania
if __name__ == "__main__":
    linear_crossover_operator = LinearCrossover()

    # Osobniki rodzicielskie
    parent_1 = [2, 6]
    parent_2 = [4, 8]

    print("Parent 1:", parent_1)
    print("Parent 2:", parent_2)

    # Krzyżowanie liniowe
    child_1, child_2 = linear_crossover_operator.crossover(parent_1, parent_2)

    print("Child 1:", child_1)
    print("Child 2:", child_2)
