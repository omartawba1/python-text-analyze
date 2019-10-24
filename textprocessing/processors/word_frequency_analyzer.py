import re
from .abstract_word_frequency import AbstractWordFrequency
from .abstract_word_frequency_analyzer import AbstractWordFrequencyAnalyzer


class WordFrequencyAnalyzer(AbstractWordFrequencyAnalyzer):
    """
    Word frequency analyzer for words inside a complete sentence
    Is an implementation for AbstractWordFrequencyAnalyzer
    """

    def __init__(self, wordFrequency: AbstractWordFrequency):
        """
        WordFrequencyAnalyzer constructor
        :param wordFrequency:
        """
        self.__wordFrequency = wordFrequency

    def calculateHighestFrequency(self, text: str) -> int:
        """
        Calculate the highest frequency for a word in a sentence
        :param String text:
        :return Number :
        """
        words = {}
        for word in self.__clearDelimiters(text).split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        return max(words.values())

    def calculateFrequencyForWord(self, text: str, word: str) -> int:
        """
        Calculate the frequency for a word in a sentence.
        :param String text:
        :param String word:
        :return Number:
        """
        # return text.split().count(word)
        counter = 0
        for item in self.__clearDelimiters(text).split():
            if item == word:
                counter += 1
        return counter

    def calculateMostFrequentNWords(self, text: str, number: int) -> list:
        """
        Calculate the highest N number repeated words.
        :param text:
        :param number:
        :return List:
        """
        # word_count = Counter(text.split())
        # return word_count.most_common(number)
        words = {}
        for word in self.__clearDelimiters(text).split():
            if word in words:
                words[word].frequency += 1
            else:
                words[word] = self.__wordFrequency(word)

        sorted_x = sorted(sorted(words.values(), key=lambda w: w.word), key=lambda w: w.frequency, reverse=True)

        return sorted_x[:number]

    def __clearDelimiters(self, text: str) -> str:
        """
        Clear all the delimiters from a string except the spaces.
        :param string text:
        :return string:
        """
        return re.sub(r'([^\s\w]|_)+', '', text)
