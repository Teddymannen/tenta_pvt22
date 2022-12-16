import pytest
import nobel_prize

test_list = [
    (1000, "1/3", 333.333),
    (1000, "1/2", 500),
    (1000, "1", 1000),
    (1000, "2/3", 666.667)
]


@pytest.mark.parametrize("prize, share, output", test_list)
def test_prize_share_calc(prize, share, output):
    assert nobel_prize.prize_share_calc(prize, share) == output
