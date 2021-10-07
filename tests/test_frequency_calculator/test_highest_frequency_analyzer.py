from src.frequency_calculator.highest_frequency_analyzer import calculate_highest_frequency
import pytest


@pytest.mark.parametrize('user_input,result',
                         [
                             (['where', 'there', 'is', 'a', 'will', 'there', 'is', 'a', 'way'], [('there', 2), ('is', 2), ('a', 2)]),
                             (['can', 'you', 'can', 'a', 'can', 'as', 'a', 'canner', 'can', 'can', 'a', 'can'], [('can', 6)]),
                             (['sun'], [('sun', 1)]),
                             (['a', 'is', 'for', 'apple', 'a', 'a', 'apple'], [('a', 3)]),
                             (['q', 'r', 's', 't', 'u', 'q', 'q', 'q'], [('q', 4)]),
                         ]
                         )
def test_calculate_highest_frequency_positive(user_input, result):
    highest_frequency = calculate_highest_frequency(user_input)
    assert highest_frequency == result


@pytest.mark.parametrize('user_input,result',
                         [
                             (['where', 'there', 'is', 'a', 'will', 'there', 'is', 'a', 'way'], [('way', 3)]),
                             (['i', 'can', 'i', 'will'], [('i', 6)])
                         ]
                         )
def test_calculate_highest_frequency_negative(user_input, result):
    highest_frequency = calculate_highest_frequency(user_input)
    assert not highest_frequency == result
