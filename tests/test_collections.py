from src.models.player import Player
from src.models.goose import Goose, WarGoose
from src.custom_collections.player_collection import PlayerCollection
from src.custom_collections.goose_collection import GooseCollection


def test_player_collection_len_iter_getitem():
    p1 = Player("A", 10)
    p2 = Player("B", 20)
    pc = PlayerCollection([p1, p2])

    assert len(pc) == 2
    assert list(pc) == [p1, p2]
    assert pc[0] == p1
    assert pc[1] == p2


def test_player_collection_slice_returns_collection():
    p1 = Player("A", 10)
    p2 = Player("B", 20)
    p3 = Player("C", 30)
    pc = PlayerCollection([p1, p2, p3])

    sub = pc[1:]
    assert isinstance(sub, PlayerCollection)
    assert len(sub) == 2
    assert sub[0] == p2


def test_player_collection_remove_and_pop():
    p1 = Player("A", 10)
    p2 = Player("B", 20)
    pc = PlayerCollection([p1, p2])

    assert pc.remove(p1) is True
    assert pc.remove(p1) is False  # уже нет
    popped = pc.pop()
    assert popped == p2
    assert len(pc) == 0


def test_goose_collection_basic():
    g1 = Goose("G1", 1)
    g2 = WarGoose("G2", 2)
    gc = GooseCollection([g1, g2])

    assert len(gc) == 2
    assert list(gc) == [g1, g2]
    assert gc[0] == g1

    sub = gc[:1]
    assert isinstance(sub, GooseCollection)
    assert len(sub) == 1