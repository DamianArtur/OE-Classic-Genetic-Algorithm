import random


class BLXAlphaBetaCrossover:
    def crossover(self, parent_1, parent_2, alpha, beta):
        assert len(parent_1) == len(parent_2) == 2

        dx = abs(parent_1[0] - parent_2[0])
        dy = abs(parent_1[1] - parent_2[1])

        child_1 = []
        child_2 = []

        min_val_x = min(parent_1[0], parent_2[0])
        max_val_x = max(parent_1[0], parent_2[0])
        min_val_y = min(parent_1[1], parent_2[1])
        max_val_y = max(parent_1[1], parent_2[1])

        min_range_child_x = min_val_x - alpha * dx
        max_range_child_x = max_val_x + beta * dx
        child_1_x_gene = random.uniform(min_range_child_x, max_range_child_x)
        child_1.append(child_1_x_gene)

        min_range_child_y = min_val_y - alpha * dy
        max_range_child_y = max_val_y + beta * dy
        child_1_y_gene = random.uniform(min_range_child_y, max_range_child_y)
        child_1.append(child_1_y_gene)

        min_range_child_x = min_val_x - alpha * dx
        max_range_child_x = max_val_x + beta * dx
        child_2_x_gene = random.uniform(min_range_child_x, max_range_child_x)
        child_2.append(child_2_x_gene)

        min_range_child_y = min_val_y - alpha * dy
        max_range_child_y = max_val_y + beta * dy
        child_2_y_gene = random.uniform(min_range_child_y, max_range_child_y)
        child_2.append(child_2_y_gene)

        return child_1, child_2