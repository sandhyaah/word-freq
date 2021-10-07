from src.i_word_frequency_analyzer import IWordFrequencyAnalyzer


def calculate_highest_frequency(user_input):
    """
    This method returns the highest frequency from the list of texts
    :param user_input: user_entry: list of words from which frequency is calculated
    :return: returns the highest frequency word(s) with its number of occurrence
    :rtype list
    """
    most_frequent = IWordFrequencyAnalyzer(user_input).calculate_most_frequent_word()  # object instantiation
    # contains the list of most common
    highest_frequency = []  # creates empty list to store the highest frequency
    for i in range(len(most_frequent)):
        if most_frequent[i][1] == most_frequent[0][1]:  # checks if there are more that one word with same frequency
            highest_frequency.append(most_frequent[i])  # append the highest word to the list highest_frequency
    return highest_frequency  # returns the highest frequency list
