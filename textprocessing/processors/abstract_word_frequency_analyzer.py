class AbstractWordFrequencyAnalyzer:
    def calculateHighestFrequency(self, text):
        raise NotImplementedError('Please implement the calculateHighestFrequency method')

    def calculateFrequencyForWord(self, text, word):
        raise NotImplementedError('Please implement the calculateFrequencyForWord method')

    def calculateMostFrequentNWords(self, text, number):
        raise NotImplementedError('Please implement the calculateMostFrequentNWords method')
