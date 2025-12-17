from __future__ import annotations

from models.goose import Goose


class GooseCollection:
    def __init__(self, items: list|None = None):
        if items is None:
            self._items = []
        else:
            for item in items:
                if not isinstance(item, Goose):
                    raise TypeError(
                        "Все элементы должны быть экземплярами класса Goose"
                        )
            self._items: list[Goose] = items.copy()
    
    def __repr__(self):
        return f"GooseCollection(len={len(self)})"
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __contains__(self, item: Goose|str) -> bool:
        if isinstance(item, str):
            return any(goose.name == item for goose in self._items)
        return item in self._items
    
    def __getitem__(self, index: int|slice) -> Goose|GooseCollection:
        if isinstance(index, slice):
            return GooseCollection(self._items[index])
        return self._items[index]
    
    def add(self, item: Goose|GooseCollection) -> None:
        if isinstance(item, Goose):
            self._items.append(item)
        elif isinstance(item, GooseCollection):
            self._items.extend(item._items)
        else:
            raise TypeError(
                "Аргумент должен быть экземпляром класса Goose или GooseCollection"
                )
    
    def remove(self, item: Goose) -> bool:
        try:
            self._items.remove(item)
            return True
        except ValueError:
            return False

    def pop(self, index: int=-1) -> Goose:
        return self._items.pop(index)