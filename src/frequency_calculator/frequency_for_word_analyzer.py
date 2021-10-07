from src.i_word_frequency_analyzer import IWordFrequencyAnalyzer


def calculate_frequency_for_word(user_input, word):
    """
    This method returns the frequency of a particular word
    :param user_input: user_input: list of words from which frequency is calculated
    :param word: str to calculate frequency of this word in the list
    :return: int
    """
    most_frequent = dict(IWordFrequencyAnalyzer(user_input).calculate_most_frequent_word())  # object instantiation
    # contains the dict of most_common
    if word in most_frequent:  # checks for the word in the list most_frequent
        return most_frequent.get(word)  # returns the frequency in number

