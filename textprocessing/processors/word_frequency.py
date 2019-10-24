from .abstract_word_frequency import AbstractWordFrequency


class WordFrequency(AbstractWordFrequency):
    """
    A word class to hold the word itself and it's associated frequency.
    """

    def __init__(self, word: str, frequency: int = 1):
        self.__word = word
        self.__frequency = frequency

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, value):
        self.__word = value

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        self.__frequency = value

    def __eq__(self, other):
        return self.word == other.word and self.frequency == other.frequency
