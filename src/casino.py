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
    
    def event_bet(self, min_bet: int=1, max_bet: int=None) -> str:
        """
        Событие: рандомный игрок делает рандомную ставку
        """
        player = self.get_random_player()
        old_balance = player.balance
        
        if old_balance == 0:
            return f"BET: {player.name} баланс 0, ставка невозможна"
        
        upper_bound = old_balance if max_bet is None else min(max_bet, old_balance)
        if min_bet > upper_bound:
            raise ValueError("Недостаточно средств для минимальной ставки")
        
        bet_amount = self.rng.randint(min_bet, upper_bound)
        new_balance = self._apply_delta(player, -bet_amount)
        log_message = f"BET: {player.name} bet_amount={bet_amount} balance {old_balance} -> {new_balance}"
        return log_message

    def event_win(self, min_win: int=1, max_win: int=None) -> str:
        """
        Событие: рандомный игрок выигрывает рандомную сумму
        """        
        player = self.get_random_player()
        old_balance = player.balance
        
        upper_bound = old_balance * 2 if max_win is None else max_win
        if min_win > upper_bound:
            raise ValueError("upper_bound меньше min_win")

        win_amount = self.rng.randint(min_win, upper_bound)
        new_balance = self._apply_delta(player, win_amount)
        log_message = f"WIN: {player.name} win_amount={win_amount} balance {old_balance} -> {new_balance}"
        return log_message
    
    def event_lose(self, min_lose: int=1, max_lose: int=None) -> str:
        """
        Событие: рандомный игрок теряет рандомную сумму
        """        
        player = self.get_random_player()
        old_balance = player.balance
        if old_balance == 0:
            return f"LOSE: {player.name} баланс 0, потерять нечего"
        
        upper_bound = old_balance if max_lose is None else min(max_lose, old_balance)
        if min_lose > upper_bound:
            raise ValueError("Недостаточно средств для минимальной потери")
        
        lose_amount = self.rng.randint(min_lose, upper_bound)
        new_balance = self._apply_delta(player, -lose_amount)
        log_message = f"LOSE: {player.name} lose_amount={lose_amount} balance {old_balance} -> {new_balance}"
        return log_message
    
    def event_wargoose_attack(self) -> str:
        """
        Событие: рандомный WarGoose атакует рандомного игрока
        """        
        player = self.get_random_player()
        old_balance = player.balance

        war_geese = [goose for goose in self.geese if isinstance(goose, WarGoose)]
        if not war_geese:
            return "ATTACK: Нет зарегистрированных WarGoose для атаки"

        war_goose = self.rng.choice(war_geese)
        damage = war_goose.attack()
        new_balance = self._apply_delta(player, -damage)
        log_message = (
            f"ATTACK: {war_goose.name} attacked {player.name} "
            f"damage={damage} balance {old_balance} -> {new_balance}"
            )
        return log_message

    def event_honkgoose_scream(self) -> str:
        """
        Событие: рандомный HonkGoose издает крик
        """        
        player = self.get_random_player()
        old_balance = player.balance
        
        honk_geese = [goose for goose in self.geese if isinstance(goose, HonkGoose)]
        if not honk_geese:
            return "HONK: Нет зарегистрированных HonkGoose для крика"

        honk_goose = self.rng.choice(honk_geese)
        scream = honk_goose()
        new_balance = self._apply_delta(player, -scream)
        
        honk_text = 'Honk! ' * min(scream, 3) + ('...' if scream > 3 else '')
        log_message = (
            f"HONK: {honk_goose.name} screamed {honk_text} "
            f"at {player.name} balance {old_balance} -> {new_balance}"
            )
        return log_message