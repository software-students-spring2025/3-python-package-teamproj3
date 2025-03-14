import pytest;
from fortunecookiepkg.fortunecookie import (
    get_random_fortune,
    get_lucky_numbers,
    get_daily_fortune,
    get_custom_fortune,
    get_themed_fortune,
)

class Tests:

    def test_lucky_length(self):
        res = get_lucky_numbers();
        assert len(res) == 6, f"Expected get_lucky_numbers() to return 6 numbers. Instead, it returned an array with {len(res)} numbers"

    