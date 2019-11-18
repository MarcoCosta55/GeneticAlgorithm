"""
NOT YET IMPLEMENTED
This class will extend the GeneticAlgorithm class. Main functions will be override how the chromosomes are encoded and
create a fitness function that tests the chromosome when compared to classical baroque melodic rules.
"""

from GeneticAlgorithm import GeneticAlgorithm


class MusicGA(GeneticAlgorithm):

    def __init__(self, pop_size=10, chrom_len=10, g_size=45):

        # This dictionary provides the basic decoding mechanism for each gene. Each gene that is generated corresponds
        # to a key in the dictionary that references a tuple. The tuple will provide a more verbose definition of the
        # melody. It is encoded as follows: ('Note', int rep. of note, int rep of note length). The int representation
        # of note length is 1 = whole, 4 = quarter, etc.
        self._NOTE_DICT = {0: ('C', 0, 1), 1: ('C', 0, 2), 2: ('C', 0, 4), 3: ('C', 0, 8), 4: ('C', 0, 16),
                           5: ('C#', 1, 1), 6: ('C#', 1, 2), 7: ('C#', 1, 4), 8: ('C#', 1, 8), 9: ('C#', 1, 16),
                           10: ('D', 2, 1), 11: ('D', 2, 2), 12: ('D', 2, 4), 13: ('D', 2, 8), 14: ('D', 2, 16),
                           15: ('D#', 3, 1), 16: ('D#', 3, 2), 17: ('D#', 3, 4), 18: ('D#', 3, 8), 19: ('D#', 3, 16),
                           20: ('E', 4, 1), 21: ('E', 4, 2), 22: ('E', 4, 4), 23: ('E', 4, 8), 24: ('E', 4, 16),
                           25: ('F', 5, 1), 26: ('F', 5, 2), 27: ('F', 5, 4), 28: ('F', 5, 8), 29: ('F', 5, 16),
                           30: ('F#', 6, 1), 31: ('F#', 6, 2), 32: ('F#', 6, 4), 33: ('F#', 6, 8), 34: ('F#', 6, 16),
                           35: ('G', 7, 1), 36: ('G', 7, 2), 37: ('G', 7, 4), 38: ('G', 7, 8), 39: ('G', 7, 16),
                           40: ('G#', 8, 1), 41: ('G#', 8, 2), 42: ('G#', 8, 4), 43: ('G#', 8, 8), 44: ('G#', 8, 16)}

        # G_SIZE directly relates to the _NOTE_DICT size and should not be changed unless the note dictionary changes.
        GeneticAlgorithm.__init__(self, pop_size, chrom_len, g_size)

    def __str__(self) -> 'string':
        """
        This will print the first (most fit) chromosome as a comma separated string that is readable in english.
        :return: string type object.
        """
        music_string = ''
        for i in range(self._CHROMOSOME_LENGTH):
            music_string += self._NOTE_DICT[self.population['chromosome'][1][i]][0] + \
                            str(self._NOTE_DICT[self.population['chromosome'][1][i]][2]) + ', '

        return music_string

    def _fitness(self):
        for i in range(self._POPULATION_SIZE):
            jump_fitness = self._jump_fitness(self.population['chromosome'][i])
            self.population['fitness'][i] = jump_fitness

    def _jump_fitness(self, curr_chrom):
        jump_total = 0
        i = 0

        while i < self._CHROMOSOME_LENGTH - 1:
            if abs(self._NOTE_DICT[curr_chrom[i]][1] - self._NOTE_DICT[curr_chrom[i+1]][1]) <= 3:
                jump_total += 10
            else:
                jump_total += 0
            i += 1

        return jump_total
