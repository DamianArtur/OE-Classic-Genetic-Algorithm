class LinearCrossover:
    def crossover(self, parent_1, parent_2):
        assert len(parent_1) == len(parent_2) == 2

        z = [(1/2)*(parent_1[i] + parent_2[i]) for i in range(2)]
        v = [(3/2)*parent_1[i] - (1/2)*parent_2[i] for i in range(2)]
        w = [-(1/2)*parent_1[i] + (3/2)*parent_2[i] for i in range(2)]

        candidates = [z, v, w]
        candidates.sort(key=lambda x: sum(x))
        child_1, child_2 = candidates[0], candidates[1]
        return child_1, child_2
