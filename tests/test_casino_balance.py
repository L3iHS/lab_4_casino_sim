import pytest

from src.custom_collections.casino_balance import CasinoBalance


def test_balance_set_and_get():
    b = CasinoBalance()
    b["Alice"] = 10
    assert b["Alice"] == 10


def test_balance_change_increases():
    b = CasinoBalance()
    b["Alice"] = 10
    new_balance = b.change("Alice", 5)
    assert new_balance == 15
    assert b["Alice"] == 15


def test_balance_change_decreases():
    b = CasinoBalance()
    b["Alice"] = 10
    new_balance = b.change("Alice", -3)
    assert new_balance == 7
    assert b["Alice"] == 7


def test_balance_never_negative():
    b = CasinoBalance()
    b["Alice"] = 3
    b.change("Alice", -100)
    assert b["Alice"] == 0


def test_balance_change_unknown_player_raises():
    b = CasinoBalance()
    with pytest.raises(KeyError):
        b.change("Unknown", 5)