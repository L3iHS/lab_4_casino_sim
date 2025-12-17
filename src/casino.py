import random

from models.player import Player
from models.goose import Goose, WarGoose, HonkGoose
from custom_collections.casino_balance import CasinoBalance
from custom_collections.player_collection import PlayerCollection
from custom_collections.goose_collection import GooseCollection


class Casino:
    def __init__(self, seed: int=1):
        self.players = PlayerCollection()
        self.geese = GooseCollection()
        self.balances = CasinoBalance()
        self.rng = random.Random(seed)

    def register_player(self, player: Player) -> None:
        if not isinstance(player, Player):
            raise TypeError("Аргумент player должен быть экземпляром класса Player")
        
        if self.has_player_name(player.name):
            raise ValueError(f"Игрок с именем {player.name} уже зарегистрирован")
        else:
            self.players.add(player)
            self.balances[player.name] = player.balance
            player.balance = self.balances[player.name]
    
    def register_goose(self, goose: Goose) -> None:
        if not isinstance(goose, Goose):
            raise TypeError("Аргумент goose должен быть экземпляром класса Goose")
        
        if self.has_goose_name(goose.name):
            raise ValueError(f"Гусь с именем {goose.name} уже зарегистрирован")
        else:
            self.geese.add(goose)
    
    def get_random_player(self) -> Player:
        if len(self.players) == 0:
            raise ValueError("Нет зарегистрированных игроков")
        index = self.rng.randrange(len(self.players))
        return self.players[index]

    def get_random_goose(self) -> Goose:
        if len(self.geese) == 0:
            raise ValueError("Нет зарегистрированных гусей")
        index = self.rng.randrange(len(self.geese))
        return self.geese[index]

    def has_player_name(self, name: str) -> bool:
        """
        Добавляем для читаемости кода
        """
        return name in self.balances
    
    def has_goose_name(self, name: str) -> bool:
        """
        Добавляем для читаемости кода
        """
        return name in self.geese
    
    def _sync_player_balance(self, player: Player) -> None:
        """
        Синхронизирует баланс игрока с балансом в казино
        """
        if not self.has_player_name(player.name):
            raise ValueError(
                f"Игрок с именем {player.name} не зарегистрирован в казино"
                )
        player.balance = self.balances[player.name]
    
    def _apply_delta(self, player: Player, delta: int|float) -> int:
        """
        Применяет изменение баланса игрока и синхронизирует его
        """
        if not self.has_player_name(player.name):
            raise ValueError(
                f"Игрок с именем {player.name} не зарегистрирован в казино"
                )
        new_balance = self.balances.change(player.name, delta)
        player.balance = new_balance
        return new_balance