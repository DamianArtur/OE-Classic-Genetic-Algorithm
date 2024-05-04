class AverageCrossover:
    def crossover(self, parents):
        assert len(parents) >= 2
        assert all(len(parent) == 2 for parent in parents)

        num_parents = len(parents)
        num_genes = len(parents[0])

        child = [sum(gene[i] for gene in parents) / num_parents for i in range(num_genes)]

        return child


# Przykład do testowania
if __name__ == "__main__":
    average_crossover_operator = AverageCrossover()

    # Osobniki rodzicielskie
    parents = [[4, 3], [4, 7]]

    print("Parents:", parents)

    # Krzyżowanie uśredniające
    child = average_crossover_operator.crossover(parents)

    print("Child:", child)