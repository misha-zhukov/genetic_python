def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(guess.Genes, target.Genes)
               if expected == actual)

class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness