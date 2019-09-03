from random import randrange
import pandas as pd


class GeneticAlgorithm(object):

    def __init__(self, pop_size=10, chrom_len=10, g_size=11):
        """
        Initializes our first generation population of chromosomes that all have randomly generated integer type genes.
        :param pop_size: the size of the entire population.
        :param chrom_len: how many genes are in a chromosome. (eg strand of DNA)
        :param g_size: how many possibilities are held within each gene. (eg. for human DNA this number would be 3)
        """
        self._POPULATION_SIZE = pop_size
        self._CHROMOSOME_LENGTH = chrom_len
        self._GENE_SIZE = g_size
        self._FINAL_GENERATION = 1

        # initializing our class variable 'population' to be a DataFrame of randomly generated chromosomes
        # and NaN fitness values.
        self.population = pd.DataFrame(columns=['chromosome', 'fitness'], index=range(0,pop_size))
        for i in range(pop_size):
            temp_gene = []
            for c in range(chrom_len):
                temp_gene.append(randrange(g_size))
            self.population['chromosome'][i] = temp_gene

    def __str__(self):
        """
        Makes it possible to print the entire GeneticAlgorithm object.
        :return: the entire population DataFrame cast as a string
        """
        return str(self.population)

    def _fitness(self):
        """
        Simple placeholder fitness function that determines fitness based on the value of the sum of all genes.
        This function is designed to be overridden by child classes as it really has no practical use.
        """
        for i in range(self._POPULATION_SIZE):
            self.population['fitness'][i] = sum(self.population['chromosome'][i])

        self.population = self.population.sort_values('fitness', ascending=False)
        self.population = self.population.reset_index(drop=True)

    def evolve(self, gen=1):
        self._FINAL_GENERATION = gen
        for i in range(gen):
            self._fitness()
            self._mate()

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
