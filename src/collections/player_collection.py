from __future__ import annotations

from models.player import Player


class PlayerCollection:
    def __init__(self, items: list|None=None):
        if items is None:
            self._items = []
        else:
            for item in items:
                if not isinstance(item, Player):
                    raise TypeError("Все элементы items должны быть Player")
            self._items = items.copy()
    
    def __repr__(self) -> str:
        return f"PlayerCollection(len={len(self)})"
        
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index: int|slice) -> Player|PlayerCollection:
        '''
        Получение элементов по индексу или срезу
        '''
        if isinstance(index, slice):
            return PlayerCollection(self._items[index])
        return self._items[index]
    
    def add(self, item: Player|PlayerCollection) -> None:
        if isinstance(item, PlayerCollection):
            self._items.extend(item._items)
        elif isinstance(item, Player):
            self._items.append(item)
        else:
            raise TypeError("item может быть только Player или PlayerCollection")
    
    def remove(self, player: Player) -> bool:
        '''
        Удаляем первое вхождение player из коллекции.
        '''
        # не делаю провереку на in, чтобы не было два прохода
        try:
            self._items.remove(player)
            return True
        except ValueError:
            return False
    
    def pop(self, index: int=-1) -> Player:
        '''
        Удаляет и возвращает элемент по индексу.
        '''
        return self._items.pop(index)