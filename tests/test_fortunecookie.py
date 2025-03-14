import pytest
import random
from fortunecookiepkg.fortunecookie import (
    get_random_fortune,
    get_lucky_numbers,
    get_daily_fortune,
    get_custom_fortune,
    get_themed_fortune,
)

class Tests:
    
    # if valid input, array should be the length of given input
    def test_lucky_numbers_length_valid(self):
        valid_len = random.randint(1, 10)
        res = get_lucky_numbers(valid_len)
        assert len(res) == valid_len, f"Expected get_lucky_numbers() to return {valid_len} numbers. Instead, it returned an array with {len(res)} numbers"

    # if invalid input, array should be length 0
    def test_lucky_numbers_length_invalid(self):
        invalid_len = random.randint(11, 100)
        res = get_lucky_numbers(invalid_len)
        assert len(res) == 0, f"Expected get_lucky_numbers() to return 0 numbers. Instead, it returned an array with {len(res)} numbers"  

    # given the same length, two outputs should not be the same (ensure randomness)
    def test_lucky_numbers_randomness(self):
        valid_len = random.randint(1, 10)
        res1 = get_lucky_numbers(valid_len)
        res2 = get_lucky_numbers(valid_len)
        assert res1 != res2, f"Expected get_lucky_numbers() to return 2 different arrays, given the same length. Instead, it returned two arrays with identical values"

    