from src.casino import Casino
from src.models.player import Player
from src.models.goose import WarGoose, HonkGoose


def make_casino(seed: int = 1) -> Casino:
    casino = Casino(seed=seed)
    casino.register_player(Player("P", 50))
    casino.register_goose(WarGoose("WG", 10))
    casino.register_goose(HonkGoose("HG", 5))
    return casino


def test_event_bet_decreases_balance():
    casino = make_casino(seed=1)
    player = casino.players[0]
    old = player.balance

    log = casino.event_bet(min_bet=1, max_bet=10)

    assert player.balance <= old
    assert log.startswith("BET:")


def test_event_win_increases_balance():
    casino = make_casino(seed=1)
    player = casino.players[0]
    old = player.balance

    log = casino.event_win(min_win=1, max_win=10)

    assert player.balance >= old
    assert log.startswith("WIN:")


def test_event_lose_decreases_balance():
    casino = make_casino(seed=1)
    player = casino.players[0]
    old = player.balance

    log = casino.event_lose(min_lose=1, max_lose=10)

    assert player.balance <= old
    assert log.startswith("LOSE:")


def test_event_wargoose_attack_decreases_balance_by_damage():
    casino = make_casino(seed=1)
    player = casino.players[0]
    old = player.balance

    log = casino.event_wargoose_attack()

    assert player.balance == old - 10
    assert log.startswith("ATTACK:")


def test_event_honkgoose_scream_decreases_balance_by_effect():
    casino = make_casino(seed=1)
    player = casino.players[0]
    old = player.balance

    log = casino.event_honkgoose_scream()

    # денежный урон = honk_volume (тк __call__ возвращает число)
    assert player.balance == old - 5
    assert log.startswith("HONK:")