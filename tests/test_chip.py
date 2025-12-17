from src.models.chip import Chip


def test_chip_add():
    c1 = Chip(2)
    c2 = Chip(3)
    result = c1 + c2
    assert result.value == 5


def test_chip_sum():
    chips = [Chip(1), Chip(2), Chip(3)]
    total = sum(chips)
    assert total.value == 6
    
def test_chip_min_value():
    c = Chip(-10)
    assert c.value == 1