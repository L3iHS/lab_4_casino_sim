class Player:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
    
    def __repr__(self) -> str:
        # !r явно показывает экранирование,
        # оставляет например /n для сложных имен
        return f'Player(name="{self.name!r}", balance={self.balance})'