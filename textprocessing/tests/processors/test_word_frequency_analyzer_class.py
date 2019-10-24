import pytest

from textprocessing.processors.abstract_word_frequency_analyzer import AbstractWordFrequencyAnalyzer
from textprocessing.processors.word_frequency import WordFrequency
from textprocessing.processors.word_frequency_analyzer import WordFrequencyAnalyzer


class TestWordFrequencyAnalyzerClass:
    TEST_WORD1 = 'The'
    TEST_WORD2 = 'lake'
    TEST_TEXT = 'The sun shines# over% The lake'
    TEST_FREQUENCY = 2

    def test_it_requires_a_word_frequency_instance(self):
        with pytest.raises(TypeError):
            WordFrequencyAnalyzer()

    def test_it_extends_abstract_word_frequency_analyzer(self):
        assert issubclass(WordFrequencyAnalyzer, AbstractWordFrequencyAnalyzer)

    def test_it_calculates_highest_frequency_correctly(self):
        instance = self.__getAnalyzerInstance()
        assert instance.calculateHighestFrequency(self.TEST_TEXT) is self.TEST_FREQUENCY

    def test_it_calculates_word_frequency_correctly(self):
        instance = self.__getAnalyzerInstance()
        assert instance.calculateFrequencyForWord(self.TEST_TEXT, self.TEST_WORD1) is self.TEST_FREQUENCY

    def test_it_calculates_most_frequent_n_words_correctly(self):
        instance = self.__getAnalyzerInstance()
        results = instance.calculateMostFrequentNWords(self.TEST_TEXT, self.TEST_FREQUENCY)
        expected = [WordFrequency(self.TEST_WORD1, 2), WordFrequency(self.TEST_WORD2, 1)]
        assert results == expected

    def __getAnalyzerInstance(self):
        return WordFrequencyAnalyzer(WordFrequency)
