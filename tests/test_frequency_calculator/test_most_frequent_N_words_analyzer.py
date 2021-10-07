from src.frequency_calculator.most_frequent_N_words_analyzer import calculate_most_frequent_n_words
import pytest


@pytest.mark.parametrize('user_input,number,result',
                         [
                             (['where', 'there', 'is', 'a', 'will', 'there', 'is', 'a', 'way'], 2, [('a', 2), ('is', 2)]),
                             (['can', 'you', 'can', 'a', 'can', 'as', 'a', 'canner', 'can', 'can', 'a', 'can'], 1, [('can', 6)]),
                             (['sun'], 1, [('sun', 1)]),
                             (['a', 'is', 'for', 'apple', 'a', 'a', 'apple'], 3, [('a', 3), ('apple', 2), ('for', 1)]),
                             (['q', 'r', 's', 't', 'u', 'q', 'q', 'q'], 4, [('q', 4), ('r', 1), ('s', 1), ('t', 1)])
                         ]
                         )
def test_calculate_most_frequent_n_words_positive(user_input, number, result):
    most_frequent_n_word = calculate_most_frequent_n_words(user_input, number)
    assert most_frequent_n_word == result


@pytest.mark.parametrize('user_input,number,result',
                         [
                             (['where', 'there', 'is', 'a', 'will', 'there', 'is', 'a', 'way'], 3, [('a', 3), ('is', 2), ('there', 2)]),
                             (['i', 'can', 'i', 'will'], 6, [('i', 2)])
                         ]
                         )
def test_calculate_most_frequent_n_words_negative(user_input, number, result):
    most_frequent_n_word = calculate_most_frequent_n_words(user_input, number)
    assert not most_frequent_n_word == result
