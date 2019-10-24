import pytest

from textprocessing.processors.abstract_word_frequency import AbstractWordFrequency
from textprocessing.processors.word_frequency import WordFrequency


class TestWordFrequencyClass:
    __TEST_WORD = 'The'
    __TEST_FREQUENCY = 3

    def test_it_requires_a_word(self):
        with pytest.raises(TypeError):
            WordFrequency()

    def test_it_extends_abstract_word_frequency(self):
        assert issubclass(WordFrequency, AbstractWordFrequency)

    def test_it_stores_word_properly(self):
        instance = WordFrequency(self.__TEST_WORD)
        assert instance.word is self.__TEST_WORD

    def test_it_stores_frequency_properly(self):
        instance = WordFrequency(self.__TEST_WORD)
        instance.frequency = self.__TEST_FREQUENCY
        assert instance.frequency is self.__TEST_FREQUENCY
