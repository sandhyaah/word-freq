from src.frequency_calculator.frequency_for_word_analyzer import calculate_frequency_for_word
import pytest


@pytest.mark.parametrize('user_input,word,result',
                         [
                             (['where', 'there', 'is', 'a', 'will', 'there', 'is', 'a', 'way'], 'a', 2),
                             (['can', 'you', 'can', 'a', 'can', 'as', 'a', 'canner', 'can', 'can', 'a', 'can'], 'as', 1),
                             (['sun'], 'sun', 1),
                             (['a', 'is', 'for', 'apple', 'a', 'a', 'apple'], 'a', 3),
                             (['q', 'r', 's', 't', 'u', 'q', 'q', 'q'], 's', 1),
                         ]
                         )
def test_calculate_frequency_for_word_analyzer_positive(user_input, word, result):
    frequency_for_word = calculate_frequency_for_word(user_input, word)
    assert frequency_for_word == result


@pytest.mark.parametrize('user_input, word, result',
                         [
                             (['where', 'there', 'is', 'a', 'will', 'there', 'is', 'a', 'way'], 'way', 3),
                             (['i', 'can', 'i', 'will'], 'z', 6)
                         ]
                         )
def test_calculate_frequency_for_word_analyzer_negative(user_input, word, result):
    frequency_for_word = calculate_frequency_for_word(user_input, word)
    assert not frequency_for_word == result
