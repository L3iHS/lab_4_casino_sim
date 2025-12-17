class CasinoBalance:
    def __init__(self, data: dict|None=None):
        self._data = data.copy() if data is not None else {}
    
    def __repr__(self) -> str:
        return f"CasinoBalance(data={self._data})"
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __iter__(self):
        return iter(self._data)
    
    def __getitem__(self, name: str) -> int:
        '''
        Получение баланса по имени игрока
        '''
        try:
            return self._data[name]
        except KeyError:
            raise KeyError(f"Игрок с именем {name} не найден")
        
    def __setitem__(self, name: str, balance: int|float) -> None:
        '''
        Установка баланса по имени игрока
        '''
        balance = max(0, int(balance)) # баланс должен быть >= 0
        old_balance = self._data.get(name)
        if name in self._data:
            print(f"Баланс игрока {name} изменен с {old_balance} на {balance}")
        else:
            print(f"Баланс игрока {name} установлен в {balance}")
        
        self._data[name] = balance
        
    def __delitem__(self, name: str) -> None:
        '''
        Удаление игрока по имени
        '''
        try:
            del self._data[name]
        except KeyError:
            raise KeyError(f"Игрок с именем {name} не найден")
    
    def change(self, name: str, delta: int|float) -> int:
        '''
        Изменение баланса игрока на += delta
        '''
        try:
            current_balance = self._data[name]
        except KeyError:
            raise KeyError(f"Игрок с именем {name} не найден")
        
        new_balance = max(0, current_balance + int(delta))
        self[name] = new_balance  # используем __setitem__ для логирования
        return new_balance
    
    def items(self):
        return self._data.items()