from collections import Counter


class IWordFrequencyAnalyzer:

    def __init__(self, user_input):
        self.user_input = user_input

    def calculate_most_frequent_word(self):
        return Counter(self.user_input).most_common()
