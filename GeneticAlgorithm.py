class GeneticAlgorithm(object):

    def __init__(self, pop_size=100, chrom_size=16):
        self._POPULATION_SIZE = pop_size
        self._CHROMOSOME_SIZE = chrom_size
        self._FINAL_GENERATION = 1 # class is initialized with only one possible generation until evolve is called.
        self._initial_pop()

    def _initial_pop(self):
        pass

    def _fitness(self):
        pass

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

    def get_chrom_size(self):
        return self._CHROMOSOME_SIZE

    def get_final_gen(self):
        return self._FINAL_GENERATION
