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
    #Fixtures
    @pytest.fixture
    def example_fixture(self):
        """
        An example fixture used for setup/teardown before/after tests are run.
        """
        yield
        
    #Test functions
    def test_sanity_check(self, example_fixture):
        """
        Test debugging is working with a simple check.
        """
        expected = True
        actual = True
        assert actual==expected, "Expected True to equal True."
    
    def test_lucky_numbers_length_valid(self):
        """
        If the input is valid, the array should be the same length as the given input"
        """
        valid_len = random.randint(1, 10)
        res = get_lucky_numbers(valid_len)
        assert len(res) == valid_len, f"Expected get_lucky_numbers() to return {valid_len} numbers. Instead, it returned an array with {len(res)} numbers"

    def test_lucky_numbers_length_invalid(self):
        """
        If there is invalid input, the array should have length of 0.
        """
        invalid_len = random.randint(11, 100)
        res = get_lucky_numbers(invalid_len)
        assert len(res) == 0, f"Expected get_lucky_numbers() to return 0 numbers. Instead, it returned an array with {len(res)} numbers"  

    def test_lucky_numbers_randomness(self):
        """
        Given the same length, two outputs should not be the same which ensures randomness.
        """
        valid_len = random.randint(1, 10)
        res1 = get_lucky_numbers(valid_len)
        res2 = get_lucky_numbers(valid_len)
        assert res1 != res2, f"Expected get_lucky_numbers() to return 2 different arrays, given the same length. Instead, it returned two arrays with identical values"

    