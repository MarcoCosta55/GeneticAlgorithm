from GeneticAlgorithm import GeneticAlgorithm


class StringGA(GeneticAlgorithm):

    def __init__(self, sample_string="Monty"):
        GeneticAlgorithm.__init__(self, pop_size=100, chrom_size=len(sample_string), g_size=56)
