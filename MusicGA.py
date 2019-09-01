from GeneticAlgorithm import GeneticAlgorithm


class MusicGA(GeneticAlgorithm):

    def __init__(self, pop_size=50, chrom_size=8):
        GeneticAlgorithm.__init__(self, pop_size, chrom_size)
