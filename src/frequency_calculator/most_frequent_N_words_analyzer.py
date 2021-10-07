from src.i_word_frequency_analyzer import IWordFrequencyAnalyzer


def calculate_most_frequent_n_words(user_input, number):
    """
    This method returns the list of most frequent N word(s)
    returns in alphabetical order if more than one word has same frequency
    :param user_input: list of words from which frequency is calculated
    :param number: int
    :return: list
    """
    user_input.sort()  # sorts the list in alphabetical order
    most_frequent = IWordFrequencyAnalyzer(user_input).calculate_most_frequent_word()  # object instantiation
    # contains the list of most common
    return most_frequent[:number]  # slicing to get expected output
