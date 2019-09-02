from GeneticAlgorithm import GeneticAlgorithm


class MusicGA(GeneticAlgorithm):

    def __init__(self, pop_size=10, chrom_len=10, g_size=11):
        GeneticAlgorithm.__init__(self, pop_size, chrom_len, g_size)
