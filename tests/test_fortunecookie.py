import pytest
import random
from fortunecookiepkg.fortunecookie import (
    FORTUNES,
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
    
    '''
    If valid input, array should be the length of given input
    '''
    def test_lucky_numbers_length_valid(self):
        """
        If the input is valid, the array should be the same length as the given input"
        """
        valid_len = random.randint(1, 10)
        res = get_lucky_numbers(valid_len)
        assert len(res) == valid_len, f"Expected get_lucky_numbers() to return {valid_len} numbers. Instead, it returned an array with {len(res)} numbers"
    '''
    If invalid input, array should be length 0
    '''
    def test_lucky_numbers_length_invalid(self):
        """
        If there is invalid input, the array should have length of 0.
        """
        invalid_len = random.randint(11, 100)
        res = get_lucky_numbers(invalid_len)
        assert len(res) == 0, f"Expected get_lucky_numbers() to return 0 numbers. Instead, it returned an array with {len(res)} numbers"  
    '''
    Given the same length, two outputs should not be the same (ensure randomness)
    '''
    def test_lucky_numbers_randomness(self):
        """
        Given the same length, two outputs should not be the same which ensures randomness.
        """
        valid_len = random.randint(1, 10)
        res1 = get_lucky_numbers(valid_len)
        res2 = get_lucky_numbers(valid_len)
        assert res1 != res2, f"Expected get_lucky_numbers() to return 2 different arrays, given the same length. Instead, it returned two arrays with identical values"
    '''
    Output should include the given name
    '''
    def test_get_custom_fortune_name(self):
        name = "Sam"
        res = get_custom_fortune(name)
        assert name in res, f"Expected '{name}' in the output but got '{res}'"
    '''
    If the name is empty, function should still return a valid fortune
    '''
    def test_get_custom_fortune_empty_name(self):
        res = get_custom_fortune("")
        assert isinstance(res, str), "Expected output to be a string"
        assert res.strip() != "", "Expected a non-empty fortune, but got an empty string"
    '''
    If system has lenght limits or unexpected behavior with long strings, function should still work
    '''
    def test_get_custom_fortune_long_name(self):
        name = "A" * 100
        res = get_custom_fortune(name)
        assert name in res, f"Expected the long name in the output but got '{res}'"
    '''
    Provided theme should be valid
    '''
    def test_get_themed_fortune_invalid_theme(self):
        res = get_themed_fortune("unknown")
        assert "There are no fortunes for your provided theme" in res, f"Expected an error message but got '{res}'"
    '''
    If an empty string is given as a theme, it should return an error message
    '''
    def test_get_themed_fortune_empty(self):
        res = get_themed_fortune("")
        assert "There are no fortunes for your provided theme" in res, f"Expected an error message but got '{res}'"
    ''' 
    If there are spaces, handle extra spaces
    '''
    @pytest.mark.parametrize("theme", [" love ", "  career  ", " happiness "])
    def test_get_themed_fortune_spaces(self, theme):
        res = get_themed_fortune(theme.strip())
        assert isinstance(res, str), "Expected output to be a string"
        assert len(res) > 0, f"Expected a non-empty fortune but got '{res}'"

    #Daily Fortune Tests
    '''
    Tests if the daily fortune is being accessed properly
    '''
    def test_daily_fortune_date(self):
        fortune1 = get_daily_fortune()
        fortune2 = get_daily_fortune()

        assert fortune1 != fortune2
        assert FORTUNES(FORTUNES.index(fortune1) + 1) == fortune2 

    '''
    Tests that the fortune for each day exists in the FORTUNE array
    '''
    def test_daily_fortune_exists(self):
        fortune = get_daily_fortune()
        assert fortune in FORTUNES

    '''
    Tests that the fortune for each day remains consistent
    '''
    def test_daily_fortune_accurate(self):
        fortune1 = get_daily_fortune()
        fortune2 = get_daily_fortune()
        assert (fortune1 == fortune2)

    '''
    Tests that the daily fortune function returns a string
    '''
    def test_daily_fortune_returns_string(self):
        fortune = get_daily_fortune()
        assert isinstance(fortune, str)