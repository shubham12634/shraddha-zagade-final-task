class TextTools:

    def tokenize(self, text):
        """
        Split text into words by spaces.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text.split()

    def word_count(self, text):
        """
        Return number of words in text.
        """
        words = self.tokenize(text)
        return len(words)

    def frequency_map(self, text):
        """
        Return frequency of each word as a dictionary.
        """
        words = self.tokenize(text)
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        return freq

tools = TextTools()

text = "hello world hello"

print("Tokenize:", tools.tokenize(text))
print("Word Count:", tools.word_count(text))
print("Frequency Map:", tools.frequency_map(text))
