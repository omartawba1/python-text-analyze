# Text processor package
A simple package for analyzing a text and provide tiny details about word frequencies inside any text

# Usage
```
word = 'The'
text = 'The sun shines over The lake'
frequency = 3
analyzer = WordFrequencyAnalyzer(WordFrequency)
print(analyzer.calculateHighestFrequency(text))
print(analyzer.calculateFrequencyForWord(text, word))
print(analyzer.calculateMostFrequentNWords(text, frequency))
```

# Testing
You could run this command to run the tests
```
pytest
```
