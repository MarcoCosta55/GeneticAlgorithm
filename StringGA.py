from GeneticAlgorithm import GeneticAlgorithm


class StringGA(GeneticAlgorithm):

    def __init__(self, sample_string="Monty"):

        self._ascii_dict = {i: chr(i) for i in range(129)}

        GeneticAlgorithm.__init__(self, pop_size=100, chrom_len=len(sample_string), g_size=len(self._ascii_dict))
