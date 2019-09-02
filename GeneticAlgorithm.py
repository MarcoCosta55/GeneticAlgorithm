from random import randrange
import pandas as pd


class GeneticAlgorithm(object):

    def __init__(self, pop_size=10, chrom_len=10, g_size=11):
        """
        :param pop_size:
        :param chrom_len:
        :param g_size:
        """
        self._POPULATION_SIZE = pop_size
        self._CHROMOSOME_LENGTH = chrom_len  # how many genes are in each chromosomes.
        self._GENE_SIZE = g_size  # this controls how many possible variations of each gene there are.
        self._FINAL_GENERATION = 1  # class is initialized with only one possible generation until evolve is called.

        # setting up an initial population.
        self.population = pd.DataFrame(columns=['chromosome', 'fitness'], index=range(0,pop_size))
        for i in range(pop_size):
            temp_gene = []
            for c in range(chrom_len):
                temp_gene.append(randrange(g_size))
            self.population['chromosome'][i] = temp_gene
        self._fitness()

        print(self.population)

    def _fitness(self):
        for i in range(self._POPULATION_SIZE):
            self.population['fitness'][i] = sum(self.population['chromosome'][i])

    def evolve(self, gen):
        self._FINAL_GENERATION = gen

    def _mating_pool(self):
        pass

    def _mate(self):
        self._crossover()
        self._mutate()

    def _crossover(self):
        pass

    def _mutate(self):
        pass

    def get_pop_size(self):
        return self._POPULATION_SIZE

    def get_chrom_length(self):
        return self._CHROMOSOME_LENGTH

    def get_final_gen(self):
        return self._FINAL_GENERATION

    def get_gene_size(self):
        return self._GENE_SIZE
