from textprocessing.processors.word_frequency_analyzer import WordFrequencyAnalyzer
from textprocessing.processors.word_frequency import WordFrequency

word = 'The'
text = 'The sun shines over The lake'
frequency = 3

analyzer = WordFrequencyAnalyzer(WordFrequency)
print(analyzer.calculateHighestFrequency(text))
print(analyzer.calculateFrequencyForWord(text, word))
print(analyzer.calculateMostFrequentNWords(text, frequency))
