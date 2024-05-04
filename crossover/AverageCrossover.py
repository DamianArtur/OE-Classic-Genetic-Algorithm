class AverageCrossover:
    def crossover(self, parents):
        assert len(parents) >= 2
        assert all(len(parent) == 2 for parent in parents)

        num_parents = len(parents)
        num_genes = len(parents[0])

        child = [sum(gene[i] for gene in parents) / num_parents for i in range(num_genes)]
        return child