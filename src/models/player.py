class Player:
    def __init__(self, name: str, balance: int) -> None:
        if not isinstance(name, str) or not name:
            self.name = "player"
        else:
            self.name = name
        self.balance = max(1, int(balance))  # баланс должен быть >=1

    def __repr__(self) -> str:
        # !r явно показывает экранирование,
        # оставляет например /n для сложных имен
        return f'Player(name={self.name!r}, balance={self.balance})'